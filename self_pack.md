# Context1 Pack Result
Generated at: 2025-11-23T22:22:58.186496
Strategy: smart
Files: 12

# Project Structure
.
│   ├── .gitignore
│   ├── .python-version
│   ├── README.md
│   ├── ctx1
│   ├── pyproject.toml
└── uv.lock


--- 文件: .gitignore ---
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv



--- 文件: .python-version ---
3.12



--- 文件: ctx1 ---
#!/usr/bin/env python3
"""
Context1 CLI entry point
"""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run the CLI app
from context1.cli import app

if __name__ == "__main__":
    app()


--- 文件: pyproject.toml ---
[project]
name = "context1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "pathspec>=0.12.1",
    "pyperclip>=1.11.0",
    "rich>=14.2.0",
    "typer[all]>=0.20.0",
]

[project.scripts]
context1 = "context1.cli:app"



--- 文件: README.md ---



--- 文件: src/context1/cli.py ---
"""
src/context1/cli.py
CLI 主入口 - 职责：命令路由、参数解析、UI反馈
"""
import typer
from pathlib import Path
from typing import Optional
from rich.console import Console

# 导入 Core 模块
from context1.core.config import load_config
from context1.core.walker import FileWalker
from context1.core.packer import generate_content
from context1.core.unpacker import unpack_project

app = typer.Typer(
    name="ctx1",
    help="Context1: The bridge between your codebase and LLMs.",
    add_completion=False
)
console = Console()

# --- 子命令: Pack ---
@app.command()
def pack(
    source: Path = typer.Argument(".", help="源目录路径", exists=True),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="输出文件路径"),
    strategy: str = typer.Option("smart", "--strategy", "-s", help="过滤策略: smart/whitelist/blacklist"),
    clipboard: bool = typer.Option(False, "--clipboard", "-c", help="复制到剪贴板"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="显示详细日志")
):
    """
    将项目代码打包为单一文本上下文。
    """
    # 1. 初始化配置
    try:
        config = load_config(strategy=strategy)
        # 如果未指定 output，默认为 {dir_name}.ctx1.md
        if not output and not clipboard:
            output = Path(f"{source.resolve().name}.ctx1.md")
            
        if verbose:
            console.log(f"🔍 Loaded Config: Strategy={config.active_strategy}")
            
    except Exception as e:
        console.print(f"[red]Config Error:[/red] {e}")
        raise typer.Exit(1)

    # 2. 扫描文件
    walker = FileWalker(config)
    with console.status("[bold green]Scanning files..."):
        files = walker.scan()
    
    if not files:
        console.print("[yellow]⚠️  No files found matching the criteria.[/yellow]")
        raise typer.Exit()

    console.print(f"📄 Found {len(files)} files.")

    # 3. 生成内容
    content = generate_content(files, config)

    # 4. 输出
    if clipboard:
        import pyperclip
        pyperclip.copy(content)
        console.print("[bold green]✅ Copied to clipboard![/bold green]")
    
    if output:
        # 写入时自动忽略自己 (虽然 walker layer 1 应该已经排除了)
        output.write_text(content, encoding='utf-8')
        console.print(f"[bold green]✅ Saved to {output}[/bold green]")

# --- 子命令: Unpack ---
@app.command()
def unpack(
    file: Path = typer.Argument(..., help="聚合文档路径", exists=True),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="目标还原目录"),
    force: bool = typer.Option(False, "--force", "-f", help="强制覆盖已存在的文件"),
):
    """
    将聚合文档还原为项目结构。
    """
    # 默认目录逻辑
    if not output:
        # context.ctx1.md -> context.ctx1/
        # context.md -> context.ctx1/
        dir_name = file.name.replace('.md', '')
        if not dir_name.endswith('.ctx1'):
            dir_name += '.ctx1'
        output = file.parent / dir_name
        
    console.print(f"📂 Unpacking to: [bold]{output}[/bold]")
    
    stats = unpack_project(file, output, force=force)
    
    console.print(f"[green]Success: {stats['success']}[/green], "
                  f"[yellow]Skipped: {stats['skipped']}[/yellow], "
                  f"[red]Failed: {stats['failed']}[/red]")

