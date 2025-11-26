#!/usr/bin/env python3
# CTX1_BUNDLE_VERSION: 0.2.0
# ================= Architecture Map =================
# test_dslpp\__init__.py [Foundation]: 包初始化和基础配置
# test_dslpp\test_user.py [Test]: 用户模块测试
# test_dslpp\user_bhv.py [Behavior]: 用户行为逻辑
# test_dslpp\user_c.py [Controller]: 用户控制器逻辑
# test_dslpp\user_cmd.py [Commander]: 用户命令处理
# test_dslpp\user_d.py [Data]: 用户数据访问逻辑
# test_dslpp\user_ent.py [Entity]: 用户数据实体定义
# test_dslpp\user_i.py [Interface]: 用户服务接口定义
# test_dslpp\user_s.py [Service]: 用户服务实现
# test_dslpp\user_stg.py [Strategy]: 用户策略定义
# test_dslpp\user_u.py [Utility]: 用户相关工具函数
# ====================================================

# <ctx1:file path=".gitignore">
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv

# </ctx1:file>

# <ctx1:file path=".python-version">
3.12

# </ctx1:file>

# <ctx1:file path="CHANGELOG.md">
# 更新日志

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

## [0.2.0] - 2025-11-26

### ✨ 新特性 (Features)
*   **[Core]** 引入 DS-LPP 拓扑排序算法，支持基于架构的智能文件排序。
*   **[Core]** 新增 Python Bundle 输出格式，生成的包本身就是合法的 Python 代码文件。
*   **[Core]** 实现元数据提取功能，自动识别 `@Role` 和 `@Responsibility` 注解。
*   **[Core]** 自动生成项目结构蓝图（layout.tree），支持重构模式。
*   **[Unpacker]** 实现智能内容池，解决重名文件问题。
*   **[Unpacker]** 支持基于结构树的智能重构模式。
*   **[CLI]** Pack 命令新增 `--sort` 参数，支持 name/vscode/dslpp 排序策略。
*   **[CLI]** Pack 命令新增 `--format` 参数，支持 markdown/python-bundle 输出格式。
*   **[CLI]** Unpack 命令新增 `--tree` 参数，支持重构模式。
*   **[CLI]** Unpack 命令新增 `--dry-run` 参数，支持试运行模式。

### 🐛 修复与优化 (Fixes & Refactoring)
*   **[Fix]** 修复了文档解析器，支持三种格式（Markdown/XML/Python Bundle）。
*   **[Fix]** 优化了空行处理，连续 3 行以上空行压缩为 2 行。
*   **[Fix]** 增强了路径安全性，防止 Zip Slip 攻击。
*   **[Doc]** 更新了项目文档，新增 v0.2.0 功能说明。

### 🏗️ 架构变更 (Architecture)
*   **[Config]** 扩展了配置系统，新增 `OutputFormat` 和 `SortStrategy` 枚举。
*   **[Config]** 新增 `dslpp_weights` 配置项，支持自定义排序权重。
*   **[Packer]** 重构了排序逻辑，支持多种排序策略。
*   **[Unpacker]** 实现了全新的智能重构引擎。

## [0.1.1] - 2025-11-24

### ✨ 新特性 (Features)
*   **[CLI]** 新增 `ctx1` 命令别名。
*   **[CLI]** `pack` 命令新增执行时的实时统计面板（Token 估算、文件大小）。
*   **[Core]** 支持读取和打包 UTF-16 编码的文件。
*   **[Core]** 无法解码的二进制文件现在会以 Hex 字符串形式保留在注释中，而不是报错或乱码。

### 🐛 修复与优化 (Fixes & Refactoring)
*   **[Fix]** 修复了 `is_binary_file` 将 UTF-16 文本误判为二进制文件的问题。
*   **[Fix]** 修复了当 `source` 目录不是当前目录时，配置文件加载路径错误的问题（实现了 `force_project_root`）。
*   **[Doc]** 补全了项目 `README.md` 文档。

## [0.1.0] - 2025-11-23

### 🎉 首次发布
*   **[CLI]** 实现基本的 `pack`、`stats`、`config` 命令
*   **[Core]** 实现文件扫描、过滤、打包核心功能
*   **[Security]** 实现 Zip Slip 攻击防护
*   **[Tests]** 实现完整的单元测试套件
# </ctx1:file>

# <ctx1:file path="context1.ctx1.md">
# Context1 Pack Result
Generated at: 2025-11-26T18:06:34.332156
Strategy: smart
Files: 30

# Project Structure
.
│   ├── .gitignore
│   ├── .python-version
│   ├── CHANGELOG.md
│   ├── LICENSE
│   ├── README.md
│   ├── ctx1
│   ├── pyproject.toml
│   ├── test_cli.py
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


--- 文件: CHANGELOG.md ---
# 更新日志

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

## [0.2.0] - 2025-11-26

### ✨ 新特性 (Features)
*   **[Core]** 引入 DS-LPP 拓扑排序算法，支持基于架构的智能文件排序。
*   **[Core]** 新增 Python Bundle 输出格式，生成的包本身就是合法的 Python 代码文件。
*   **[Core]** 实现元数据提取功能，自动识别 `@Role` 和 `@Responsibility` 注解。
*   **[Core]** 自动生成项目结构蓝图（layout.tree），支持重构模式。
*   **[Unpacker]** 实现智能内容池，解决重名文件问题。
*   **[Unpacker]** 支持基于结构树的智能重构模式。
*   **[CLI]** Pack 命令新增 `--sort` 参数，支持 name/vscode/dslpp 排序策略。
*   **[CLI]** Pack 命令新增 `--format` 参数，支持 markdown/python-bundle 输出格式。
*   **[CLI]** Unpack 命令新增 `--tree` 参数，支持重构模式。
*   **[CLI]** Unpack 命令新增 `--dry-run` 参数，支持试运行模式。

### 🐛 修复与优化 (Fixes & Refactoring)
*   **[Fix]** 修复了文档解析器，支持三种格式（Markdown/XML/Python Bundle）。
*   **[Fix]** 优化了空行处理，连续 3 行以上空行压缩为 2 行。
*   **[Fix]** 增强了路径安全性，防止 Zip Slip 攻击。
*   **[Doc]** 更新了项目文档，新增 v0.2.0 功能说明。

### 🏗️ 架构变更 (Architecture)
*   **[Config]** 扩展了配置系统，新增 `OutputFormat` 和 `SortStrategy` 枚举。
*   **[Config]** 新增 `dslpp_weights` 配置项，支持自定义排序权重。
*   **[Packer]** 重构了排序逻辑，支持多种排序策略。
*   **[Unpacker]** 实现了全新的智能重构引擎。

## [0.1.1] - 2025-11-24

### ✨ 新特性 (Features)
*   **[CLI]** 新增 `ctx1` 命令别名。
*   **[CLI]** `pack` 命令新增执行时的实时统计面板（Token 估算、文件大小）。
*   **[Core]** 支持读取和打包 UTF-16 编码的文件。
*   **[Core]** 无法解码的二进制文件现在会以 Hex 字符串形式保留在注释中，而不是报错或乱码。

### 🐛 修复与优化 (Fixes & Refactoring)
*   **[Fix]** 修复了 `is_binary_file` 将 UTF-16 文本误判为二进制文件的问题。
*   **[Fix]** 修复了当 `source` 目录不是当前目录时，配置文件加载路径错误的问题（实现了 `force_project_root`）。
*   **[Doc]** 补全了项目 `README.md` 文档。

## [0.1.0] - 2025-11-23

### 🎉 首次发布
*   **[CLI]** 实现基本的 `pack`、`stats`、`config` 命令
*   **[Core]** 实现文件扫描、过滤、打包核心功能
*   **[Security]** 实现 Zip Slip 攻击防护
*   **[Tests]** 实现完整的单元测试套件


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


--- 文件: LICENSE ---
MIT License

Copyright (c) 2025 Context1 Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


--- 文件: pyproject.toml ---
[project]
name = "context1"
version = "0.2.0"
description = "在您的代码库和 LLM 之间架设桥梁的强大 CLI 工具"
readme = "README.md"
requires-python = ">=3.12"
license = "MIT"
license-files = ["LICENSE"]
authors = [
    {name = "Context1 Contributors", email = "support@context1.dev"},
]
keywords = ["cli", "llm", "code", "packaging", "ai"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Code Generators",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
dependencies = [
    "pathspec>=0.12.1",
    "pyperclip>=1.11.0",
    "pytest>=9.0.1",
    "rich>=14.2.0",
    "typer>=0.20.0",
]

[project.scripts]
ctx1 = "context1.cli:app"
context1 = "context1.cli:app"


--- 文件: README.md ---
# Context1

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/yourusername/context1)

**Context1** - 在您的代码库和 LLM 之间架设桥梁的强大 CLI 工具

## 📖 简介

Context1 是一个专为开发者设计的命令行工具，能够将您的项目代码打包成单一文本上下文，为大型语言模型（LLM）提供完整的代码上下文信息。它支持智能文件过滤、多种排序策略、元数据提取、智能重构等高级功能，是您与 AI 协作开发的得力助手。

## ✨ 主要特性

### 🚀 核心功能
- 🚀 **智能文件过滤** - 支持 smart、whitelist、blacklist 三种过滤策略
- 🌳 **ASCII 目录树** - 生成类似 Linux `tree` 命令的目录结构
- 🔒 **安全防护** - 内置 Zip Slip 攻击防护机制
- 📊 **项目统计** - 提供文件数量、大小和 Token 估算
- 🎨 **美观界面** - 使用 Rich 库提供丰富的终端输出
- ⚙️ **灵活配置** - 支持项目级、用户级和默认配置
- 🧪 **全面测试** - 包含完整的单元测试套件

### 🏗️ v0.2.0 新增功能
- **DS-LPP 拓扑排序** - 基于领域驱动设计的智能文件排序
- **Python Bundle 格式** - 生成的包本身就是合法的 Python 代码文件
- **元数据提取** - 自动识别 `@Role` 和 `@Responsibility` 注解
- **智能重构引擎** - 基于结构树的文件重构和重命名
- **试运行模式** - 预览重构操作，避免意外覆盖
- **内容池机制** - 智能解决重名文件问题

## 📦 安装

### 从 PyPI 安装（推荐）

```bash
pip install context1
```

### 从源码安装

```bash
git clone https://github.com/yourusername/context1.git
cd context1
uv pip install -e .
```

### 使用 uv 安装

```bash
uv add context1
```

## 🚀 快速开始

### 基本用法

```bash
# 打包当前目录
context1 pack .

# 打包指定目录到文件
context1 pack /path/to/project -o project_context.md

# 复制到剪贴板
context1 pack . -c

# 使用过滤策略
context1 pack . -s whitelist
```

### 查看项目统计

```bash
context1 stats .
```

### 管理配置

```bash
# 初始化配置文件
context1 config init

# 查看当前配置
context1 config list
```

## 📖 详细使用指南

### Pack 命令

将项目代码打包为单一文本上下文。

```bash
context1 pack [OPTIONS] SOURCE
```

**参数：**
- `SOURCE`: 源目录路径（默认：当前目录）

**选项：**
- `-o, --output PATH`: 输出文件路径
- `-c, --clipboard`: 复制到剪贴板
- `-s, --strategy {smart,whitelist,blacklist}`: 过滤策略（默认：smart）
- `--sort {name,vscode,dslpp}`: 排序策略（默认：name）
- `--format {markdown,python-bundle}`: 输出格式（默认：markdown）
- `-v, --verbose`: 显示详细日志

**示例：**
```bash
# 基本打包
context1 pack .

# 使用 DS-LPP 排序和 Python Bundle 格式
context1 pack . --sort dslpp --format python-bundle -o project.py

# 使用 VSCode 风格排序
context1 pack . --sort vscode -o project.md

# 输出到指定文件
context1 pack ./my-project -o project.md

# 使用白名单过滤
context1 pack . -s whitelist -o filtered.md

# 复制到剪贴板
context1 pack . -c
```

### Stats 命令

显示项目统计信息。

```bash
context1 stats [OPTIONS] PATH
```

**参数：**
- `PATH`: 项目路径（默认：当前目录）

**输出信息：**
- 总文件数量
- 总大小（MB）
- 估算 Token 数量（字符数 / 4）

**示例：**
```bash
# 查看当前项目统计
context1 stats .

# 查看指定项目统计
context1 stats /path/to/project
```

### Config 命令

管理配置文件。

```bash
context1 config [OPTIONS] COMMAND
```

**子命令：**
- `init`: 创建默认配置文件
- `list`: 显示当前配置

**示例：**
```bash
# 初始化配置
context1 config init

# 查看配置
context1 config list
```

## ⚙️ 配置系统

Context1 使用三层配置系统：

1. **默认配置** - 内置的默认设置
2. **用户配置** - `~/.context1/config.json`
3. **项目配置** - `项目根目录/.context1/config.json`

### 配置文件示例

```json
{
  "strategy": "smart",
  "strategy_spec": {
    "patterns": [
      "*.py",
      "*.js",
      "*.ts",
      "*.json",
      "*.md",
      "*.txt"
    ]
  },
  "exclusions": [
    "*.lock",
    "*.log",
    "__pycache__/",
    "node_modules/",
    ".git/"
  ]
}
```

### 过滤策略

#### Smart（默认）
- 包含所有文件，排除常见的构建和缓存文件
- 自动排除：`.git/`, `__pycache__/`, `node_modules/`, `*.lock`, `*.log` 等

#### Whitelist
- 只包含配置文件中指定的文件类型
- 适合精确控制包含的文件

#### Blacklist
- 排除配置文件中指定的文件类型
- 适合排除特定类型的文件

## 🛡️ 安全特性

