"""
src/context1/core/config.py
配置管理核心 - 职责：加载三级配置、合并规则、提供全局配置单例
"""
import json
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

# --- 默认硬编码配置 (Layer 1 Base Rules) ---
DEFAULT_CONFIG = {
    "output": {
        "default_format": "markdown",
        "follow_symlinks": False,
        "max_file_size_kb": 500
    },
    "filters": {
        "use_gitignore": True,
        # 总是排除的扩展名 (二进制/媒体/压缩包)
        "binary_extensions": [
            ".exe", ".dll", ".so", ".dylib", ".bin", ".pkl",
            ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
            ".zip", ".tar", ".gz", ".7z", ".rar", ".pdf",
            ".pyc", ".pyo", ".pyd", ".class"
        ],
        # 总是排除的目录/文件 (无论什么策略)
        "always_exclude": [
            ".git", ".svn", ".hg", ".idea", ".vscode",
            ".DS_Store", "Thumbs.db",
            "node_modules", ".venv", "venv", "env",
            "__pycache__", "target", "dist", "build",
            "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock"
        ]
    }
}

@dataclass
class Config:
    """运行时配置对象"""
    project_root: Path
    output_format: str = "markdown"
    follow_symlinks: bool = False
    max_file_size_kb: int = 500
    use_gitignore: bool = True
    binary_extensions: List[str] = field(default_factory=list)
    always_exclude: List[str] = field(default_factory=list)
    # 策略相关
    active_strategy: str = "smart"  # smart, whitelist, blacklist, all
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], project_root: Path) -> 'Config':
        """从合并后的字典创建 Config 对象"""
        output = data.get("output", {})
        filters = data.get("filters", {})
        
        return cls(
            project_root=project_root,
            output_format=output.get("default_format", "markdown"),
            follow_symlinks=output.get("follow_symlinks", False),
            max_file_size_kb=output.get("max_file_size_kb", 500),
            use_gitignore=filters.get("use_gitignore", True),
            binary_extensions=filters.get("binary_extensions", []),
            always_exclude=filters.get("always_exclude", [])
        )

class ConfigManager:
    def __init__(self, start_path: Path = Path("."), force_project_root: Optional[Path] = None):
        self.start_path = start_path.resolve()
        # 如果强制指定了项目根目录，使用它；否则自动定位
        if force_project_root:
            self.project_root = force_project_root.resolve()
        else:
            from context1.utils.fs import get_project_root
            self.project_root = get_project_root(self.start_path)
        self.ctx_dir = self.project_root / ".context1"

    def _load_json(self, path: Path) -> Dict:
        if path.exists() and path.is_file():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {} # 加载失败降级为空
        return {}

    def _deep_merge(self, base: Dict, update: Dict) -> Dict:
        """简单的深度合并 (字典递归，列表覆盖)"""
        result = base.copy()
        for k, v in update.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = self._deep_merge(result[k], v)
            else:
                result[k] = v
        return result

    def load(self, cli_strategy: Optional[str] = None) -> Config:
        """
        加载并合并所有配置
        Priority: Default < User Global < Project Local
        """
        # 1. 默认配置
        final_data = DEFAULT_CONFIG.copy()

        # 2. 用户全局配置 (~/.config/context1/config.json)
        user_config_path = Path.home() / ".config" / "context1" / "config.json"
        user_data = self._load_json(user_config_path)
        final_data = self._deep_merge(final_data, user_data)

        # 3. 项目级配置 (.context1/config.json)
        project_config_path = self.ctx_dir / "config.json"
        project_data = self._load_json(project_config_path)
        final_data = self._deep_merge(final_data, project_data)

        # 创建对象
        config = Config.from_dict(final_data, self.project_root)
        
        # 策略覆盖：CLI 参数 > 配置文件
        if cli_strategy:
            config.active_strategy = cli_strategy
        
        return config

# 便捷入口
def load_config(strategy: Optional[str] = None, force_project_root: Optional[Path] = None) -> Config:
    return ConfigManager(force_project_root=force_project_root).load(strategy)