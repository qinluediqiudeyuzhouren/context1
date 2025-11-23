# Context1

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/yourusername/context1)

**Context1** - 在您的代码库和 LLM 之间架设桥梁的强大 CLI 工具

## 📖 简介

Context1 是一个专为开发者设计的命令行工具，能够将您的项目代码打包成单一文本上下文，为大型语言模型（LLM）提供完整的代码上下文信息。它支持智能文件过滤、目录树生成、配置管理和安全路径检查，是您与 AI 协作开发的得力助手。

## ✨ 主要特性

- 🚀 **智能文件过滤** - 支持 smart、whitelist、blacklist 三种过滤策略
- 🌳 **ASCII 目录树** - 生成类似 Linux `tree` 命令的目录结构
- 🔒 **安全防护** - 内置 Zip Slip 攻击防护机制
- 📊 **项目统计** - 提供文件数量、大小和 Token 估算
- 🎨 **美观界面** - 使用 Rich 库提供丰富的终端输出
- ⚙️ **灵活配置** - 支持项目级、用户级和默认配置
- 🧪 **全面测试** - 包含完整的单元测试套件

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
- `-v, --verbose`: 显示详细日志

**示例：**
```bash
# 基本打包
context1 pack .

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