### Zip Slip 防护

Context1 内置了完整的 Zip Slip 攻击防护机制：

```python
def is_safe_path(base_dir: Path, target_path: str) -> bool:
    """检查路径是否安全，防止 Zip Slip 攻击"""
    try:
        base = base_dir.resolve()
        target = (base / target_path).resolve()
        return target.relative_to(base) == target_path
    except ValueError:
        return False
```

### 文件类型检测

自动检测二进制文件，避免将非文本文件包含在输出中。

## 🧪 测试

运行测试套件：

```bash
# 运行所有测试
pytest

# 运行安全测试
pytest tests/test_safety.py

# 运行文件扫描器测试
pytest tests/test_walker.py

# 生成覆盖率报告
pytest --cov=context1
```

### 测试覆盖

- **安全测试**：路径验证、Zip Slip 防护
- **功能测试**：文件过滤、Gitignore 集成、策略模式
- **集成测试**：CLI 命令、配置管理

## 📁 项目结构

```
context1/
├── src/
│   └── context1/
│       ├── __init__.py
│       ├── cli.py              # CLI 入口
│       ├── core/
│       │   ├── config.py       # 配置管理
│       │   ├── packer.py       # 打包逻辑
│       │   ├── unpacker.py     # 解包逻辑
│       │   └── walker.py       # 文件扫描器
│       └── utils/
│           └── fs.py           # 文件系统工具
├── tests/
│   ├── test_safety.py          # 安全测试
│   └── test_walker.py          # 功能测试
├── pyproject.toml
└── README.md
```

## 🔧 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/context1.git
cd context1

# 创建虚拟环境
uv venv

# 安装开发依赖
uv pip install -e ".[dev]"
```

### 代码规范

项目使用以下工具确保代码质量：

- **Black** - 代码格式化
- **Ruff** - 代码检查和修复
- **MyPy** - 类型检查

```bash
# 格式化代码
black src/ tests/

# 检查代码
ruff check src/ tests/

