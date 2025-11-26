"""
src/context1/core/config.py
配置管理核心 - 职责：加载三级配置、合并规则、提供全局配置单例
"""
import json
import os
from enum import Enum
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

# ==========================================
# 👇 1. 先定义枚举和常量 (必须放在最前面！)
# ==========================================

# --- 枚举定义 ---
class OutputFormat(Enum):
    """输出格式枚举"""
    MARKDOWN = "markdown"
    PYTHON_BUNDLE = "python-bundle"

class SortStrategy(Enum):
    """排序策略枚举"""
    NAME = "name"
    VSCODE = "vscode"
    DSLPP = "dslpp"

# --- DS-LPP 权重配置常量 ---
DEFAULT_DSLPP_WEIGHTS = [
    {"pattern": "__init__.py", "weight": 0},
    {"pattern": "*_ent.py", "weight": 10}, {"pattern": "*_d.py", "weight": 10},
    {"pattern": "*_i.py", "weight": 10},   {"pattern": "*_c.py", "weight": 10},
    {"pattern": "*_bhv.py", "weight": 20}, {"pattern": "*_u.py", "weight": 20},
    {"pattern": "*_stg.py", "weight": 30}, {"pattern": "*_s.py", "weight": 30},
    {"pattern": "*_cmd.py", "weight": 40},
    {"pattern": "test_*.py", "weight": 99}
]

# ==========================================
# 👇 2. 然后再定义 DEFAULT_CONFIG (因为它引用了上面的常量)
# ==========================================

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
    },
    "sort": {
        "strategy": "name",
        # ✅ 现在这里可以正确引用了，因为上面已经定义了
        "dslpp_weights": DEFAULT_DSLPP_WEIGHTS
    }
}

# ==========================================
# 👇 3. 最后定义类和逻辑
# ==========================================

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
    # 新增字段：输出格式和排序策略
    output_format_enum: OutputFormat = OutputFormat.MARKDOWN
    sort_strategy: SortStrategy = SortStrategy.NAME
    dslpp_weights: List[Dict[str, Any]] = field(default_factory=lambda: DEFAULT_DSLPP_WEIGHTS.copy())
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], project_root: Path) -> 'Config':
        """从合并后的字典创建 Config 对象"""
        output = data.get("output", {})
        filters = data.get("filters", {})
        sort_config = data.get("sort", {})
        
        # 处理输出格式枚举
        output_format_str = output.get("default_format", "markdown")
        try:
            output_format_enum = OutputFormat(output_format_str)
        except ValueError:
            output_format_enum = OutputFormat.MARKDOWN
        
        # 处理排序策略枚举
        sort_strategy_str = sort_config.get("strategy", "name")
        try:
            sort_strategy = SortStrategy(sort_strategy_str)
        except ValueError:
            sort_strategy = SortStrategy.NAME
        
        # 处理 DSLPP 权重配置
        dslpp_weights = sort_config.get("dslpp_weights", DEFAULT_DSLPP_WEIGHTS)
        
        return cls(
            project_root=project_root,
            output_format=output_format_str,
            output_format_enum=output_format_enum,
            follow_symlinks=output.get("follow_symlinks", False),
            max_file_size_kb=output.get("max_file_size_kb", 500),
            use_gitignore=filters.get("use_gitignore", True),
            binary_extensions=filters.get("binary_extensions", []),
            always_exclude=filters.get("always_exclude", []),
            sort_strategy=sort_strategy,
            dslpp_weights=dslpp_weights
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