# --- 子命令: Config & Stats ---
@app.command()
def config(
    action: str = typer.Argument(..., help="操作: init/list"),
    path: Optional[Path] = typer.Option(None, "--path", "-p", help="配置文件路径")
):
    """管理配置文件 (Init/List)"""
    from context1.core.config import ConfigManager
    import json
    
    config_manager = ConfigManager()
    
    if action == "init":
        # 创建默认配置文件
        if path:
            config_path = path
        else:
            config_path = config_manager.config_dir / "config.json"
        
        # 确保配置目录存在
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 创建默认配置
        default_config = {
            "output": {
                "default_format": "markdown",
                "follow_symlinks": False,
                "max_file_size_kb": 500
            },
            "filters": {
                "use_gitignore": True,
                "binary_extensions": [
                    ".exe", ".dll", ".so", ".dylib", ".bin", ".pkl",
                    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
                    ".zip", ".tar", ".gz", ".7z", ".rar", ".pdf",
                    ".pyc", ".pyo", ".pyd", ".class"
                ],
                "always_exclude": [
                    ".git", ".svn", ".hg", ".idea", ".vscode",
                    ".DS_Store", "Thumbs.db",
                    "node_modules", ".venv", "venv", "env",
                    "__pycache__", "target", "dist", "build",
                    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock"
                ]
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        
        console.print(f"[bold green]✅ Created default config at: {config_path}[/bold green]")
        
    elif action == "list":
        # 显示当前配置
        try:
            config = config_manager.load()
            console.print("[bold blue]Current Configuration:[/bold blue]")
            console.print(f"  Project Root: {config.project_root}")
            console.print(f"  Output Format: {config.output_format}")
            console.print(f"  Max File Size: {config.max_file_size_kb}KB")
            console.print(f"  Use Gitignore: {config.use_gitignore}")
            console.print(f"  Active Strategy: {config.active_strategy}")
            console.print(f"  Binary Extensions: {len(config.binary_extensions)} types")
            console.print(f"  Always Exclude: {len(config.always_exclude)} patterns")
        except Exception as e:
            console.print(f"[red]Error loading config: {e}[/red]")
            raise typer.Exit(1)
            
    else:
        console.print(f"[red]Unknown action: {action}[/red]")
        console.print("Available actions: init, list")
        raise typer.Exit(1)

@app.command()
def stats(
    source: Path = typer.Argument(".", help="源目录路径", exists=True),
    strategy: str = typer.Option("smart", "--strategy", "-s", help="过滤策略: smart/whitelist/blacklist"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="显示详细日志")
):
    """显示项目统计信息与 Token 估算"""
    from rich.table import Table
    from rich.panel import Panel
    
    # 1. 初始化配置
    try:
        config = load_config(strategy=strategy)
        if verbose:
            console.log(f"🔍 Loaded Config: Strategy={config.active_strategy}")
    except Exception as e:
        console.print(f"[red]Config Error:[/red] {e}")
        raise typer.Exit(1)
    
    # 2. 扫描文件
    walker = FileWalker(config)
    with console.status("[bold green]Scanning files for stats..."):
        files = walker.scan()
    
    if not files:
        console.print("[yellow]⚠️  No files found matching the criteria.[/yellow]")
        raise typer.Exit()
    
    # 3. 计算统计信息
    total_files = len(files)
    total_size = 0
    total_chars = 0
    
    file_extensions = {}
    
    for file_path in files:
        try:
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            total_size += file_size
            
            # 读取文件内容计算字符数
            try:
                content = file_path.read_text(encoding='utf-8', errors='replace')
                total_chars += len(content)
                
                # 统计文件扩展名
                ext = file_path.suffix.lower() or '(no extension)'
                file_extensions[ext] = file_extensions.get(ext, 0) + 1
                
            except Exception:
                # 如果无法读取文件，跳过字符统计
                pass
                
        except Exception:
            # 如果无法获取文件信息，跳过
            pass
    
    # 4. 显示结果
    table = Table(title="Project Statistics")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    # 基础统计
    table.add_row("Total Files", str(total_files))
    table.add_row("Total Size", f"{total_size / 1024 / 1024:.2f} MB")
    table.add_row("Estimated Tokens", f"{total_chars // 4:,}")
    
    # 文件扩展名统计（前10个）
    if file_extensions:
        sorted_extensions = sorted(file_extensions.items(), key=lambda x: x[1], reverse=True)[:10]
        ext_summary = ", ".join([f"{ext} ({count})" for ext, count in sorted_extensions])
        table.add_row("Top Extensions", ext_summary)
    
    console.print(table)
    
    # 5. 详细信息面板
    if verbose:
        details_panel = Panel(
            f"Strategy: {config.active_strategy}\n"
            f"Project Root: {config.project_root}\n"
            f"Max File Size: {config.max_file_size_kb}KB\n"
            f"Use Gitignore: {config.use_gitignore}",
            title="Configuration Details",
            border_style="blue"
        )
        console.print(details_panel)

if __name__ == "__main__":
    app()


--- 文件: src/context1/core/config.py ---
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
    def __init__(self, start_path: Path = Path(".")):
        self.start_path = start_path.resolve()
        # 自动定位项目根目录（寻找 .context1）
        from context1.utils.fs import get_project_root
        self.project_root = get_project_root(self.start_path)
        self.config_dir = self.project_root / ".context1"

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
        project_config_path = self.config_dir / "config.json"
        project_data = self._load_json(project_config_path)
        final_data = self._deep_merge(final_data, project_data)

        # 创建对象
        config = Config.from_dict(final_data, self.project_root)
        
        # 策略覆盖：CLI 参数 > 配置文件
        if cli_strategy:
            config.active_strategy = cli_strategy
        
        return config

# 便捷入口
def load_config(strategy: Optional[str] = None) -> Config:
    return ConfigManager().load(strategy)


--- 文件: src/context1/core/packer.py ---
"""
src/context1/core/packer.py
打包器 - 核心职责：生成目录树、文件排序、格式化输出(Markdown/XML)
[修正版] 增加了内存溢出保护 (Pre-read size check)
"""
from pathlib import Path
from typing import List
from datetime import datetime
from context1.core.config import Config

def vscode_sort_key(file_path: Path) -> List[str]:
    """
    【核心特色】VSCode 风格自然排序
    """
    parts = file_path.parts
    sort_parts = []
    
    for i, part in enumerate(parts):
        # 简单模拟：点开头优先级最高(0)，其他(1)
        priority = 0 if part.startswith('.') else 1
        sort_parts.append((priority, part.lower()))
    
    return sort_parts

def generate_tree(files: List[Path], root: Path) -> str:
    """生成 ASCII 目录树结构 (类似 Linux tree 命令)"""
    tree_lines = ["# Project Structure"]
    tree_lines.append(".")
    
    # 按目录分组文件
    dir_files = {}
    for file_path in files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        if dir_path not in dir_files:
            dir_files[dir_path] = []
        dir_files[dir_path].append(rel_path)
    
    # 生成目录树
    def build_tree_display(path: Path, prefix: str = "", is_last: bool = True) -> List[str]:
        lines = []
        name = path.name if path != Path(".") else "."
        lines.append(f"{prefix}{'└── ' if is_last else '├── '}{name}")
        
        if path in dir_files:
            children = sorted(dir_files[path], key=lambda x: (x.is_file(), x.name))
            for i, child in enumerate(children):
                child_prefix = prefix + ("    " if is_last else "│   ")
                is_last_child = i == len(children) - 1
                if child.is_file():
                    lines.append(f"{child_prefix}{'└── ' if is_last_child else '├── '}{child.name}")
                else:
                    lines.extend(build_tree_display(child, child_prefix, is_last_child))
        
        return lines
    
    # 从根目录开始构建
    root_files = [f for f in files if f.parent == root]
    root_dirs = [d for d in dir_files.keys() if d != Path(".") and d.parent == root]
    
    # 先显示根目录文件
    for i, file_path in enumerate(sorted(root_files, key=lambda x: x.name)):
        is_last = i == len(root_files) - 1 and len(root_dirs) == 0
        prefix = "" if is_last else "│   "
        lines = build_tree_display(file_path.relative_to(root), prefix, is_last)
        tree_lines.extend(lines)
    
    # 再显示根目录
    for i, dir_path in enumerate(sorted(root_dirs, key=lambda x: x.name)):
        is_last = i == len(root_dirs) - 1
        prefix = "" if is_last else "│   "
        lines = build_tree_display(dir_path, prefix, is_last)
        tree_lines.extend(lines)
    
    return "\n".join(tree_lines)

def generate_content(files: List[Path], config: Config, tree_view: bool = True) -> str:
    """主入口：生成聚合文档内容"""
    root = config.project_root
    
    # 1. 排序
    files_sorted = sorted(files, key=lambda f: vscode_sort_key(f.relative_to(root)))
    
    output = []
    
    # 2. Header & Metadata
    output.append(f"# Context1 Pack Result")
    output.append(f"Generated at: {datetime.now().isoformat()}")
    output.append(f"Strategy: {config.active_strategy}")
    output.append(f"Files: {len(files_sorted)}\n")
    
    # 3. Directory Tree
    if tree_view:
        output.append(generate_tree(files_sorted, root))
        output.append("\n")
        
    # 4. File Contents
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root).as_posix()
        
        try:
            # [FIX] 内存安全检查：先看大小，再读文件
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            
            if file_size > config.max_file_size_kb * 1024:
                content = f"<!-- File skipped: size ({file_size} bytes) > {config.max_file_size_kb}KB -->"
            else:
                content = file_path.read_text(encoding='utf-8', errors='replace')
            
            if config.output_format == "xml":
                # XML Format
                output.append(f'<document path="{rel_path}">')
                output.append(content)
                output.append('</document>\n')
            else:
                # Markdown Format
                output.append(f"--- 文件: {rel_path} ---")
                output.append(content)
                output.append("\n")
                
        except Exception as e:
            output.append(f"<!-- Error reading {rel_path}: {str(e)} -->\n")
            
    if config.output_format == "xml":
        return "<documents>\n" + "\n".join(output) + "\n</documents>"
        
    return "\n".join(output)


--- 文件: src/context1/core/unpacker.py ---
"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版] 修复了 Python 缩进错误，优化了 strip 逻辑以保护数据完整性
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple
from context1.utils.fs import safe_write_file

MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    """
    解析文档内容，返回文件列表
    """
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    
    for line in lines:
        # Markdown Header Match
        md_match = MD_PATTERN.match(line)
        if md_match:
            if current_file:
                files.append({
                    'path': current_file,
                    # [FIX] 不移除行首缩进，仅移除尾部多余换行
                    'content': '\n'.join(current_content) 
                })
            current_file = md_match.group(1).strip()
            current_content = []
            continue
            
        # XML Header Match
        xml_match = XML_PATTERN.match(line)
        if xml_match:
            # [FIX] 缩进已修复，与上一层 if 对齐
            if current_file:
                files.append({
                    'path': current_file,
                    'content': '\n'.join(current_content)
                })
            current_file = xml_match.group(1).strip()
            current_content = []
            continue
             
        # Content Collection
        if current_file:
            if line.strip() == '</document>':
                continue
            current_content.append(line)
            
    # Save last file
    if current_file:
        files.append({
            'path': current_file,
            'content': '\n'.join(current_content)
        })
        
    return files

def unpack_project(
    source_file: Path, 
    output_dir: Path, 
    force: bool = False,
    structure_only: bool = False
) -> Dict[str, int]:
    """
    执行还原操作
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    content = source_file.read_text(encoding='utf-8')
    files = parse_document(content)
    
    stats = {"success": 0, "skipped": 0, "failed": 0}
    
    for file_data in files:
        rel_path = file_data['path']
        file_content = file_data['content']
        
        try:
            if structure_only:
                file_content = ""
            
            written = safe_write_file(output_dir, rel_path, file_content, force=force)
            
            if written:
                stats["success"] += 1
            else:
                stats["skipped"] += 1
                
        except Exception as e:
            print(f"❌ Error unpacking {rel_path}: {e}")
            stats["failed"] += 1
            
    return stats


--- 文件: src/context1/core/walker.py ---
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


--- 文件: src/context1/utils/fs.py ---
"""
src/context1/utils/fs.py
文件系统操作工具集 - 核心职责：路径安全检查、二进制检测、文件读写封装
[修正版] 已修复 Zip Slip 漏洞，使用 os.path.commonpath
"""
import os
from pathlib import Path
from typing import Union

def is_safe_path(base_dir: Union[str, Path], target_path: Union[str, Path]) -> bool:
    """
    【核心安全逻辑】Zip Slip 防护
    使用 os.path.commonpath 确保 target 在 base 目录下
    """
    try:
        base = Path(base_dir).resolve()
        # 允许 target_path 是绝对路径或相对路径
        if os.path.isabs(target_path):
            target = Path(target_path).resolve()
        else:
            target = (base / target_path).resolve()
            
        # 真正的安全检查：比较公共路径是否等于 base
        # 这种方式比 startswith 更可靠，能处理 /var/lib vs /var/lib2 的情况
        return os.path.commonpath([base, target]) == str(base)
    except Exception:
        return False

def is_binary_file(file_path: Path, chunk_size: int = 1024) -> bool:
    """
    通过读取前 chunk_size 字节检查是否包含 NULL 字节来判断是否为二进制文件
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
            return b'\x00' in chunk
    except IOError:
        return False

def get_project_root(start_path: Path = Path(".")) -> Path:
    """
    向上递归查找包含 .context1/ 的目录，如果找不到则返回 start_path
    """
    current = start_path.resolve()
    for parent in [current, *current.parents]:
        if (parent / ".context1").is_dir():
            return parent
    return current

def safe_write_file(base_dir: Path, rel_path: str, content: str, force: bool = False) -> bool:
    """
    安全写入文件
    """
    if not is_safe_path(base_dir, rel_path):
        raise ValueError(f"Unsafe path detected: {rel_path}")
    
    target_file = (base_dir / rel_path).resolve()
    
    # 检查文件是否存在
    if target_file.exists() and not force:
        return False
    
    # 自动创建父目录
    target_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True


--- 文件: uv.lock ---
version = 1
revision = 2
requires-python = ">=3.12"

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "context1"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "pathspec" },
    { name = "pyperclip" },
    { name = "rich" },
    { name = "typer" },
]