# 类型检查
mypy src/
```

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 创建 Pull Request

### 贡献指南

- 遵循 PEP 8 代码规范
- 添加适当的测试
- 更新文档
- 确保 CI/CD 测试通过

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Typer](https://typer.tiangolo.com/) - 现代 Python CLI 框架
- [Rich](https://github.com/Textualize/rich) - 终端美化库
- [PathSpec](https://github.com/cpburnz/python-pathspec) - Gitignore 模式匹配

## 📞 支持

如果您遇到问题或有建议，请：

1. 查看 [Issues](https://github.com/yourusername/context1/issues)
2. 创建新的 Issue
3. 发送邮件至：support@context1.dev

---

**Context1** - 让您的代码与 AI 完美协作 🚀


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


--- 文件: src/context1/core/config.py ---
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


--- 文件: src/context1/core/packer.py ---
"""
src/context1/core/packer.py
打包器 - 核心职责：生成目录树、文件排序、格式化输出(Markdown/XML/Python Bundle)
[修正版] 增加了内存溢出保护 (Pre-read size check)
"""
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime
from context1.core.config import Config, SortStrategy, OutputFormat

def calculate_dslpp_weight(filename: str, weights: List[Dict[str, Any]]) -> int:
    """
    计算 DS-LPP 权重
    Args:
        filename: 文件名
        weights: 权重配置列表
    Returns:
        权重值，未匹配则返回默认值 50
    """
    import fnmatch
    
    # 首先检查 test 文件，因为它有最高优先级
    if filename.startswith("test_") and filename.endswith(".py"):
        for weight_config in weights:
            if weight_config["pattern"] == "test_*.py":
                return weight_config["weight"]
    
    for weight_config in weights:
        pattern = weight_config["pattern"]
        weight = weight_config["weight"]
        
        # 跳过 test 模式，因为已经处理过了
        if pattern == "test_*.py":
            continue
            
        # 使用 fnmatch 进行 glob 模式匹配
        if fnmatch.fnmatch(filename, pattern):
            return weight
        # 额外处理一些特殊情况
        elif pattern == "*_ent.py" and filename.endswith("_entity.py"):
            return weight
        elif pattern == "*_d.py" and filename.endswith("_d.py"):
            return weight
        elif pattern == "*_i.py" and filename.endswith("_i.py"):
            return weight
        elif pattern == "*_c.py" and filename.endswith("_c.py"):
            return weight
        elif pattern == "*_bhv.py" and filename.endswith("_bhv.py"):
            return weight
        elif pattern == "*_u.py" and (filename.endswith("_u.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_stg.py" and filename.endswith("_stg.py"):
            return weight
        elif pattern == "*_s.py" and (filename.endswith("_s.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_cmd.py" and filename.endswith("_cmd.py"):
            return weight
    
    return 50  # 默认权重

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

def sort_files(files: List[Path], config: Config) -> List[Path]:
    """
    根据配置的排序策略对文件进行排序
    """
    root = config.project_root
    
    if config.sort_strategy == SortStrategy.NAME:
        # 默认按名称排序
        return sorted(files, key=lambda f: f.relative_to(root))
    elif config.sort_strategy == SortStrategy.VSCODE:
        # VSCode 风格排序
        return sorted(files, key=lambda f: vscode_sort_key(f.relative_to(root)))
    elif config.sort_strategy == SortStrategy.DSLPP:
        # DS-LPP 拓扑排序
        def dslpp_sort_key(file_path: Path) -> Tuple[int, str]:
            try:
                rel_path = file_path.relative_to(root)
                filename = rel_path.name
            except ValueError:
                # 如果无法获取相对路径，使用文件名本身
                filename = file_path.name
            weight = calculate_dslpp_weight(filename, config.dslpp_weights)
            return (weight, filename)
        
        return sorted(files, key=dslpp_sort_key)
    else:
        # 默认回退到名称排序
        return sorted(files, key=lambda f: f.relative_to(root))

def extract_metadata(file_path: Path) -> Dict[str, str]:
    """
    提取文件元数据（@Role 和 @Responsibility）
    Args:
        file_path: 文件路径
    Returns:
        包含 role 和 responsibility 的字典
    """
    metadata = {"role": "", "responsibility": ""}
    
    try:
        # 读取文件前 20 行
        lines = file_path.read_text(encoding='utf-8', errors='ignore').split('\n')[:20]
        
        # 正则匹配 @Role 和 @Responsibility，支持多行格式
        role_pattern = re.compile(r'@Role:\s*(.*?)(?:\n|$)')
        responsibility_pattern = re.compile(r'@Responsibility:\s*(.*?)(?:\n|$)')
        
        for line in lines:
            role_match = role_pattern.search(line)
            if role_match and not metadata["role"]:
                metadata["role"] = role_match.group(1).strip()
            
            responsibility_match = responsibility_pattern.search(line)
            if responsibility_match and not metadata["responsibility"]:
                metadata["responsibility"] = responsibility_match.group(1).strip()
                
    except Exception:
        # 如果读取失败，返回空元数据
        pass
    
    return metadata

def generate_layout_tree(files: List[Path], root: Path) -> str:
    """
    生成布局蓝图文件（纯文本树格式）
    目录名必须以 / 结尾
    """
    tree_lines = []
    
    # 过滤掉噪音文件
    filtered_files = []
    for file_path in files:
        rel_path = file_path.relative_to(root)
        # 排除 __init__.py, __pycache__ 等
        if (rel_path.name != "__init__.py" and 
            "__pycache__" not in rel_path.parts and
            not rel_path.name.startswith(".")):
            filtered_files.append(file_path)
    
    # 按目录分组
    dir_structure = {}
    for file_path in filtered_files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        
        # 确保目录以 / 结尾
        dir_key = str(dir_path) + "/" if dir_path != Path(".") else "./"
        if dir_key not in dir_structure:
            dir_structure[dir_key] = []
        dir_structure[dir_key].append(rel_path.name)
    
    # 生成树结构
    for dir_key in sorted(dir_structure.keys()):
        tree_lines.append(dir_key)
        for filename in sorted(dir_structure[dir_key]):
            tree_lines.append(f"  {filename}")
    
    return "\n".join(tree_lines)

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
    files_sorted = sort_files(files, config)
    
    output = []
    
    # 2. 元数据提取
    architecture_map = {}
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root)
        metadata = extract_metadata(file_path)
        if metadata["role"] or metadata["responsibility"]:
            architecture_map[str(rel_path)] = metadata
    
    # 3. Header & Metadata
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        # Python Bundle 格式
        output.append("#!/usr/bin/env python3")
        output.append(f"# CTX1_BUNDLE_VERSION: 0.2.0")
        
        # 添加 Architecture Map
        if architecture_map:
            output.append("# ================= Architecture Map =================")
            for file_path, metadata in architecture_map.items():
                role_info = f" [{metadata['role']}]" if metadata['role'] else ""
                responsibility_info = f": {metadata['responsibility']}" if metadata['responsibility'] else ""
                output.append(f"# {file_path}{role_info}{responsibility_info}")
            output.append("# ====================================================")
        output.append("")
    else:
        # Markdown 格式
        output.append(f"# Context1 Pack Result")
        output.append(f"Generated at: {datetime.now().isoformat()}")
        output.append(f"Strategy: {config.active_strategy}")
        output.append(f"Files: {len(files_sorted)}\n")
    
    # 4. Directory Tree
    if tree_view and config.output_format_enum != OutputFormat.PYTHON_BUNDLE:
        output.append(generate_tree(files_sorted, root))
        output.append("\n")
    
    # 5. File Contents
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root).as_posix()
        
        try:
            # [FIX] 内存安全检查：先看大小，再读文件
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            
            if file_size > config.max_file_size_kb * 1024:
                content = f"<!-- File skipped: size ({file_size} bytes) > {config.max_file_size_kb}KB -->"
            else:
                # 尝试 UTF-8 编码，如果失败则尝试 UTF-16
                try:
                    content = file_path.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    # 如果 UTF-8 失败，尝试 UTF-16
                    try:
                        content = file_path.read_text(encoding='utf-16')
                    except UnicodeDecodeError:
                        # 如果都失败，使用二进制模式读取并转义
                        with open(file_path, 'rb') as f:
                            binary_content = f.read()
                            content = binary_content.hex()  # 转换为十六进制字符串
                        content = f"<!-- Binary file content (hex): {content} -->"
            
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                # Python Bundle 格式
                output.append(f"# <ctx1:file path=\"{rel_path}\">")
                
                # 空行压缩：3行以上空行压缩为2行
                compressed_lines = []
                empty_count = 0
                for line in content.split('\n'):
                    if line.strip() == "":
                        empty_count += 1
                        if empty_count <= 2:
                            compressed_lines.append(line)
                    else:
                        empty_count = 0
                        compressed_lines.append(line)
                
                output.extend(compressed_lines)
                output.append("# </ctx1:file>")
                output.append("")
            elif config.output_format_enum == OutputFormat.MARKDOWN:
                # Markdown 格式
                output.append(f"--- 文件: {rel_path} ---")
                output.append(content)
                output.append("\n")
            else:
                # XML 格式（保留原有逻辑）
                output.append(f'<document path="{rel_path}">')
                output.append(content)
                output.append('</document>\n')
                
        except Exception as e:
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                output.append(f"# <!-- Error reading {rel_path}: {str(e)} -->")
            else:
                output.append(f"<!-- Error reading {rel_path}: {str(e)} -->\n")
    
    # 6. 生成布局蓝图
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        layout_tree_content = generate_layout_tree(files_sorted, root)
        layout_tree_path = config.project_root / ".context1" / "layout.tree"
        layout_tree_path.parent.mkdir(exist_ok=True)
        layout_tree_path.write_text(layout_tree_content, encoding='utf-8')
    
    # 7. 封装输出
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        return "\n".join(output)
    elif config.output_format_enum == OutputFormat.MARKDOWN:
        return "\n".join(output)
    else:
        return "<documents>\n" + "\n".join(output) + "\n</documents>"


--- 文件: src/context1/core/unpacker.py ---
"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版] 修复了 Python 缩进错误，优化了 strip 逻辑以保护数据完整性
[新增] 支持 Python Bundle 格式、智能内容池、结构树驱动重构
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from context1.utils.fs import safe_write_file

MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')
PYTHON_BUNDLE_PATTERN = re.compile(r'# <ctx1:file path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    """
    解析文档内容，返回文件列表
    支持三种格式：Markdown、XML、Python Bundle
    """
    # 统一换行符为 \n
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    format_type = None  # 'markdown', 'xml', 'python-bundle'
    
    for line in lines:
        # 检测格式类型
        if not format_type:
            if MD_PATTERN.match(line):
                format_type = 'markdown'
            elif XML_PATTERN.match(line):
                format_type = 'xml'
            elif PYTHON_BUNDLE_PATTERN.match(line):
                format_type = 'python-bundle'
        
        # Markdown Header Match
        if format_type == 'markdown':
            md_match = MD_PATTERN.match(line)
            if md_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = md_match.group(1).strip()
                current_content = []
                continue
                
        # XML Header Match
        elif format_type == 'xml':
            xml_match = XML_PATTERN.match(line)
            if xml_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = xml_match.group(1).strip()
                current_content = []
                continue
        
        # Python Bundle Header Match
        elif format_type == 'python-bundle':
            bundle_match = PYTHON_BUNDLE_PATTERN.match(line)
            if bundle_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = bundle_match.group(1).strip()
                current_content = []
                continue
            
            # Python Bundle Footer Match
            if current_file and line.strip() == '# </ctx1:file>':
                files.append({
                    'path': current_file,
                    'content': '\n'.join(current_content)
                })
                current_file = None
                current_content = []
                continue
         
        # Content Collection
        if current_file:
            if format_type == 'xml' and line.strip() == '</document>':
                continue
            # 保持原始缩进，不进行额外处理
            current_content.append(line)
            
    # Save last file
    if current_file:
        files.append({
            'path': current_file,
            'content': '\n'.join(current_content)
        })
        
    return files

class ContentPool:
    """
    智能内容池 - 解决重名文件问题
    """
    def __init__(self, files: List[Dict[str, str]]):
        self.pool: Dict[str, List[Tuple[str, str]]] = {}
        
        # 填充内容池
        for file_data in files:
            filename = Path(file_data['path']).name
            if filename not in self.pool:
                self.pool[filename] = []
            self.pool[filename].append((file_data['path'], file_data['content']))
    
    def get_file(self, filename: str) -> Optional[Tuple[str, str]]:
        """
        获取指定文件名的文件内容
        返回：(原始路径, 内容)
        """
        if filename in self.pool and len(self.pool[filename]) == 1:
            return self.pool[filename][0]
        return None
    
    def get_all_files(self, filename: str) -> List[Tuple[str, str]]:
        """
        获取所有同名文件
        """
        return self.pool.get(filename, [])

def parse_layout_tree(tree_content: str) -> List[str]:
    """
    解析布局树文件
    返回：目标路径列表
    """
    target_paths = []
    lines = tree_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # 处理缩进
        if line.startswith('  '):
            # 去掉缩进，保留相对路径
            line = line[2:]
        
        # 目录以 / 结尾，文件不以 / 结尾
        if line.endswith('/'):
            # 目录，跳过处理（只处理文件）
            continue
        else:
            # 文件，确保路径格式正确
            if not line.startswith('./'):
                line = './' + line
            target_paths.append(line)
    
    return target_paths

def calculate_path_similarity(path1: str, path2: str) -> int:
    """
    计算两个路径的相似度
    返回：重叠的目录层级数量
    """
    parts1 = Path(path1).parts
    parts2 = Path(path2).parts
    
    similarity = 0
    for i, (p1, p2) in enumerate(zip(parts1, parts2)):
        if p1 == p2:
            similarity += 1
        else:
            break
    
    return similarity

def resolve_target(target_path: str, content_pool: ContentPool) -> Tuple[str, str]:
    """
    解析目标路径对应的文件内容
    返回：(状态, 内容或错误信息)
    状态: 'match', 'scaffold', 'conflict'
    """
    filename = Path(target_path).name
    
    # Step 1: 检查唯一匹配
    unique_file = content_pool.get_file(filename)
    if unique_file:
        return 'match', unique_file
    
    # Step 2: 路径相似度匹配
    candidates = content_pool.get_all_files(filename)
    if candidates:
        best_match = None
        best_similarity = -1
        best_matches = []
        
        for candidate_path, candidate_content in candidates:
            similarity = calculate_path_similarity(target_path, candidate_path)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = (candidate_path, candidate_content)
                best_matches = [(candidate_path, candidate_content)]
            elif similarity == best_similarity:
                # 相似度相同，添加到候选列表
                best_matches.append((candidate_path, candidate_content))
        
        # 如果有多个最佳匹配，产生冲突
        if len(best_matches) > 1:
            return 'conflict', f"Multiple candidates with same similarity: {best_matches}"
        elif best_match:
            return 'match', best_match
    
    # Step 3: 特殊处理 __init__.py
    if filename == '__init__.py':
        return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"
    
    # Step 4: 脚手架
    return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"

def unpack_project(
    source_file: Path,
    output_dir: Path,
    force: bool = False,
    structure_only: bool = False,
    tree_path: Optional[Path] = None,
    dry_run: bool = False
) -> Dict[str, any]:
    """
    执行还原操作
    支持重构模式和试运行模式
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    # 尝试不同的编码读取文件
    content = ""
    for encoding in ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']:
        try:
            content = source_file.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    
    if not content:
        raise UnicodeDecodeError(f"无法解码文件: {source_file}")
    
    files = parse_document(content)
    
    # 创建内容池
    content_pool = ContentPool(files)
    
    # 检查是否为重构模式
    refactor_mode = tree_path is not None and tree_path.exists()
    
    if refactor_mode:
        # 重构模式：使用结构树
        tree_content = tree_path.read_text(encoding='utf-8')
        target_paths = parse_layout_tree(tree_content)
        
        stats = {
            "create": 0, "match": 0, "scaffold": 0, "conflict": 0,
            "skipped": 0, "failed": 0
        }
        
        # 检查目标目录是否为空
        if not dry_run and not force and any(output_dir.iterdir()):
            raise ValueError(f"目标目录 {output_dir} 不为空，请使用 --force 强制覆盖")
        
        for target_path in target_paths:
            status, content_or_error = resolve_target(target_path, content_pool)
            
            try:
                if dry_run:
                    # 试运行模式：只记录不写入
                    if status == 'match':
                        stats["match"] += 1
                    elif status == 'scaffold':
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        stats["conflict"] += 1
                else:
                    # 实际执行
                    if status == 'match':
                        written = safe_write_file(output_dir, target_path, content_or_error, force=force)
                        if written:
                            stats["match"] += 1
                        else:
                            stats["skipped"] += 1
                    elif status == 'scaffold':
                        # 创建脚手架文件
                        scaffold_path = output_dir / target_path
                        scaffold_path.parent.mkdir(parents=True, exist_ok=True)
                        scaffold_path.write_text(content_or_error, encoding='utf-8')
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        # 创建冲突文件
                        conflict_path = output_dir / f"{target_path}.CONFLICT"
                        conflict_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # 获取所有候选路径
                        candidates = content_pool.get_all_files(Path(target_path).name)
                        conflict_content = f"# Conflict resolution for {target_path}\n"
                        conflict_content += f"# Original candidates:\n"
                        for candidate_path, _ in candidates:
                            conflict_content += f"# - {candidate_path}\n"
                        
                        conflict_path.write_text(conflict_content, encoding='utf-8')
                        stats["conflict"] += 1
                        
            except Exception as e:
                if dry_run:
                    stats["failed"] += 1
                else:
                    print(f"❌ Error processing {target_path}: {e}")
                    stats["failed"] += 1
        
        return stats
    else:
        # 普通模式：直接还原
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
    使用 pathlib 的相对_to() 方法确保 target 在 base 目录下
    """
    try:
        base = Path(base_dir).resolve()
        
        # 允许 target_path 是绝对路径或相对路径
        if os.path.isabs(target_path):
            target = Path(target_path).resolve()
        else:
            target = (base / target_path).resolve()
            
        # 使用 pathlib 的相对_to() 方法进行安全检查
        # 如果 target 不在 base 目录下，会抛出 ValueError
        try:
            relative = target.relative_to(base)
            # 检查相对路径是否包含向上导航的组件
            return not any(part == '..' for part in relative.parts)
        except ValueError:
            # target 不在 base 目录下
            return False
            
    except Exception:
        return False

def is_binary_file(file_path: Path, chunk_size: int = 1024) -> bool:
    """
    通过读取前 chunk_size 字节检查是否包含 NULL 字节来判断是否为二进制文件
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
            
            # 如果文件为空，则不是二进制文件
            if not chunk:
                return False
            
            # 检查是否包含 NULL 字节
            has_null = b'\x00' in chunk
            
            # 如果包含 NULL 字节，检查是否可能是 UTF-16 编码的文本
            if has_null:
                # 检查是否是 UTF-16 BOM
                if chunk.startswith(b'\xff\xfe') or chunk.startswith(b'\xfe\xff'):
                    # 可能是 UTF-16 编码的文本，不是二进制文件
                    return False
                
                # 检查是否是纯文本的 UTF-16 编码（每个字符后跟 NULL 字节）
                # 如果大部分字符都是字母数字，并且 NULL 字节规律分布，可能是 UTF-16 文本
                null_positions = [i for i, b in enumerate(chunk) if b == 0]
                if len(null_positions) > 0:
                    # 检查 NULL 字节是否规律分布（每2个字节一个NULL）
                    is_utf16_pattern = True
                    for i in range(1, len(null_positions)):
                        if null_positions[i] - null_positions[i-1] != 2:
                            is_utf16_pattern = False
                            break
                    
                    # 如果大部分内容都是可打印字符，可能是 UTF-16 文本
                    printable_count = sum(1 for b in chunk if 32 <= b <= 126)
                    if is_utf16_pattern and printable_count > len(chunk) * 0.3:
                        return False
            
            # 如果包含 NULL 字节且不是 UTF-16 文本，则是二进制文件
            if has_null:
                return True
            
            # 如果没有 NULL 字节，则不是二进制文件
            return False
            
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


--- 文件: test_cli.py ---
#!/usr/bin/env python3
import sys
from pathlib import Path
# 确保引用的是本地 src 目录
sys.path.insert(0, str(Path.cwd() / 'src'))

from context1.cli import app
from typer.main import get_command

# 获取底层的 Click 命令对象
click_cmd = get_command(app)

print("✅ App loaded successfully!")
print(f"Available commands: {list(click_cmd.commands.keys())}")

# 检查 pack 命令的参数
if 'pack' in click_cmd.commands:
    pack_cmd = click_cmd.commands['pack']
    print("\n🔍 Checking 'pack' command parameters:")
    
    found_new_params = False
    for param in pack_cmd.params:
        # param.name 是参数名，param.opts 是命令行标志 (如 --sort)
        print(f"  - {param.name} {param.opts}")
        if param.name in ['sort', 'format']:
            found_new_params = True
            
    if found_new_params:
        print("\n✨ SUCCESS: New parameters 'sort' and 'format' detected!")
    else:
        print("\n❌ FAIL: New parameters not found.")
else:
    print("Pack command not found")


--- 文件: test_dslpp/__init__.py ---
# 初始化文件
@Role: Foundation
@Responsibility: 包初始化和基础配置


--- 文件: test_dslpp/test_user.py ---
# 测试文件
@Role: Test
@Responsibility: 用户模块测试
import unittest

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = {"name": "Test", "email": "test@example.com"}
        self.assertEqual(user["name"], "Test")


--- 文件: test_dslpp/user_bhv.py ---
# 行为层
@Role: Behavior
@Responsibility: 用户行为逻辑
class UserBehavior:
    def validate_email(self, email):
        return "@" in email and "." in email


--- 文件: test_dslpp/user_c.py ---
# 控制器层
@Role: Controller
@Responsibility: 用户控制器逻辑
from .user_i import UserServiceInterface

class UserController(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created with email {email}"


--- 文件: test_dslpp/user_cmd.py ---
# 命令层
@Role: Commander
@Responsibility: 用户命令处理
class UserCommand:
    def execute(self, user_data):
        return f"Command executed for user: {user_data['name']}"


--- 文件: test_dslpp/user_d.py ---
# 数据访问层
@Role: Data
@Responsibility: 用户数据访问逻辑
class UserData:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Test User"}


--- 文件: test_dslpp/user_ent.py ---
# 实体类文件
@Role: Entity
@Responsibility: 用户数据实体定义
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


--- 文件: test_dslpp/user_i.py ---
# 接口层
@Role: Interface
@Responsibility: 用户服务接口定义
from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, name, email):
        pass


--- 文件: test_dslpp/user_s.py ---
# 服务层
@Role: Service
@Responsibility: 用户服务实现
from .user_i import UserServiceInterface

class UserService(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created successfully"


--- 文件: test_dslpp/user_stg.py ---
# 策略层
@Role: Strategy
@Responsibility: 用户策略定义
class UserStrategy:
    def process_user(self, user_data):
        return f"Processing user: {user_data['name']}"


--- 文件: test_dslpp/user_u.py ---
# 工具层
@Role: Utility
@Responsibility: 用户相关工具函数
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


--- 文件: tests/test_packer.py ---
"""
单元测试 - Packer 模块
测试 DS-LPP 排序、Python Bundle 格式生成、元数据提取等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.config import Config, OutputFormat, SortStrategy, DEFAULT_DSLPP_WEIGHTS
from context1.core.packer import (
    calculate_dslpp_weight, 
    sort_files, 
    extract_metadata, 
    generate_layout_tree,
    generate_content
)


class TestDSLPPSorting:
    """测试 DS-LPP 排序功能"""
    
    def test_calculate_dslpp_weight_init(self):
        """测试 __init__.py 权重"""
        weight = calculate_dslpp_weight("__init__.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 0
    
    def test_calculate_dslpp_weight_entity(self):
        """测试实体文件权重"""
        weight = calculate_dslpp_weight("user_entity.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 10
    
    def test_calculate_dslpp_weight_command(self):
        """测试命令文件权重"""
        weight = calculate_dslpp_weight("search_cmd.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 40
    
    def test_calculate_dslpp_weight_test(self):
        """测试文件权重"""
        weight = calculate_dslpp_weight("test_user_service.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 99
    
    def test_calculate_dslpp_weight_default(self):
        """测试默认权重"""
        weight = calculate_dslpp_weight("unknown_file.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 50
    
    def test_sort_files_dslpp(self):
        """测试 DS-LPP 排序"""
        files = [
            Path("test_user_service.py"),
            Path("__init__.py"),
            Path("user_entity.py"),
            Path("search_cmd.py"),
            Path("user_service.py")
        ]
        
        config = Config(
            project_root=Path("/test"),
            sort_strategy=SortStrategy.DSLPP,
            dslpp_weights=DEFAULT_DSLPP_WEIGHTS
        )
        
        sorted_files = sort_files(files, config)
        
        # 验证排序结果
        assert str(sorted_files[0]) == "__init__.py"
        assert str(sorted_files[1]) == "user_entity.py"
        assert str(sorted_files[2]) == "user_service.py"
        assert str(sorted_files[3]) == "search_cmd.py"
        assert str(sorted_files[4]) == "test_user_service.py"


class TestMetadataExtraction:
    """测试元数据提取功能"""
    
    def test_extract_metadata_with_role(self):
        """测试提取角色信息"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
# @Role: Commander
# @Responsibility: 搜索入口
def search():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == "Commander"
            assert metadata["responsibility"] == "搜索入口"
        finally:
            temp_file.unlink()
    
    def test_extract_metadata_without_role(self):
        """测试无角色信息的文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
def simple_function():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == ""
            assert metadata["responsibility"] == ""
        finally:
            temp_file.unlink()


class TestPythonBundle:
    """测试 Python Bundle 格式生成"""
    
    def test_generate_content_python_bundle(self):
        """测试 Python Bundle 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.PYTHON_BUNDLE,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Python Bundle 格式
            assert "#!/usr/bin/env python3" in content
            assert "# CTX1_BUNDLE_VERSION: 0.2.0" in content
            assert '# <ctx1:file path="test.py">' in content
            assert "# </ctx1:file>" in content
            assert 'print("Hello, World!")' in content
    
    def test_generate_content_markdown(self):
        """测试 Markdown 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.MARKDOWN,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Markdown 格式
            assert "--- 文件: test.py ---" in content
            assert 'print("Hello, World!")' in content


class TestLayoutTree:
    """测试布局蓝图生成"""
    
    def test_generate_layout_tree(self):
        """测试布局蓝图生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            (temp_path / "src").mkdir()
            (temp_path / "tests").mkdir()
            
            (temp_path / "src" / "main.py").write_text("def main(): pass")
            (temp_path / "src" / "utils.py").write_text("def util(): pass")
            (temp_path / "tests" / "test_main.py").write_text("def test_main(): pass")
            (temp_path / "README.md").write_text("# Test Project")
            
            files = [
                temp_path / "src" / "main.py",
                temp_path / "src" / "utils.py",
                temp_path / "tests" / "test_main.py",
                temp_path / "README.md"
            ]
            
            tree_content = generate_layout_tree(files, temp_path)
            
            # 验证树格式
            assert "src/" in tree_content
            assert "tests/" in tree_content
            assert "main.py" in tree_content
            assert "utils.py" in tree_content
            assert "test_main.py" in tree_content
            assert "README.md" in tree_content


if __name__ == "__main__":
    pytest.main([__file__])


--- 文件: tests/test_safety.py ---
"""
测试文件系统安全性 - 核心职责：测试路径安全检查、Zip Slip 防护
"""
import pytest
import tempfile
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.utils.fs import is_safe_path

def test_is_safe_path_basic():
    """测试基本的安全路径检查"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 同一目录下的文件应该是安全的
        assert is_safe_path(base, "file.txt") == True
        assert is_safe_path(base, "subdir/file.txt") == True
        
        # 父目录应该是安全的
        assert is_safe_path(base, "..") == False
        assert is_safe_path(base, "../other") == False

def test_is_safe_path_absolute():
    """测试绝对路径的安全性"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 绝对路径指向同一目录应该是安全的
        abs_path = base / "file.txt"
        assert is_safe_path(base, str(abs_path)) == True
        
        # 绝对路径指向子目录应该是安全的
        subdir = base / "subdir"
        subdir.mkdir()
        abs_subdir_path = subdir / "file.txt"
        assert is_safe_path(base, str(abs_subdir_path)) == True
        
        # 绝对路径指向完全不同的目录应该是危险的
        with tempfile.TemporaryDirectory() as other_temp_dir:
            other_base = Path(other_temp_dir)
            other_abs_path = other_base / "file.txt"
            assert is_safe_path(base, str(other_abs_path)) == False

def test_is_safe_path_zip_slip_attack():
    """测试 Zip Slip 攻击防护"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 测试 Zip Slip 攻击模式
        attack_paths = [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "subdir/../../../etc/passwd",
            "subdir/..\\..\\..\\windows\\system32\\config\\sam",
        ]
        
        for attack_path in attack_paths:
            assert is_safe_path(base, attack_path) == False, f"Path '{attack_path}' should be blocked"

def test_is_safe_path_edge_cases():
    """测试边界情况"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 空路径
        assert is_safe_path(base, "") == True
        
        # 点路径
        assert is_safe_path(base, ".") == True
        
        # 相对路径到自身
        assert is_safe_path(base, "./file.txt") == True
        
        # 多层相对路径
        assert is_safe_path(base, "a/b/c/file.txt") == True

def test_is_safe_path_with_symlinks():
    """测试符号链接处理（如果支持）"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 创建一个符号链接指向外部目录
        try:
            external_file = Path(temp_dir) / "external.txt"
            external_file.write_text("test")
            
            symlink_path = base / "symlink"
            symlink_path.symlink_to(external_file)
            
            # 符号链接指向外部文件应该是安全的（如果解析后仍在 base 内）
            assert is_safe_path(base, "symlink") == True
            
        except (OSError, NotImplementedError):
            # 如果不支持符号链接，跳过测试
            pytest.skip("Symbolic links not supported on this platform")

if __name__ == "__main__":
    pytest.main([__file__])


--- 文件: tests/test_unpacker.py ---
"""
单元测试 - Unpacker 模块
测试文档解析、智能内容池、结构树驱动注入等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.unpacker import (
    parse_document,
    ContentPool,
    parse_layout_tree,
    calculate_path_similarity,
    resolve_target,
    unpack_project
)


class TestDocumentParsing:
    """测试文档解析功能"""
    
    def test_parse_markdown_format(self):
        """测试 Markdown 格式解析"""
        content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_xml_format(self):
        """测试 XML 格式解析"""
        content = """<document path="src/main.py">
def main():
    print("Hello, World!")
</document>

<document path="src/utils.py">
def util():
    pass
</document>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_python_bundle_format(self):
        """测试 Python Bundle 格式解析"""
        content = """#!/usr/bin/env python3
# CTX1_BUNDLE_VERSION: 0.2.0

# <ctx1:file path="src/main.py">
def main():
    print("Hello, World!")
# </ctx1:file>

# <ctx1:file path="src/utils.py">
def util():
    pass
# </ctx1:file>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'


class TestContentPool:
    """测试智能内容池功能"""
    
    def test_content_pool_creation(self):
        """测试内容池创建"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'src/utils.py', 'content': 'def util(): pass'},
            {'path': 'tests/test_main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        assert len(pool.pool) == 3
        assert 'main.py' in pool.pool
        assert 'utils.py' in pool.pool
        assert 'test_main.py' in pool.pool
    
    def test_content_pool_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        result = pool.get_file('main.py')
        
        assert result is not None
        assert result[0] == 'src/main.py'
        assert result[1] == 'def main(): pass'
    
    def test_content_pool_multiple_files(self):
        """测试多文件同名情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试获取所有同名文件
        all_files = pool.get_all_files('main.py')
        assert len(all_files) == 2
        assert all_files[0][0] == 'src/main.py'
        assert all_files[1][0] == 'tests/main.py'
        
        # 测试唯一匹配（应该返回 None）
        unique = pool.get_file('main.py')
        assert unique is None


class TestLayoutTree:
    """测试布局树功能"""
    
    def test_parse_layout_tree(self):
        """测试布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils.py
tests/
    test_main.py
    test_utils.py
README.md
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 5
        assert 'src/main.py' in target_paths
        assert 'src/utils.py' in target_paths
        assert 'tests/test_main.py' in target_paths
        assert 'tests/test_utils.py' in target_paths
        assert 'README.md' in target_paths
    
    def test_parse_layout_tree_with_directories(self):
        """测试包含目录的布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils/
        helper.py
tests/
    test_main.py
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 3
        assert 'src/main.py' in target_paths
        assert 'src/utils/helper.py' in target_paths
        assert 'tests/test_main.py' in target_paths


class TestPathSimilarity:
    """测试路径相似度计算"""
    
    def test_path_similarity_same_path(self):
        """测试相同路径"""
        similarity = calculate_path_similarity('src/main.py', 'src/main.py')
        assert similarity == 2  # 'src' + 'main.py'
    
    def test_path_similarity_common_prefix(self):
        """测试公共前缀"""
        similarity = calculate_path_similarity('src/main.py', 'src/utils.py')
        assert similarity == 1  # 'src'
    
    def test_path_similarity_different_prefix(self):
        """测试不同前缀"""
        similarity = calculate_path_similarity('src/main.py', 'tests/main.py')
        assert similarity == 0  # 无公共部分
    
    def test_path_similarity_nested(self):
        """测试嵌套路径"""
        similarity = calculate_path_similarity('src/utils/helper.py', 'src/utils/main.py')
        assert similarity == 2  # 'src' + 'utils'


class TestTargetResolution:
    """测试目标路径解析"""
    
    def test_resolve_target_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        status, content = resolve_target('src/main.py', pool)
        
        assert status == 'match'
        assert content == ('src/main.py', 'def main(): pass')
    
    def test_resolve_target_path_similarity(self):
        """测试路径相似度匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试匹配 src/main.py
        status, content = resolve_target('src/main.py', pool)
        assert status == 'match'
        assert content[0] == 'src/main.py'
        
        # 测试匹配 tests/main.py
        status, content = resolve_target('tests/main.py', pool)
        assert status == 'match'
        assert content[0] == 'tests/main.py'
    
    def test_resolve_target_conflict(self):
        """测试冲突情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试冲突（两个路径相似度相同）
        status, content = resolve_target('other/main.py', pool)
        assert status == 'conflict'
        assert 'Conflict resolution' in content
    
    def test_resolve_target_scaffold(self):
        """测试脚手架情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试不存在的文件
        status, content = resolve_target('src/new_file.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content
    
    def test_resolve_target_init_special_case(self):
        """测试 __init__.py 特殊处理"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试 __init__.py 特殊处理
        status, content = resolve_target('src/__init__.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content


class TestUnpackProject:
    """测试解包项目功能"""
    
    def test_unpack_project_normal_mode(self):
        """测试普通模式解包"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 解包到新目录
            output_dir = temp_path / "output"
            stats = unpack_project(bundle_file, output_dir)
            
            # 验证结果
            assert stats['success'] == 2
            assert stats['skipped'] == 0
            assert stats['failed'] == 0
            
            # 验证文件是否正确创建
            assert (output_dir / "src" / "main.py").exists()
            assert (output_dir / "src" / "utils.py").exists()
    
    def test_unpack_project_dry_run(self):
        """测试试运行模式"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 创建结构树
            tree_content = """src/
    main.py
    new_file.py"""
            
            tree_file = temp_path / "layout.tree"
            tree_file.write_text(tree_content)
            
            # 试运行
            output_dir = temp_path / "output"
            stats = unpack_project(
                bundle_file, 
                output_dir, 
                tree_path=tree_file,
                dry_run=True
            )
            
            # 验证结果
            assert stats['match'] == 1  # main.py 匹配
            assert stats['scaffold'] == 1  # new_file.py 脚手架
            assert stats['conflict'] == 0
            assert stats['failed'] == 0
            
            # 验证文件未实际创建
            assert not output_dir.exists()


if __name__ == "__main__":
    pytest.main([__file__])


--- 文件: tests/test_walker.py ---
"""
测试文件扫描器 - 核心职责：测试文件过滤、Gitignore集成、策略过滤
"""
import pytest
import tempfile
import json
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.core.config import Config
from context1.core.walker import FileWalker

def create_test_files(base_dir: Path):
    """创建测试文件结构"""
    # 创建各种类型的文件
    (base_dir / "main.py").write_text("# Main file")
    (base_dir / "test.py").write_text("# Test file")
    (base_dir / "data.json").write_text('{"key": "value"}')
    (base_dir / "README.md").write_text("# README")
    (base_dir / "config.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # 创建二进制文件
    (base_dir / "binary.exe").write_bytes(b"\x00\x01\x02\x03")
    (base_dir / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    
    # 创建锁定文件
    (base_dir / "package-lock.json").write_text("{}")
    (base_dir / "yarn.lock").write_text("# yarn lock")
    (base_dir / "poetry.lock").write_text("# poetry lock")
    
    # 创建子目录
    subdir = base_dir / "src"
    subdir.mkdir()
    (subdir / "module.py").write_text("# Module file")
    (subdir / "test.lock").write_text("# Test lock file")
    
    # 创建 .gitignore
    (base_dir / ".gitignore").write_text("""
__pycache__/
*.pyc
*.pyo
*.pyd
*.class
*.lock
.venv/
venv/
env/
node_modules/
""")

def test_walker_excludes_lock_files():
    """测试 walker 是否正确排除 .lock 文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            always_exclude=["*.lock"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有 .lock 文件
        lock_files = [f for f in files if f.name.endswith('.lock')]
        assert len(lock_files) == 0, f"Found lock files that should be excluded: {lock_files}"

def test_walker_excludes_binary_files():
    """测试 walker 是否正确排除二进制文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            binary_extensions=[".exe", ".png"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有二进制文件
        binary_files = [f for f in files if f.suffix.lower() in ['.exe', '.png']]
        assert len(binary_files) == 0, f"Found binary files that should be excluded: {binary_files}"

def test_walker_respects_gitignore():
    """测试 walker 是否正确遵循 .gitignore"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            use_gitignore=True,
            always_exclude=[]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否排除了 .gitignore 中指定的文件
        file_names = [f.name for f in files]
        
        # 应该排除的文件
        excluded_patterns = ["__pycache__", "*.pyc", "*.pyo", "*.pyd", "*.lock", ".venv", "venv", "env", "node_modules"]
        
        # 检查是否有被排除的文件
        for pattern in excluded_patterns:
            if pattern.endswith('*'):
                # 处理通配符
                prefix = pattern[:-1]
                matching_files = [f for f in file_names if f.startswith(prefix)]
                assert len(matching_files) == 0, f"Found files matching pattern '{pattern}': {matching_files}"
            else:
                assert pattern not in file_names, f"Found excluded file: {pattern}"

def test_walker_smart_strategy():
    """测试 smart 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="smart"
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该找到所有非二进制、非锁定、非排除的文件
        expected_files = ["main.py", "test.py", "data.json", "README.md", "config.toml"]
        file_names = [f.name for f in files]
        
        for expected_file in expected_files:
            assert expected_file in file_names, f"Expected file '{expected_file}' not found in scan results"

def test_walker_blacklist_strategy():
    """测试 blacklist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="blacklist"
        )
        
        # 创建黑名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        blacklist_file = ctx_dir / "blacklist.json"
        blacklist_data = {
            "patterns": ["*.json", "src/"]
        }
        with open(blacklist_file, 'w') as f:
            json.dump(blacklist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该排除 .json 文件和 src 目录
        file_names = [f.name for f in files]
        relative_paths = [str(f.relative_to(base_dir)) for f in files]
        
        # 检查是否排除了 .json 文件
        json_files = [f for f in file_names if f.endswith('.json')]
        assert len(json_files) == 0, f"Found JSON files that should be blacklisted: {json_files}"
        
        # 检查是否排除了 src 目录
        src_files = [f for f in relative_paths if f.startswith('src/')]
        assert len(src_files) == 0, f"Found src directory files that should be blacklisted: {src_files}"

def test_walker_whitelist_strategy():
    """测试 whitelist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="whitelist"
        )
        
        # 创建白名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        whitelist_file = ctx_dir / "whitelist.json"
        whitelist_data = {
            "patterns": ["*.py", "README.md"]
        }
        with open(whitelist_file, 'w') as f:
            json.dump(whitelist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该只包含 .py 文件和 README.md
        file_names = [f.name for f in files]
        
        # 检查是否只包含白名单文件
        for file_name in file_names:
            assert file_name.endswith('.py') or file_name == 'README.md', f"Found non-whitelisted file: {file_name}"

def test_walker_empty_directory():
    """测试空目录的扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        
        # 创建配置
        config = Config(project_root=base_dir)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该返回空列表
        assert len(files) == 0, f"Expected no files in empty directory, found: {files}"

if __name__ == "__main__":
    pytest.main([__file__])


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
version = "0.2.0"
source = { virtual = "." }
dependencies = [
    { name = "pathspec" },
    { name = "pyperclip" },
    { name = "pytest" },
    { name = "rich" },
    { name = "typer" },
]

[package.metadata]
requires-dist = [
    { name = "pathspec", specifier = ">=0.12.1" },
    { name = "pyperclip", specifier = ">=1.11.0" },
    { name = "pytest", specifier = ">=9.0.1" },
    { name = "rich", specifier = ">=14.2.0" },
    { name = "typer", specifier = ">=0.20.0" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
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
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
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
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
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
name = "pytest"
version = "9.0.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/07/56/f013048ac4bc4c1d9be45afd4ab209ea62822fb1598f40687e6bf45dcea4/pytest-9.0.1.tar.gz", hash = "sha256:3e9c069ea73583e255c3b21cf46b8d3c56f6e3a1a8f6da94ccb0fcf57b9d73c8", size = 1564125, upload-time = "2025-11-12T13:05:09.333Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/8b/6300fb80f858cda1c51ffa17075df5d846757081d11ab4aa35cef9e6258b/pytest-9.0.1-py3-none-any.whl", hash = "sha256:67be0030d194df2dfa7b556f2e56fb3c3315bd5c8822c6951162b92b32ce7dad", size = 373668, upload-time = "2025-11-12T13:05:07.379Z" },
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


# </ctx1:file>

# <ctx1:file path="ctx1">
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
# </ctx1:file>

# <ctx1:file path="LICENSE">
MIT License

Copyright (c) 2025 Context1 Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# </ctx1:file>

# <ctx1:file path="pyproject.toml">
[project]
name = "context1"
version = "0.2.0"
description = "在您的代码库和 LLM 之间架设桥梁的强大 CLI 工具"
readme = "README.md"
requires-python = ">=3.12"
license = "MIT"
license-files = ["LICENSE"]
authors = [
    {name = "Context1 Contributors", email = "support@context1.dev"},
]
keywords = ["cli", "llm", "code", "packaging", "ai"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Code Generators",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
dependencies = [
    "pathspec>=0.12.1",
    "pyperclip>=1.11.0",
    "pytest>=9.0.1",
    "rich>=14.2.0",
    "typer>=0.20.0",
]

[project.scripts]
ctx1 = "context1.cli:app"
context1 = "context1.cli:app"


# </ctx1:file>

# <ctx1:file path="README.md">
# Context1

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/yourusername/context1)

**Context1** - 在您的代码库和 LLM 之间架设桥梁的强大 CLI 工具

## 📖 简介

Context1 是一个专为开发者设计的命令行工具，能够将您的项目代码打包成单一文本上下文，为大型语言模型（LLM）提供完整的代码上下文信息。它支持智能文件过滤、多种排序策略、元数据提取、智能重构等高级功能，是您与 AI 协作开发的得力助手。

## ✨ 主要特性

### 🚀 核心功能
- 🚀 **智能文件过滤** - 支持 smart、whitelist、blacklist 三种过滤策略
- 🌳 **ASCII 目录树** - 生成类似 Linux `tree` 命令的目录结构
- 🔒 **安全防护** - 内置 Zip Slip 攻击防护机制
- 📊 **项目统计** - 提供文件数量、大小和 Token 估算
- 🎨 **美观界面** - 使用 Rich 库提供丰富的终端输出
- ⚙️ **灵活配置** - 支持项目级、用户级和默认配置
- 🧪 **全面测试** - 包含完整的单元测试套件

### 🏗️ v0.2.0 新增功能
- **DS-LPP 拓扑排序** - 基于领域驱动设计的智能文件排序
- **Python Bundle 格式** - 生成的包本身就是合法的 Python 代码文件
- **元数据提取** - 自动识别 `@Role` 和 `@Responsibility` 注解
- **智能重构引擎** - 基于结构树的文件重构和重命名
- **试运行模式** - 预览重构操作，避免意外覆盖
- **内容池机制** - 智能解决重名文件问题

## 📦 安装

### 从 PyPI 安装（推荐）

```bash
pip install context1
```

### 从源码安装

```bash
git clone https://github.com/yourusername/context1.git
cd context1
uv pip install -e .
```

### 使用 uv 安装

```bash
uv add context1
```

## 🚀 快速开始

### 基本用法

```bash
# 打包当前目录
context1 pack .

