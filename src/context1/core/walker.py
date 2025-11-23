"""
src/context1/core/walker.py
文件扫描器 - 核心职责：目录遍历、Gitignore集成、策略过滤
[修正版] 修复了 Any 引用丢失、支持 glob 排除模式、优化了 JSON 错误处理
"""
import os
import json
import fnmatch
from pathlib import Path
from typing import List, Set, Optional, Dict, Any
import pathspec

from context1.core.config import Config
from context1.utils.fs import is_binary_file

class FileWalker:
    def __init__(self, config: Config, ignore_strategy: bool = False):
        self.config = config
        self.root = config.project_root
        self.ignore_strategy = ignore_strategy
        
        # 初始化 Layer 1: 基础过滤 (Gitignore + Always Exclude)
        self.gitignore_spec = self._load_gitignore()
        
        # 初始化 Layer 2: 策略过滤 (White/Black/Detailed)
        self.strategy_spec = None
        if not ignore_strategy:
            self.strategy_spec = self._load_strategy_spec()

    def _load_gitignore(self) -> Optional[pathspec.PathSpec]:
        """加载根目录的 .gitignore"""
        if not self.config.use_gitignore:
            return None
        
        gitignore_path = self.root / ".gitignore"
        if gitignore_path.exists():
            try:
                with open(gitignore_path, "r", encoding="utf-8") as f:
                    return pathspec.PathSpec.from_lines("gitwildmatch", f)
            except Exception:
                pass 
        return None

    def _load_strategy_spec(self) -> Dict[str, Any]:
        """加载策略文件"""
        ctx_dir = self.root / ".context1"
        
        # Whitelist
        whitelist_path = ctx_dir / "whitelist.json"
        if whitelist_path.exists():
            return {"type": "whitelist", "patterns": self._load_json_list(whitelist_path)}
            
        # Blacklist
        blacklist_path = ctx_dir / "blacklist.json"
        if blacklist_path.exists():
            return {"type": "blacklist", "patterns": self._load_json_list(blacklist_path)}
            
        # Smart/Default
        return {"type": "smart", "patterns": []}

    def _load_json_list(self, path: Path) -> List[str]:
        """安全加载 JSON 列表"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list): return data
                return data.get("patterns", [])
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"[Warning] 配置文件格式错误，已跳过: {path} ({e})")
            return []
        except Exception:
            return []

    def _match_patterns(self, rel_path: str, patterns: List[str]) -> bool:
        if not patterns: return False
        spec = pathspec.PathSpec.from_lines("gitwildmatch", patterns)
        return spec.match_file(rel_path)

    def scan(self) -> List[Path]:
        """执行扫描"""
        collected_files = []
        
        for root, dirs, files in os.walk(self.root):
            # 递归剪枝：原地修改 dirs
            dirs[:] = [d for d in dirs if self._should_visit_dir(Path(root) / d)]
            
            for filename in files:
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(self.root)
                rel_path_str = str(rel_path.as_posix())
                
                if self._should_include_file(file_path, rel_path_str):
                    collected_files.append(file_path)
                    
        return collected_files

    def _should_visit_dir(self, dir_path: Path) -> bool:
        """Layer 1: 检查目录是否应该进入"""
        rel_path = dir_path.relative_to(self.root).as_posix()
        name = dir_path.name
        
        # 1. 基础排除 (Always Exclude) - 支持 fnmatch
        for pattern in self.config.always_exclude:
            if fnmatch.fnmatch(name, pattern):
                return False
                
        # 隐藏目录
        if name.startswith(".") and name != ".":
            return False
            
        # 2. Gitignore
        if self.gitignore_spec and self.gitignore_spec.match_file(rel_path):
            return False
            
        return True

    def _should_include_file(self, file_path: Path, rel_path: str) -> bool:
        """双层过滤判断"""
        name = file_path.name
        
        # --- Layer 1: Base Filter ---
        
        # 1. 扩展名黑名单
        if file_path.suffix.lower() in self.config.binary_extensions:
            return False
            
        # 2. 基础排除 (Always Exclude) - 支持 fnmatch
        for pattern in self.config.always_exclude:
            if fnmatch.fnmatch(name, pattern):
                return False
            
        # 3. Gitignore
        if self.gitignore_spec and self.gitignore_spec.match_file(rel_path):
            return False
            
        # 4. 二进制内容检测
        if is_binary_file(file_path):
            return False

        # --- Layer 2: Strategy Filter ---
        if self.ignore_strategy:
            return True
            
        st_type = self.strategy_spec["type"]
        patterns = self.strategy_spec["patterns"]
        
        if st_type == "whitelist":
            return self._match_patterns(rel_path, patterns)
        elif st_type == "blacklist":
            if self._match_patterns(rel_path, patterns):
                return False
            return True
        elif st_type == "smart":
            return True
            
        return True