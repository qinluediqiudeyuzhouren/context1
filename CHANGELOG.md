# 更新日志

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

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