# 打包指定目录到文件
context1 pack /path/to/project -o project_context.md

# 复制到剪贴板
context1 pack . -c

# 使用过滤策略
context1 pack . -s whitelist
```

### 查看项目统计

```bash
context1 stats .
```

### 管理配置

```bash
# 初始化配置文件
context1 config init

# 查看当前配置
context1 config list
```

## 📖 详细使用指南

### Pack 命令

将项目代码打包为单一文本上下文。

```bash
context1 pack [OPTIONS] SOURCE
```

**参数：**
- `SOURCE`: 源目录路径（默认：当前目录）

**选项：**
- `-o, --output PATH`: 输出文件路径
- `-c, --clipboard`: 复制到剪贴板
- `-s, --strategy {smart,whitelist,blacklist}`: 过滤策略（默认：smart）
- `--sort {name,vscode,dslpp}`: 排序策略（默认：name）
- `--format {markdown,python-bundle}`: 输出格式（默认：markdown）
- `-v, --verbose`: 显示详细日志

**示例：**
```bash
# 基本打包
context1 pack .

# 使用 DS-LPP 排序和 Python Bundle 格式
context1 pack . --sort dslpp --format python-bundle -o project.py

# 使用 VSCode 风格排序
context1 pack . --sort vscode -o project.md

