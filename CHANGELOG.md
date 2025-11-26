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