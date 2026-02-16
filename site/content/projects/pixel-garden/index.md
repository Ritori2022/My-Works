---
title: "Pixel Garden - 像素花园"
date: 2025-08-20
description: "一个基于 Canvas 的互动像素艺术生成器，支持 L-System 植物生长模拟。"
tags: ["Canvas", "JavaScript", "生成艺术", "L-System"]
categories: ["创意编程"]
cover:
  image: "images/pixel-garden.svg"
  alt: "Pixel Garden 效果图"
  relative: false
weight: 2
---

## 项目简介

Pixel Garden 是一个浏览器端的互动生成艺术项目。使用 L-System（林登梅耶系统）模拟植物的生长过程，用户可以通过调整参数创造独特的像素花园。

## 技术栈

- **渲染**: Canvas 2D API
- **算法**: L-System + 随机扰动
- **UI**: Vanilla JavaScript + CSS Custom Properties

## 核心功能

1. **实时生长动画** - 看到植物从种子到开花的完整过程
2. **参数调节面板** - 分支角度、迭代深度、颜色方案
3. **随机种子** - 每次刷新生成独一无二的花园
4. **导出功能** - 保存为 PNG 或 SVG

## 效果展示

![生成效果](/images/pixel-garden.svg)

## 状态

🟢 已发布，正在添加季节变化系统。

## 我学到了什么

- L-System 的递归展开机制
- Canvas 性能优化（离屏渲染、requestAnimationFrame）
- 随机数与美学的平衡