# 输出到指定文件
context1 pack ./my-project -o project.md

# 使用白名单过滤
context1 pack . -s whitelist -o filtered.md

# 复制到剪贴板
context1 pack . -c
```

### Stats 命令

显示项目统计信息。

```bash
context1 stats [OPTIONS] PATH
```

**参数：**
- `PATH`: 项目路径（默认：当前目录）

**输出信息：**
- 总文件数量
- 总大小（MB）
- 估算 Token 数量（字符数 / 4）

**示例：**
```bash
# 查看当前项目统计
context1 stats .

# 查看指定项目统计
context1 stats /path/to/project
```

### Config 命令

管理配置文件。

```bash
context1 config [OPTIONS] COMMAND
```

**子命令：**
- `init`: 创建默认配置文件
- `list`: 显示当前配置

**示例：**
```bash
# 初始化配置
context1 config init

# 查看配置
context1 config list
```

## ⚙️ 配置系统

Context1 使用三层配置系统：

1. **默认配置** - 内置的默认设置
2. **用户配置** - `~/.context1/config.json`
3. **项目配置** - `项目根目录/.context1/config.json`

### 配置文件示例

```json
{
  "strategy": "smart",
  "strategy_spec": {
    "patterns": [
      "*.py",
      "*.js",
      "*.ts",
      "*.json",
      "*.md",
      "*.txt"
    ]
  },
  "exclusions": [
    "*.lock",
    "*.log",
    "__pycache__/",
    "node_modules/",
    ".git/"
  ]
}
```

### 过滤策略

#### Smart（默认）
- 包含所有文件，排除常见的构建和缓存文件
- 自动排除：`.git/`, `__pycache__/`, `node_modules/`, `*.lock`, `*.log` 等

#### Whitelist
- 只包含配置文件中指定的文件类型
- 适合精确控制包含的文件

#### Blacklist
- 排除配置文件中指定的文件类型
- 适合排除特定类型的文件

## 🛡️ 安全特性

### Zip Slip 防护

Context1 内置了完整的 Zip Slip 攻击防护机制：

```python
def is_safe_path(base_dir: Path, target_path: str) -> bool:
    """检查路径是否安全，防止 Zip Slip 攻击"""
    try:
        base = base_dir.resolve()
        target = (base / target_path).resolve()
        return target.relative_to(base) == target_path
    except ValueError:
        return False
```

### 文件类型检测

自动检测二进制文件，避免将非文本文件包含在输出中。

## 🧪 测试

运行测试套件：

```bash
# 运行所有测试
pytest

# 运行安全测试
pytest tests/test_safety.py

# 运行文件扫描器测试
pytest tests/test_walker.py

# 生成覆盖率报告
pytest --cov=context1
```

### 测试覆盖

- **安全测试**：路径验证、Zip Slip 防护
- **功能测试**：文件过滤、Gitignore 集成、策略模式
- **集成测试**：CLI 命令、配置管理

## 📁 项目结构

```
context1/
├── src/
│   └── context1/
│       ├── __init__.py
│       ├── cli.py              # CLI 入口
│       ├── core/
│       │   ├── config.py       # 配置管理
│       │   ├── packer.py       # 打包逻辑
│       │   ├── unpacker.py     # 解包逻辑
│       │   └── walker.py       # 文件扫描器
│       └── utils/
│           └── fs.py           # 文件系统工具
├── tests/
│   ├── test_safety.py          # 安全测试
│   └── test_walker.py          # 功能测试
├── pyproject.toml
└── README.md
```

## 🔧 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/context1.git
cd context1

# 创建虚拟环境
uv venv

# 安装开发依赖
uv pip install -e ".[dev]"
```

### 代码规范

项目使用以下工具确保代码质量：

- **Black** - 代码格式化
- **Ruff** - 代码检查和修复
- **MyPy** - 类型检查

```bash
# 格式化代码
black src/ tests/

# 检查代码
ruff check src/ tests/

# 类型检查
mypy src/
```

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'Add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 创建 Pull Request

### 贡献指南

