"""
src/context1/cli.py
CLI 主入口 - 职责：命令路由、参数解析、UI反馈
"""
import typer
from pathlib import Path
from typing import Optional
from rich.console import Console

# 导入 Core 模块
from context1.core.config import load_config, OutputFormat
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
    sort: str = typer.Option("name", "--sort", help="排序策略: name/vscode/dslpp"),
    format: str = typer.Option("markdown", "--format", help="输出格式: markdown/python-bundle"),
    clipboard: bool = typer.Option(False, "--clipboard", "-c", help="复制到剪贴板"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="显示详细日志")
):
    """
    将项目代码打包为单一文本上下文。
    """
    # 1. 初始化配置
    try:
        # 如果指定了源路径，使用它作为项目根目录；否则使用当前目录
        force_project_root = source.resolve() if source != Path(".") else None
        config = load_config(strategy=strategy, force_project_root=force_project_root)
        
        # 设置新的配置选项
        config.sort_strategy = sort
        config.output_format = format
        
        # 更新对应的枚举属性
        try:
            config.output_format_enum = OutputFormat(format)
        except ValueError:
            # 如果格式无效，使用默认值
            config.output_format_enum = OutputFormat.MARKDOWN
        
        # 如果未指定 output，默认为 {dir_name}.ctx1.md 或 .py
        if not output and not clipboard:
            if format == "python-bundle":
                output = Path(f"{source.resolve().name}.ctx1.py")
            else:
                output = Path(f"{source.resolve().name}.ctx1.md")
            
        if verbose:
            console.log(f"🔍 Loaded Config: Strategy={config.active_strategy}, Sort={sort}, Format={format}, Project Root={config.project_root}")
            
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
    
    # 计算统计信息
    total_size = sum(f.stat().st_size for f in files)
    total_chars = sum(f.read_text(encoding='utf-8', errors='replace').__len__() for f in files)
    estimated_tokens = total_chars // 4  # 粗略估算：1 token ≈ 4 characters
    
    # 显示统计信息
    console.print(f"\n[bold cyan]📊 Pack Statistics:[/bold cyan]")
    console.print(f"   📁 Total files: {len(files)}")
    console.print(f"   📏 Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    console.print(f"   🔤 Total characters: {total_chars:,}")
    console.print(f"   🎯 Estimated tokens: {estimated_tokens:,}")
    console.print(f"   📂 Strategy: {config.active_strategy}")
    
    # 3. 生成内容
    content = generate_content(files, config)

    # 4. 输出
    if clipboard:
        import pyperclip
        pyperclip.copy(content)
        console.print(f"\n[bold green]✅ Content copied to clipboard![/bold green]")
    
    if output:
        # 写入时自动忽略自己 (虽然 walker layer 1 应该已经排除了)
        output.write_text(content, encoding='utf-8')
        console.print(f"\n[bold green]✅ Packed content saved to: {output}[/bold green]")
        console.print(f"   📄 Output size: {len(content)} characters")
        console.print(f"   💾 File size: {output.stat().st_size:,} bytes ({output.stat().st_size/1024:.1f} KB)")

# --- 子命令: Unpack ---
@app.command()
def unpack(
    file: Path = typer.Argument(..., help="聚合文档路径", exists=True),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="目标还原目录"),
    force: bool = typer.Option(False, "--force", "-f", help="强制覆盖已存在的文件"),
    tree: Optional[Path] = typer.Option(None, "--tree", help="重构结构树路径 (.tree)"),
    dry_run: bool = typer.Option(False, "--dry-run", help="仅预览操作，不写入磁盘"),
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
    
    # 检查是否为重构模式
    if tree:
        console.print(f"🌳 Refactor mode using tree: [bold]{tree}[/bold]")
    
    # 执行解包
    stats = unpack_project(
        file,
        output,
        force=force,
        tree_path=tree,
        dry_run=dry_run
    )
    
    # 显示结果
    if dry_run:
        console.print("\n[bold yellow]🔍 Dry Run Results:[/bold yellow]")
        console.print(f"🎯 Match: {stats.get('match', 0)} files")
        console.print(f"🏗️  Scaffold: {stats.get('scaffold', 0)} files")
        console.print(f"⚠️  Conflict: {stats.get('conflict', 0)} files")
        console.print(f"❌ Failed: {stats.get('failed', 0)} files")
    else:
        if tree:
            console.print("\n[bold green]✅ Refactor completed![/bold green]")
            console.print(f"🎯 Match: {stats.get('match', 0)} files")
            console.print(f"🏗️  Scaffold: {stats.get('scaffold', 0)} files")
            console.print(f"⚠️  Conflict: {stats.get('conflict', 0)} files")
        else:
            console.print(f"[green]✅ Success: {stats.get('success', 0)}[/green], "
                         f"[yellow]⏭️  Skipped: {stats.get('skipped', 0)}[/yellow], "
                         f"[red]❌ Failed: {stats.get('failed', 0)}[/red]")

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
        # 如果指定了源路径，使用它作为项目根目录；否则使用当前目录
        force_project_root = source.resolve() if source != Path(".") else None
        config = load_config(strategy=strategy, force_project_root=force_project_root)
        
        if verbose:
            console.log(f"🔍 Loaded Config: Strategy={config.active_strategy}, Project Root={config.project_root}")
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