[package.metadata]
requires-dist = [
    { name = "pathspec", specifier = ">=0.12.1" },
    { name = "pyperclip", specifier = ">=1.11.0" },
    { name = "rich", specifier = ">=14.2.0" },
    { name = "typer", extras = ["all"], specifier = ">=0.20.0" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "pathspec"
version = "0.12.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ca/bc/f35b8446f4531a7cb215605d100cd88b7ac6f44ab3fc94870c120ab3adbf/pathspec-0.12.1.tar.gz", hash = "sha256:a482d51503a1ab33b1c67a6c3813a26953dbdc71c31dacaef9a838c4e29f5712", size = 51043, upload-time = "2023-12-10T22:30:45Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/20/ff623b09d963f88bfde16306a54e12ee5ea43e9b597108672ff3a408aad6/pathspec-0.12.1-py3-none-any.whl", hash = "sha256:a0d503e138a4c123b27490a4f7beda6a01c6f288df0e4a8b79c7eb0dc7b4cc08", size = 31191, upload-time = "2023-12-10T22:30:43.14Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pyperclip"
version = "1.11.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e8/52/d87eba7cb129b81563019d1679026e7a112ef76855d6159d24754dbd2a51/pyperclip-1.11.0.tar.gz", hash = "sha256:244035963e4428530d9e3a6101a1ef97209c6825edab1567beac148ccc1db1b6", size = 12185, upload-time = "2025-09-26T14:40:37.245Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/df/80/fc9d01d5ed37ba4c42ca2b55b4339ae6e200b456be3a1aaddf4a9fa99b8c/pyperclip-1.11.0-py3-none-any.whl", hash = "sha256:299403e9ff44581cb9ba2ffeed69c7aa96a008622ad0c46cb575ca75b5b84273", size = 11063, upload-time = "2025-09-26T14:40:36.069Z" },
]