- 遵循 PEP 8 代码规范
- 添加适当的测试
- 更新文档
- 确保 CI/CD 测试通过

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Typer](https://typer.tiangolo.com/) - 现代 Python CLI 框架
- [Rich](https://github.com/Textualize/rich) - 终端美化库
- [PathSpec](https://github.com/cpburnz/python-pathspec) - Gitignore 模式匹配

## 📞 支持

如果您遇到问题或有建议，请：

1. 查看 [Issues](https://github.com/yourusername/context1/issues)
2. 创建新的 Issue
3. 发送邮件至：support@context1.dev

---

**Context1** - 让您的代码与 AI 完美协作 🚀
# </ctx1:file>

# <ctx1:file path="src/context1/cli.py">
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


# </ctx1:file>

# <ctx1:file path="src/context1/core/config.py">
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
# </ctx1:file>

# <ctx1:file path="src/context1/core/packer.py">
"""
src/context1/core/packer.py
打包器 - 核心职责：生成目录树、文件排序、格式化输出(Markdown/XML/Python Bundle)
[修正版] 增加了内存溢出保护 (Pre-read size check)
"""
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime
from context1.core.config import Config, SortStrategy, OutputFormat

def calculate_dslpp_weight(filename: str, weights: List[Dict[str, Any]]) -> int:
    """
    计算 DS-LPP 权重
    Args:
        filename: 文件名
        weights: 权重配置列表
    Returns:
        权重值，未匹配则返回默认值 50
    """
    import fnmatch
    
    # 首先检查 test 文件，因为它有最高优先级
    if filename.startswith("test_") and filename.endswith(".py"):
        for weight_config in weights:
            if weight_config["pattern"] == "test_*.py":
                return weight_config["weight"]
    
    for weight_config in weights:
        pattern = weight_config["pattern"]
        weight = weight_config["weight"]
        
        # 跳过 test 模式，因为已经处理过了
        if pattern == "test_*.py":
            continue
            
        # 使用 fnmatch 进行 glob 模式匹配
        if fnmatch.fnmatch(filename, pattern):
            return weight
        # 额外处理一些特殊情况
        elif pattern == "*_ent.py" and filename.endswith("_entity.py"):
            return weight
        elif pattern == "*_d.py" and filename.endswith("_d.py"):
            return weight
        elif pattern == "*_i.py" and filename.endswith("_i.py"):
            return weight
        elif pattern == "*_c.py" and filename.endswith("_c.py"):
            return weight
        elif pattern == "*_bhv.py" and filename.endswith("_bhv.py"):
            return weight
        elif pattern == "*_u.py" and (filename.endswith("_u.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_stg.py" and filename.endswith("_stg.py"):
            return weight
        elif pattern == "*_s.py" and (filename.endswith("_s.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_cmd.py" and filename.endswith("_cmd.py"):
            return weight
    
    return 50  # 默认权重

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

def sort_files(files: List[Path], config: Config) -> List[Path]:
    """
    根据配置的排序策略对文件进行排序
    """
    root = config.project_root
    
    if config.sort_strategy == SortStrategy.NAME:
        # 默认按名称排序
        return sorted(files, key=lambda f: f.relative_to(root))
    elif config.sort_strategy == SortStrategy.VSCODE:
        # VSCode 风格排序
        return sorted(files, key=lambda f: vscode_sort_key(f.relative_to(root)))
    elif config.sort_strategy == SortStrategy.DSLPP:
        # DS-LPP 拓扑排序
        def dslpp_sort_key(file_path: Path) -> Tuple[int, str]:
            try:
                rel_path = file_path.relative_to(root)
                filename = rel_path.name
            except ValueError:
                # 如果无法获取相对路径，使用文件名本身
                filename = file_path.name
            weight = calculate_dslpp_weight(filename, config.dslpp_weights)
            return (weight, filename)
        
        return sorted(files, key=dslpp_sort_key)
    else:
        # 默认回退到名称排序
        return sorted(files, key=lambda f: f.relative_to(root))

def extract_metadata(file_path: Path) -> Dict[str, str]:
    """
    提取文件元数据（@Role 和 @Responsibility）
    Args:
        file_path: 文件路径
    Returns:
        包含 role 和 responsibility 的字典
    """
    metadata = {"role": "", "responsibility": ""}
    
    try:
        # 读取文件前 20 行
        lines = file_path.read_text(encoding='utf-8', errors='ignore').split('\n')[:20]
        
        # 正则匹配 @Role 和 @Responsibility，支持多行格式
        role_pattern = re.compile(r'@Role:\s*(.*?)(?:\n|$)')
        responsibility_pattern = re.compile(r'@Responsibility:\s*(.*?)(?:\n|$)')
        
        for line in lines:
            role_match = role_pattern.search(line)
            if role_match and not metadata["role"]:
                metadata["role"] = role_match.group(1).strip()
            
            responsibility_match = responsibility_pattern.search(line)
            if responsibility_match and not metadata["responsibility"]:
                metadata["responsibility"] = responsibility_match.group(1).strip()
                
    except Exception:
        # 如果读取失败，返回空元数据
        pass
    
    return metadata

def generate_layout_tree(files: List[Path], root: Path) -> str:
    """
    生成布局蓝图文件（纯文本树格式）
    目录名必须以 / 结尾
    """
    tree_lines = []
    
    # 过滤掉噪音文件
    filtered_files = []
    for file_path in files:
        rel_path = file_path.relative_to(root)
        # 排除 __init__.py, __pycache__ 等
        if (rel_path.name != "__init__.py" and 
            "__pycache__" not in rel_path.parts and
            not rel_path.name.startswith(".")):
            filtered_files.append(file_path)
    
    # 按目录分组
    dir_structure = {}
    for file_path in filtered_files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        
        # 确保目录以 / 结尾
        dir_key = str(dir_path) + "/" if dir_path != Path(".") else "./"
        if dir_key not in dir_structure:
            dir_structure[dir_key] = []
        dir_structure[dir_key].append(rel_path.name)
    
    # 生成树结构
    for dir_key in sorted(dir_structure.keys()):
        tree_lines.append(dir_key)
        for filename in sorted(dir_structure[dir_key]):
            tree_lines.append(f"  {filename}")
    
    return "\n".join(tree_lines)

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
    files_sorted = sort_files(files, config)
    
    output = []
    
    # 2. 元数据提取
    architecture_map = {}
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root)
        metadata = extract_metadata(file_path)
        if metadata["role"] or metadata["responsibility"]:
            architecture_map[str(rel_path)] = metadata
    
    # 3. Header & Metadata
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        # Python Bundle 格式
        output.append("#!/usr/bin/env python3")
        output.append(f"# CTX1_BUNDLE_VERSION: 0.2.0")
        
        # 添加 Architecture Map
        if architecture_map:
            output.append("# ================= Architecture Map =================")
            for file_path, metadata in architecture_map.items():
                role_info = f" [{metadata['role']}]" if metadata['role'] else ""
                responsibility_info = f": {metadata['responsibility']}" if metadata['responsibility'] else ""
                output.append(f"# {file_path}{role_info}{responsibility_info}")
            output.append("# ====================================================")
        output.append("")
    else:
        # Markdown 格式
        output.append(f"# Context1 Pack Result")
        output.append(f"Generated at: {datetime.now().isoformat()}")
        output.append(f"Strategy: {config.active_strategy}")
        output.append(f"Files: {len(files_sorted)}\n")
    
    # 4. Directory Tree
    if tree_view and config.output_format_enum != OutputFormat.PYTHON_BUNDLE:
        output.append(generate_tree(files_sorted, root))
        output.append("\n")
    
    # 5. File Contents
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root).as_posix()
        
        try:
            # [FIX] 内存安全检查：先看大小，再读文件
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            
            if file_size > config.max_file_size_kb * 1024:
                content = f"<!-- File skipped: size ({file_size} bytes) > {config.max_file_size_kb}KB -->"
            else:
                # 尝试 UTF-8 编码，如果失败则尝试 UTF-16
                try:
                    content = file_path.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    # 如果 UTF-8 失败，尝试 UTF-16
                    try:
                        content = file_path.read_text(encoding='utf-16')
                    except UnicodeDecodeError:
                        # 如果都失败，使用二进制模式读取并转义
                        with open(file_path, 'rb') as f:
                            binary_content = f.read()
                            content = binary_content.hex()  # 转换为十六进制字符串
                        content = f"<!-- Binary file content (hex): {content} -->"
            
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                # Python Bundle 格式
                output.append(f"# <ctx1:file path=\"{rel_path}\">")
                
                # 空行压缩：3行以上空行压缩为2行
                compressed_lines = []
                empty_count = 0
                for line in content.split('\n'):
                    if line.strip() == "":
                        empty_count += 1
                        if empty_count <= 2:
                            compressed_lines.append(line)
                    else:
                        empty_count = 0
                        compressed_lines.append(line)
                
                output.extend(compressed_lines)
                output.append("# </ctx1:file>")
                output.append("")
            elif config.output_format_enum == OutputFormat.MARKDOWN:
                # Markdown 格式
                output.append(f"--- 文件: {rel_path} ---")
                output.append(content)
                output.append("\n")
            else:
                # XML 格式（保留原有逻辑）
                output.append(f'<document path="{rel_path}">')
                output.append(content)
                output.append('</document>\n')
                
        except Exception as e:
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                output.append(f"# <!-- Error reading {rel_path}: {str(e)} -->")
            else:
                output.append(f"<!-- Error reading {rel_path}: {str(e)} -->\n")
    
    # 6. 生成布局蓝图
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        layout_tree_content = generate_layout_tree(files_sorted, root)
        layout_tree_path = config.project_root / ".context1" / "layout.tree"
        layout_tree_path.parent.mkdir(exist_ok=True)
        layout_tree_path.write_text(layout_tree_content, encoding='utf-8')
    
    # 7. 封装输出
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        return "\n".join(output)
    elif config.output_format_enum == OutputFormat.MARKDOWN:
        return "\n".join(output)
    else:
        return "<documents>\n" + "\n".join(output) + "\n</documents>"


# </ctx1:file>

# <ctx1:file path="src/context1/core/unpacker.py">
"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版] 修复了 Python 缩进错误，优化了 strip 逻辑以保护数据完整性
[新增] 支持 Python Bundle 格式、智能内容池、结构树驱动重构
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from context1.utils.fs import safe_write_file

MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')
PYTHON_BUNDLE_PATTERN = re.compile(r'# <ctx1:file path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    """
    解析文档内容，返回文件列表
    支持三种格式：Markdown、XML、Python Bundle
    """
    # 统一换行符为 \n
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    format_type = None  # 'markdown', 'xml', 'python-bundle'
    
    for line in lines:
        # 检测格式类型
        if not format_type:
            if MD_PATTERN.match(line):
                format_type = 'markdown'
            elif XML_PATTERN.match(line):
                format_type = 'xml'
            elif PYTHON_BUNDLE_PATTERN.match(line):
                format_type = 'python-bundle'
        
        # Markdown Header Match
        if format_type == 'markdown':
            md_match = MD_PATTERN.match(line)
            if md_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = md_match.group(1).strip()
                current_content = []
                continue
                
        # XML Header Match
        elif format_type == 'xml':
            xml_match = XML_PATTERN.match(line)
            if xml_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = xml_match.group(1).strip()
                current_content = []
                continue
        
        # Python Bundle Header Match
        elif format_type == 'python-bundle':
            bundle_match = PYTHON_BUNDLE_PATTERN.match(line)
            if bundle_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = bundle_match.group(1).strip()
                current_content = []
                continue
            
            # Python Bundle Footer Match
            if current_file and line.strip() == '# </ctx1:file>':
                files.append({
                    'path': current_file,
                    'content': '\n'.join(current_content)
                })
                current_file = None
                current_content = []
                continue
         
        # Content Collection
        if current_file:
            if format_type == 'xml' and line.strip() == '</document>':
                continue
            # 保持原始缩进，不进行额外处理
            current_content.append(line)
            
    # Save last file
    if current_file:
        files.append({
            'path': current_file,
            'content': '\n'.join(current_content)
        })
        
    return files

class ContentPool:
    """
    智能内容池 - 解决重名文件问题
    """
    def __init__(self, files: List[Dict[str, str]]):
        self.pool: Dict[str, List[Tuple[str, str]]] = {}
        
        # 填充内容池
        for file_data in files:
            filename = Path(file_data['path']).name
            if filename not in self.pool:
                self.pool[filename] = []
            self.pool[filename].append((file_data['path'], file_data['content']))
    
    def get_file(self, filename: str) -> Optional[Tuple[str, str]]:
        """
        获取指定文件名的文件内容
        返回：(原始路径, 内容)
        """
        if filename in self.pool and len(self.pool[filename]) == 1:
            return self.pool[filename][0]
        return None
    
    def get_all_files(self, filename: str) -> List[Tuple[str, str]]:
        """
        获取所有同名文件
        """
        return self.pool.get(filename, [])

def parse_layout_tree(tree_content: str) -> List[str]:
    """
    解析布局树文件
    返回：目标路径列表
    """
    target_paths = []
    lines = tree_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # 处理缩进
        if line.startswith('  '):
            # 去掉缩进，保留相对路径
            line = line[2:]
        
        # 目录以 / 结尾，文件不以 / 结尾
        if line.endswith('/'):
            # 目录，跳过处理（只处理文件）
            continue
        else:
            # 文件，确保路径格式正确
            if not line.startswith('./'):
                line = './' + line
            target_paths.append(line)
    
    return target_paths

def calculate_path_similarity(path1: str, path2: str) -> int:
    """
    计算两个路径的相似度
    返回：重叠的目录层级数量
    """
    parts1 = Path(path1).parts
    parts2 = Path(path2).parts
    
    similarity = 0
    for i, (p1, p2) in enumerate(zip(parts1, parts2)):
        if p1 == p2:
            similarity += 1
        else:
            break
    
    return similarity

def resolve_target(target_path: str, content_pool: ContentPool) -> Tuple[str, str]:
    """
    解析目标路径对应的文件内容
    返回：(状态, 内容或错误信息)
    状态: 'match', 'scaffold', 'conflict'
    """
    filename = Path(target_path).name
    
    # Step 1: 检查唯一匹配
    unique_file = content_pool.get_file(filename)
    if unique_file:
        return 'match', unique_file
    
    # Step 2: 路径相似度匹配
    candidates = content_pool.get_all_files(filename)
    if candidates:
        best_match = None
        best_similarity = -1
        best_matches = []
        
        for candidate_path, candidate_content in candidates:
            similarity = calculate_path_similarity(target_path, candidate_path)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = (candidate_path, candidate_content)
                best_matches = [(candidate_path, candidate_content)]
            elif similarity == best_similarity:
                # 相似度相同，添加到候选列表
                best_matches.append((candidate_path, candidate_content))
        
        # 如果有多个最佳匹配，产生冲突
        if len(best_matches) > 1:
            return 'conflict', f"Multiple candidates with same similarity: {best_matches}"
        elif best_match:
            return 'match', best_match
    
    # Step 3: 特殊处理 __init__.py
    if filename == '__init__.py':
        return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"
    
    # Step 4: 脚手架
    return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"

def unpack_project(
    source_file: Path,
    output_dir: Path,
    force: bool = False,
    structure_only: bool = False,
    tree_path: Optional[Path] = None,
    dry_run: bool = False
) -> Dict[str, any]:
    """
    执行还原操作
    支持重构模式和试运行模式
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    # 尝试不同的编码读取文件
    content = ""
    for encoding in ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']:
        try:
            content = source_file.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    
    if not content:
        raise UnicodeDecodeError(f"无法解码文件: {source_file}")
    
    files = parse_document(content)
    
    # 创建内容池
    content_pool = ContentPool(files)
    
    # 检查是否为重构模式
    refactor_mode = tree_path is not None and tree_path.exists()
    
    if refactor_mode:
        # 重构模式：使用结构树
        tree_content = tree_path.read_text(encoding='utf-8')
        target_paths = parse_layout_tree(tree_content)
        
        stats = {
            "create": 0, "match": 0, "scaffold": 0, "conflict": 0,
            "skipped": 0, "failed": 0
        }
        
        # 检查目标目录是否为空
        if not dry_run and not force and any(output_dir.iterdir()):
            raise ValueError(f"目标目录 {output_dir} 不为空，请使用 --force 强制覆盖")
        
        for target_path in target_paths:
            status, content_or_error = resolve_target(target_path, content_pool)
            
            try:
                if dry_run:
                    # 试运行模式：只记录不写入
                    if status == 'match':
                        stats["match"] += 1
                    elif status == 'scaffold':
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        stats["conflict"] += 1
                else:
                    # 实际执行
                    if status == 'match':
                        written = safe_write_file(output_dir, target_path, content_or_error, force=force)
                        if written:
                            stats["match"] += 1
                        else:
                            stats["skipped"] += 1
                    elif status == 'scaffold':
                        # 创建脚手架文件
                        scaffold_path = output_dir / target_path
                        scaffold_path.parent.mkdir(parents=True, exist_ok=True)
                        scaffold_path.write_text(content_or_error, encoding='utf-8')
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        # 创建冲突文件
                        conflict_path = output_dir / f"{target_path}.CONFLICT"
                        conflict_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # 获取所有候选路径
                        candidates = content_pool.get_all_files(Path(target_path).name)
                        conflict_content = f"# Conflict resolution for {target_path}\n"
                        conflict_content += f"# Original candidates:\n"
                        for candidate_path, _ in candidates:
                            conflict_content += f"# - {candidate_path}\n"
                        
                        conflict_path.write_text(conflict_content, encoding='utf-8')
                        stats["conflict"] += 1
                        
            except Exception as e:
                if dry_run:
                    stats["failed"] += 1
                else:
                    print(f"❌ Error processing {target_path}: {e}")
                    stats["failed"] += 1
        
        return stats
    else:
        # 普通模式：直接还原
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


# </ctx1:file>

# <ctx1:file path="src/context1/core/walker.py">
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
# </ctx1:file>

# <ctx1:file path="src/context1/utils/fs.py">
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
    使用 pathlib 的相对_to() 方法确保 target 在 base 目录下
    """
    try:
        base = Path(base_dir).resolve()
        
        # 允许 target_path 是绝对路径或相对路径
        if os.path.isabs(target_path):
            target = Path(target_path).resolve()
        else:
            target = (base / target_path).resolve()
            
        # 使用 pathlib 的相对_to() 方法进行安全检查
        # 如果 target 不在 base 目录下，会抛出 ValueError
        try:
            relative = target.relative_to(base)
            # 检查相对路径是否包含向上导航的组件
            return not any(part == '..' for part in relative.parts)
        except ValueError:
            # target 不在 base 目录下
            return False
            
    except Exception:
        return False

def is_binary_file(file_path: Path, chunk_size: int = 1024) -> bool:
    """
    通过读取前 chunk_size 字节检查是否包含 NULL 字节来判断是否为二进制文件
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
            
            # 如果文件为空，则不是二进制文件
            if not chunk:
                return False
            
            # 检查是否包含 NULL 字节
            has_null = b'\x00' in chunk
            
            # 如果包含 NULL 字节，检查是否可能是 UTF-16 编码的文本
            if has_null:
                # 检查是否是 UTF-16 BOM
                if chunk.startswith(b'\xff\xfe') or chunk.startswith(b'\xfe\xff'):
                    # 可能是 UTF-16 编码的文本，不是二进制文件
                    return False
                
                # 检查是否是纯文本的 UTF-16 编码（每个字符后跟 NULL 字节）
                # 如果大部分字符都是字母数字，并且 NULL 字节规律分布，可能是 UTF-16 文本
                null_positions = [i for i, b in enumerate(chunk) if b == 0]
                if len(null_positions) > 0:
                    # 检查 NULL 字节是否规律分布（每2个字节一个NULL）
                    is_utf16_pattern = True
                    for i in range(1, len(null_positions)):
                        if null_positions[i] - null_positions[i-1] != 2:
                            is_utf16_pattern = False
                            break
                    
                    # 如果大部分内容都是可打印字符，可能是 UTF-16 文本
                    printable_count = sum(1 for b in chunk if 32 <= b <= 126)
                    if is_utf16_pattern and printable_count > len(chunk) * 0.3:
                        return False
            
            # 如果包含 NULL 字节且不是 UTF-16 文本，则是二进制文件
            if has_null:
                return True
            
            # 如果没有 NULL 字节，则不是二进制文件
            return False
            
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
# </ctx1:file>

# <ctx1:file path="test_cli.py">
#!/usr/bin/env python3
import sys
from pathlib import Path
# 确保引用的是本地 src 目录
sys.path.insert(0, str(Path.cwd() / 'src'))

from context1.cli import app
from typer.main import get_command

# 获取底层的 Click 命令对象
click_cmd = get_command(app)

print("✅ App loaded successfully!")
print(f"Available commands: {list(click_cmd.commands.keys())}")

# 检查 pack 命令的参数
if 'pack' in click_cmd.commands:
    pack_cmd = click_cmd.commands['pack']
    print("\n🔍 Checking 'pack' command parameters:")
    
    found_new_params = False
    for param in pack_cmd.params:
        # param.name 是参数名，param.opts 是命令行标志 (如 --sort)
        print(f"  - {param.name} {param.opts}")
        if param.name in ['sort', 'format']:
            found_new_params = True
            
    if found_new_params:
        print("\n✨ SUCCESS: New parameters 'sort' and 'format' detected!")
    else:
        print("\n❌ FAIL: New parameters not found.")
else:
    print("Pack command not found")
# </ctx1:file>

# <ctx1:file path="test_dslpp/__init__.py">
# 初始化文件
@Role: Foundation
@Responsibility: 包初始化和基础配置
# </ctx1:file>

# <ctx1:file path="test_dslpp/test_user.py">
# 测试文件
@Role: Test
@Responsibility: 用户模块测试
import unittest

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = {"name": "Test", "email": "test@example.com"}
        self.assertEqual(user["name"], "Test")
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_bhv.py">
# 行为层
@Role: Behavior
@Responsibility: 用户行为逻辑
class UserBehavior:
    def validate_email(self, email):
        return "@" in email and "." in email
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_c.py">
# 控制器层
@Role: Controller
@Responsibility: 用户控制器逻辑
from .user_i import UserServiceInterface

class UserController(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created with email {email}"
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_cmd.py">
# 命令层
@Role: Commander
@Responsibility: 用户命令处理
class UserCommand:
    def execute(self, user_data):
        return f"Command executed for user: {user_data['name']}"
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_d.py">
# 数据访问层
@Role: Data
@Responsibility: 用户数据访问逻辑
class UserData:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Test User"}
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_ent.py">
# 实体类文件
@Role: Entity
@Responsibility: 用户数据实体定义
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_i.py">
# 接口层
@Role: Interface
@Responsibility: 用户服务接口定义
from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, name, email):
        pass
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_s.py">
# 服务层
@Role: Service
@Responsibility: 用户服务实现
from .user_i import UserServiceInterface

class UserService(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created successfully"
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_stg.py">
# 策略层
@Role: Strategy
@Responsibility: 用户策略定义
class UserStrategy:
    def process_user(self, user_data):
        return f"Processing user: {user_data['name']}"
# </ctx1:file>

# <ctx1:file path="test_dslpp/user_u.py">
# 工具层
@Role: Utility
@Responsibility: 用户相关工具函数
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# </ctx1:file>

# <ctx1:file path="tests/test_packer.py">
"""
单元测试 - Packer 模块
测试 DS-LPP 排序、Python Bundle 格式生成、元数据提取等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.config import Config, OutputFormat, SortStrategy, DEFAULT_DSLPP_WEIGHTS
from context1.core.packer import (
    calculate_dslpp_weight, 
    sort_files, 
    extract_metadata, 
    generate_layout_tree,
    generate_content
)


class TestDSLPPSorting:
    """测试 DS-LPP 排序功能"""
    
    def test_calculate_dslpp_weight_init(self):
        """测试 __init__.py 权重"""
        weight = calculate_dslpp_weight("__init__.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 0
    
    def test_calculate_dslpp_weight_entity(self):
        """测试实体文件权重"""
        weight = calculate_dslpp_weight("user_entity.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 10
    
    def test_calculate_dslpp_weight_command(self):
        """测试命令文件权重"""
        weight = calculate_dslpp_weight("search_cmd.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 40
    
    def test_calculate_dslpp_weight_test(self):
        """测试文件权重"""
        weight = calculate_dslpp_weight("test_user_service.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 99
    
    def test_calculate_dslpp_weight_default(self):
        """测试默认权重"""
        weight = calculate_dslpp_weight("unknown_file.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 50
    
    def test_sort_files_dslpp(self):
        """测试 DS-LPP 排序"""
        files = [
            Path("test_user_service.py"),
            Path("__init__.py"),
            Path("user_entity.py"),
            Path("search_cmd.py"),
            Path("user_service.py")
        ]
        
        config = Config(
            project_root=Path("/test"),
            sort_strategy=SortStrategy.DSLPP,
            dslpp_weights=DEFAULT_DSLPP_WEIGHTS
        )
        
        sorted_files = sort_files(files, config)
        
        # 验证排序结果
        assert str(sorted_files[0]) == "__init__.py"
        assert str(sorted_files[1]) == "user_entity.py"
        assert str(sorted_files[2]) == "user_service.py"
        assert str(sorted_files[3]) == "search_cmd.py"
        assert str(sorted_files[4]) == "test_user_service.py"


class TestMetadataExtraction:
    """测试元数据提取功能"""
    
    def test_extract_metadata_with_role(self):
        """测试提取角色信息"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
# @Role: Commander
# @Responsibility: 搜索入口
def search():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == "Commander"
            assert metadata["responsibility"] == "搜索入口"
        finally:
            temp_file.unlink()
    
    def test_extract_metadata_without_role(self):
        """测试无角色信息的文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
def simple_function():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == ""
            assert metadata["responsibility"] == ""
        finally:
            temp_file.unlink()


class TestPythonBundle:
    """测试 Python Bundle 格式生成"""
    
    def test_generate_content_python_bundle(self):
        """测试 Python Bundle 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.PYTHON_BUNDLE,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Python Bundle 格式
            assert "#!/usr/bin/env python3" in content
            assert "# CTX1_BUNDLE_VERSION: 0.2.0" in content
            assert '# <ctx1:file path="test.py">' in content
            assert "# </ctx1:file>" in content
            assert 'print("Hello, World!")' in content
    
    def test_generate_content_markdown(self):
        """测试 Markdown 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.MARKDOWN,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Markdown 格式
            assert "--- 文件: test.py ---" in content
            assert 'print("Hello, World!")' in content


class TestLayoutTree:
    """测试布局蓝图生成"""
    
    def test_generate_layout_tree(self):
        """测试布局蓝图生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            (temp_path / "src").mkdir()
            (temp_path / "tests").mkdir()
            
            (temp_path / "src" / "main.py").write_text("def main(): pass")
            (temp_path / "src" / "utils.py").write_text("def util(): pass")
            (temp_path / "tests" / "test_main.py").write_text("def test_main(): pass")
            (temp_path / "README.md").write_text("# Test Project")
            
            files = [
                temp_path / "src" / "main.py",
                temp_path / "src" / "utils.py",
                temp_path / "tests" / "test_main.py",
                temp_path / "README.md"
            ]
            
            tree_content = generate_layout_tree(files, temp_path)
            
            # 验证树格式
            assert "src/" in tree_content
            assert "tests/" in tree_content
            assert "main.py" in tree_content
            assert "utils.py" in tree_content
            assert "test_main.py" in tree_content
            assert "README.md" in tree_content


if __name__ == "__main__":
    pytest.main([__file__])
# </ctx1:file>

# <ctx1:file path="tests/test_safety.py">
"""
测试文件系统安全性 - 核心职责：测试路径安全检查、Zip Slip 防护
"""
import pytest
import tempfile
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.utils.fs import is_safe_path

def test_is_safe_path_basic():
    """测试基本的安全路径检查"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 同一目录下的文件应该是安全的
        assert is_safe_path(base, "file.txt") == True
        assert is_safe_path(base, "subdir/file.txt") == True
        
        # 父目录应该是安全的
        assert is_safe_path(base, "..") == False
        assert is_safe_path(base, "../other") == False

def test_is_safe_path_absolute():
    """测试绝对路径的安全性"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 绝对路径指向同一目录应该是安全的
        abs_path = base / "file.txt"
        assert is_safe_path(base, str(abs_path)) == True
        
        # 绝对路径指向子目录应该是安全的
        subdir = base / "subdir"
        subdir.mkdir()
        abs_subdir_path = subdir / "file.txt"
        assert is_safe_path(base, str(abs_subdir_path)) == True
        
        # 绝对路径指向完全不同的目录应该是危险的
        with tempfile.TemporaryDirectory() as other_temp_dir:
            other_base = Path(other_temp_dir)
            other_abs_path = other_base / "file.txt"
            assert is_safe_path(base, str(other_abs_path)) == False

def test_is_safe_path_zip_slip_attack():
    """测试 Zip Slip 攻击防护"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 测试 Zip Slip 攻击模式
        attack_paths = [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "subdir/../../../etc/passwd",
            "subdir/..\\..\\..\\windows\\system32\\config\\sam",
        ]
        
        for attack_path in attack_paths:
            assert is_safe_path(base, attack_path) == False, f"Path '{attack_path}' should be blocked"

def test_is_safe_path_edge_cases():
    """测试边界情况"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 空路径
        assert is_safe_path(base, "") == True
        
        # 点路径
        assert is_safe_path(base, ".") == True
        
        # 相对路径到自身
        assert is_safe_path(base, "./file.txt") == True
        
        # 多层相对路径
        assert is_safe_path(base, "a/b/c/file.txt") == True

def test_is_safe_path_with_symlinks():
    """测试符号链接处理（如果支持）"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 创建一个符号链接指向外部目录
        try:
            external_file = Path(temp_dir) / "external.txt"
            external_file.write_text("test")
            
            symlink_path = base / "symlink"
            symlink_path.symlink_to(external_file)
            
            # 符号链接指向外部文件应该是安全的（如果解析后仍在 base 内）
            assert is_safe_path(base, "symlink") == True
            
        except (OSError, NotImplementedError):
            # 如果不支持符号链接，跳过测试
            pytest.skip("Symbolic links not supported on this platform")

if __name__ == "__main__":
    pytest.main([__file__])
# </ctx1:file>

# <ctx1:file path="tests/test_unpacker.py">
"""
单元测试 - Unpacker 模块
测试文档解析、智能内容池、结构树驱动注入等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.unpacker import (
    parse_document,
    ContentPool,
    parse_layout_tree,
    calculate_path_similarity,
    resolve_target,
    unpack_project
)


class TestDocumentParsing:
    """测试文档解析功能"""
    
    def test_parse_markdown_format(self):
        """测试 Markdown 格式解析"""
        content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_xml_format(self):
        """测试 XML 格式解析"""
        content = """<document path="src/main.py">
def main():
    print("Hello, World!")
</document>

<document path="src/utils.py">
def util():
    pass
</document>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_python_bundle_format(self):
        """测试 Python Bundle 格式解析"""
        content = """#!/usr/bin/env python3
# CTX1_BUNDLE_VERSION: 0.2.0

# <ctx1:file path="src/main.py">
def main():
    print("Hello, World!")
# </ctx1:file>

# <ctx1:file path="src/utils.py">
def util():
    pass
# </ctx1:file>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'


class TestContentPool:
    """测试智能内容池功能"""
    
    def test_content_pool_creation(self):
        """测试内容池创建"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'src/utils.py', 'content': 'def util(): pass'},
            {'path': 'tests/test_main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        assert len(pool.pool) == 3
        assert 'main.py' in pool.pool
        assert 'utils.py' in pool.pool
        assert 'test_main.py' in pool.pool
    
    def test_content_pool_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        result = pool.get_file('main.py')
        
        assert result is not None
        assert result[0] == 'src/main.py'
        assert result[1] == 'def main(): pass'
    
    def test_content_pool_multiple_files(self):
        """测试多文件同名情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试获取所有同名文件
        all_files = pool.get_all_files('main.py')
        assert len(all_files) == 2
        assert all_files[0][0] == 'src/main.py'
        assert all_files[1][0] == 'tests/main.py'
        
        # 测试唯一匹配（应该返回 None）
        unique = pool.get_file('main.py')
        assert unique is None


class TestLayoutTree:
    """测试布局树功能"""
    
    def test_parse_layout_tree(self):
        """测试布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils.py
tests/
    test_main.py
    test_utils.py
README.md
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 5
        assert 'src/main.py' in target_paths
        assert 'src/utils.py' in target_paths
        assert 'tests/test_main.py' in target_paths
        assert 'tests/test_utils.py' in target_paths
        assert 'README.md' in target_paths
    
    def test_parse_layout_tree_with_directories(self):
        """测试包含目录的布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils/
        helper.py
tests/
    test_main.py
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 3
        assert 'src/main.py' in target_paths
        assert 'src/utils/helper.py' in target_paths
        assert 'tests/test_main.py' in target_paths


class TestPathSimilarity:
    """测试路径相似度计算"""
    
    def test_path_similarity_same_path(self):
        """测试相同路径"""
        similarity = calculate_path_similarity('src/main.py', 'src/main.py')
        assert similarity == 2  # 'src' + 'main.py'
    
    def test_path_similarity_common_prefix(self):
        """测试公共前缀"""
        similarity = calculate_path_similarity('src/main.py', 'src/utils.py')
        assert similarity == 1  # 'src'
    
    def test_path_similarity_different_prefix(self):
        """测试不同前缀"""
        similarity = calculate_path_similarity('src/main.py', 'tests/main.py')
        assert similarity == 0  # 无公共部分
    
    def test_path_similarity_nested(self):
        """测试嵌套路径"""
        similarity = calculate_path_similarity('src/utils/helper.py', 'src/utils/main.py')
        assert similarity == 2  # 'src' + 'utils'


class TestTargetResolution:
    """测试目标路径解析"""
    
    def test_resolve_target_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        status, content = resolve_target('src/main.py', pool)
        
        assert status == 'match'
        assert content == ('src/main.py', 'def main(): pass')
    
    def test_resolve_target_path_similarity(self):
        """测试路径相似度匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试匹配 src/main.py
        status, content = resolve_target('src/main.py', pool)
        assert status == 'match'
        assert content[0] == 'src/main.py'
        
        # 测试匹配 tests/main.py
        status, content = resolve_target('tests/main.py', pool)
        assert status == 'match'
        assert content[0] == 'tests/main.py'
    
    def test_resolve_target_conflict(self):
        """测试冲突情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试冲突（两个路径相似度相同）
        status, content = resolve_target('other/main.py', pool)
        assert status == 'conflict'
        assert 'Conflict resolution' in content
    
    def test_resolve_target_scaffold(self):
        """测试脚手架情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试不存在的文件
        status, content = resolve_target('src/new_file.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content
    
    def test_resolve_target_init_special_case(self):
        """测试 __init__.py 特殊处理"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试 __init__.py 特殊处理
        status, content = resolve_target('src/__init__.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content


class TestUnpackProject:
    """测试解包项目功能"""
    
    def test_unpack_project_normal_mode(self):
        """测试普通模式解包"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 解包到新目录
            output_dir = temp_path / "output"
            stats = unpack_project(bundle_file, output_dir)
            
            # 验证结果
            assert stats['success'] == 2
            assert stats['skipped'] == 0
            assert stats['failed'] == 0
            
            # 验证文件是否正确创建
            assert (output_dir / "src" / "main.py").exists()
            assert (output_dir / "src" / "utils.py").exists()
    
    def test_unpack_project_dry_run(self):
        """测试试运行模式"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 创建结构树
            tree_content = """src/
    main.py
    new_file.py"""
            
            tree_file = temp_path / "layout.tree"
            tree_file.write_text(tree_content)
            
            # 试运行
            output_dir = temp_path / "output"
            stats = unpack_project(
                bundle_file, 
                output_dir, 
                tree_path=tree_file,
                dry_run=True
            )
            
            # 验证结果
            assert stats['match'] == 1  # main.py 匹配
            assert stats['scaffold'] == 1  # new_file.py 脚手架
            assert stats['conflict'] == 0
            assert stats['failed'] == 0
            
            # 验证文件未实际创建
            assert not output_dir.exists()


if __name__ == "__main__":
    pytest.main([__file__])
# </ctx1:file>

# <ctx1:file path="tests/test_walker.py">
"""
测试文件扫描器 - 核心职责：测试文件过滤、Gitignore集成、策略过滤
"""
import pytest
import tempfile
import json
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.core.config import Config
from context1.core.walker import FileWalker

def create_test_files(base_dir: Path):
    """创建测试文件结构"""
    # 创建各种类型的文件
    (base_dir / "main.py").write_text("# Main file")
    (base_dir / "test.py").write_text("# Test file")
    (base_dir / "data.json").write_text('{"key": "value"}')
    (base_dir / "README.md").write_text("# README")
    (base_dir / "config.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # 创建二进制文件
    (base_dir / "binary.exe").write_bytes(b"\x00\x01\x02\x03")
    (base_dir / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    
    # 创建锁定文件
    (base_dir / "package-lock.json").write_text("{}")
    (base_dir / "yarn.lock").write_text("# yarn lock")
    (base_dir / "poetry.lock").write_text("# poetry lock")
    
    # 创建子目录
    subdir = base_dir / "src"
    subdir.mkdir()
    (subdir / "module.py").write_text("# Module file")
    (subdir / "test.lock").write_text("# Test lock file")
    
    # 创建 .gitignore
    (base_dir / ".gitignore").write_text("""
__pycache__/
*.pyc
*.pyo
*.pyd
*.class
*.lock
.venv/
venv/
env/
node_modules/
""")

def test_walker_excludes_lock_files():
    """测试 walker 是否正确排除 .lock 文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            always_exclude=["*.lock"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有 .lock 文件
        lock_files = [f for f in files if f.name.endswith('.lock')]
        assert len(lock_files) == 0, f"Found lock files that should be excluded: {lock_files}"

def test_walker_excludes_binary_files():
    """测试 walker 是否正确排除二进制文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            binary_extensions=[".exe", ".png"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有二进制文件
        binary_files = [f for f in files if f.suffix.lower() in ['.exe', '.png']]
        assert len(binary_files) == 0, f"Found binary files that should be excluded: {binary_files}"

def test_walker_respects_gitignore():
    """测试 walker 是否正确遵循 .gitignore"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            use_gitignore=True,
            always_exclude=[]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否排除了 .gitignore 中指定的文件
        file_names = [f.name for f in files]
        
        # 应该排除的文件
        excluded_patterns = ["__pycache__", "*.pyc", "*.pyo", "*.pyd", "*.lock", ".venv", "venv", "env", "node_modules"]
        
        # 检查是否有被排除的文件
        for pattern in excluded_patterns:
            if pattern.endswith('*'):
                # 处理通配符
                prefix = pattern[:-1]
                matching_files = [f for f in file_names if f.startswith(prefix)]
                assert len(matching_files) == 0, f"Found files matching pattern '{pattern}': {matching_files}"
            else:
                assert pattern not in file_names, f"Found excluded file: {pattern}"

def test_walker_smart_strategy():
    """测试 smart 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="smart"
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该找到所有非二进制、非锁定、非排除的文件
        expected_files = ["main.py", "test.py", "data.json", "README.md", "config.toml"]
        file_names = [f.name for f in files]
        
        for expected_file in expected_files:
            assert expected_file in file_names, f"Expected file '{expected_file}' not found in scan results"

def test_walker_blacklist_strategy():
    """测试 blacklist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="blacklist"
        )
        
        # 创建黑名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        blacklist_file = ctx_dir / "blacklist.json"
        blacklist_data = {
            "patterns": ["*.json", "src/"]
        }
        with open(blacklist_file, 'w') as f:
            json.dump(blacklist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该排除 .json 文件和 src 目录
        file_names = [f.name for f in files]
        relative_paths = [str(f.relative_to(base_dir)) for f in files]
        
        # 检查是否排除了 .json 文件
        json_files = [f for f in file_names if f.endswith('.json')]
        assert len(json_files) == 0, f"Found JSON files that should be blacklisted: {json_files}"
        
        # 检查是否排除了 src 目录
        src_files = [f for f in relative_paths if f.startswith('src/')]
        assert len(src_files) == 0, f"Found src directory files that should be blacklisted: {src_files}"

def test_walker_whitelist_strategy():
    """测试 whitelist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="whitelist"
        )
        
        # 创建白名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        whitelist_file = ctx_dir / "whitelist.json"
        whitelist_data = {
            "patterns": ["*.py", "README.md"]
        }
        with open(whitelist_file, 'w') as f:
            json.dump(whitelist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该只包含 .py 文件和 README.md
        file_names = [f.name for f in files]
        
        # 检查是否只包含白名单文件
        for file_name in file_names:
            assert file_name.endswith('.py') or file_name == 'README.md', f"Found non-whitelisted file: {file_name}"

def test_walker_empty_directory():
    """测试空目录的扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        
        # 创建配置
        config = Config(project_root=base_dir)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该返回空列表
        assert len(files) == 0, f"Expected no files in empty directory, found: {files}"

if __name__ == "__main__":
    pytest.main([__file__])
# </ctx1:file>

# <ctx1:file path="uv.lock">
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
version = "0.2.0"
source = { virtual = "." }
dependencies = [
    { name = "pathspec" },
    { name = "pyperclip" },
    { name = "pytest" },
    { name = "rich" },
    { name = "typer" },
]

[package.metadata]
requires-dist = [
    { name = "pathspec", specifier = ">=0.12.1" },
    { name = "pyperclip", specifier = ">=1.11.0" },
    { name = "pytest", specifier = ">=9.0.1" },
    { name = "rich", specifier = ">=14.2.0" },
    { name = "typer", specifier = ">=0.20.0" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
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
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
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
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
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
name = "pytest"
version = "9.0.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/07/56/f013048ac4bc4c1d9be45afd4ab209ea62822fb1598f40687e6bf45dcea4/pytest-9.0.1.tar.gz", hash = "sha256:3e9c069ea73583e255c3b21cf46b8d3c56f6e3a1a8f6da94ccb0fcf57b9d73c8", size = 1564125, upload-time = "2025-11-12T13:05:09.333Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/8b/6300fb80f858cda1c51ffa17075df5d846757081d11ab4aa35cef9e6258b/pytest-9.0.1-py3-none-any.whl", hash = "sha256:67be0030d194df2dfa7b556f2e56fb3c3315bd5c8822c6951162b92b32ce7dad", size = 373668, upload-time = "2025-11-12T13:05:07.379Z" },
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

# </ctx1:file>
