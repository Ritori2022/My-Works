---
title: "Quantum Chat - 量子聊天应用"
date: 2025-12-15
description: "一个基于 WebSocket 的实时聊天应用，支持端到端加密和消息自毁功能。"
tags: ["Web", "TypeScript", "WebSocket", "加密"]
categories: ["Web 应用"]
cover:
  image: "images/quantum-chat.svg"
  alt: "Quantum Chat 截图"
  relative: false
weight: 1
---

## 项目简介

Quantum Chat 是一个注重隐私的实时聊天应用。消息通过端到端加密传输，支持设定消息自毁时间。

## 技术栈

- **前端**: React + TypeScript
- **后端**: Node.js + Express
- **通信**: WebSocket (ws)
- **加密**: libsodium

## 核心功能

1. **端到端加密** - 使用 X25519 密钥交换 + XChaCha20-Poly1305
2. **消息自毁** - 可设置 30秒 / 5分钟 / 1小时 自动销毁
3. **匿名房间** - 无需注册，生成临时身份
4. **代码高亮** - 支持发送代码片段并自动高亮

## 项目截图

![聊天界面](/images/quantum-chat.svg)

## 状态

🟢 已完成 MVP，正在优化移动端体验。

## 链接

- [GitHub 仓库](https://github.com/example/quantum-chat)（示例链接）