[[package]]
name = "rich"
version = "14.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fb/d2/8920e102050a0de7bfabeb4c4614a49248cf8d5d7a8d01885fbb24dc767a/rich-14.2.0.tar.gz", hash = "sha256:73ff50c7c0c1c77c8243079283f4edb376f0f6442433aecb8ce7e6d0b92d1fe4", size = 219990, upload-time = "2025-10-09T14:16:53.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/25/7a/b0178788f8dc6cafce37a212c99565fa1fe7872c70c6c9c1e1a372d9d88f/rich-14.2.0-py3-none-any.whl", hash = "sha256:76bc51fe2e57d2b1be1f96c524b890b816e334ab4c1e45888799bfaab0021edd", size = 243393, upload-time = "2025-10-09T14:16:51.245Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "typer"
version = "0.20.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8f/28/7c85c8032b91dbe79725b6f17d2fffc595dff06a35c7a30a37bef73a1ab4/typer-0.20.0.tar.gz", hash = "sha256:1aaf6494031793e4876fb0bacfa6a912b551cf43c1e63c800df8b1a866720c37", size = 106492, upload-time = "2025-10-20T17:03:49.445Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/64/7713ffe4b5983314e9d436a90d5bd4f63b6054e2aca783a3cfc44cb95bbf/typer-0.20.0-py3-none-any.whl", hash = "sha256:5b463df6793ec1dca6213a3cf4c0f03bc6e322ac5e16e13ddd622a889489784a", size = 47028, upload-time = "2025-10-20T17:03:47.617Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]


