---
title: "TinyMD - 轻量 Markdown 解析器"
date: 2025-05-10
description: "用 Rust 从零实现的 Markdown 解析器，支持 CommonMark 规范的核心子集。"
tags: ["Rust", "解析器", "编译原理", "CLI"]
categories: ["工具库"]
cover:
  image: "images/markdown-parser.svg"
  alt: "TinyMD 架构图"
  relative: false
weight: 3
---

## 项目简介

TinyMD 是一个用 Rust 编写的轻量级 Markdown 解析器。目标是理解编译原理中词法分析和语法分析的核心概念，同时产出一个可用的工具。

## 技术栈

- **语言**: Rust
- **解析策略**: 手写递归下降解析器
- **输出**: HTML / ANSI 终端渲染

## 支持的语法

| 语法 | 状态 |
|------|------|
| 标题 (h1-h6) | ✅ |
| 粗体 / 斜体 | ✅ |
| 代码块 | ✅ |
| 链接 / 图片 | ✅ |
| 列表（有序/无序） | ✅ |
| 表格 | 🚧 进行中 |
| 脚注 | ❌ 计划中 |

## 架构

```
输入 Markdown 文本
    ↓
[Lexer] → Token 流
    ↓
[Parser] → AST
    ↓
[Renderer] → HTML / ANSI
```

## 性能

在 10MB 的 Markdown 文件上：
- **TinyMD**: ~120ms
- **pulldown-cmark**: ~45ms
- **comrak**: ~80ms

还有优化空间，但作为学习项目已经不错了。

## 状态

🟡 核心功能完成，表格支持开发中。
