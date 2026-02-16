---
title: "SoundWave - 音乐可视化器"
date: 2026-01-28
description: "基于 Web Audio API 的实时音乐可视化器，支持多种视觉效果和自定义配色。"
tags: ["Web Audio", "WebGL", "JavaScript", "可视化"]
categories: ["创意编程"]
cover:
  image: "images/music-visualizer.svg"
  alt: "SoundWave 效果图"
  relative: false
weight: 1
---

## 项目简介

SoundWave 是一个在浏览器中运行的实时音乐可视化器。它通过 Web Audio API 分析音频频谱数据，使用 WebGL 渲染炫酷的视觉效果。

## 技术栈

- **音频分析**: Web Audio API (AnalyserNode + FFT)
- **渲染**: WebGL 2.0 + 自定义 Shader
- **框架**: 无框架，纯 JavaScript

## 可视化模式

### 🌊 波形模式
实时显示音频波形，颜色随振幅变化。

### 🎯 频谱环
将频谱数据映射到极坐标环上，低频在内圈，高频在外圈。

### ✨ 粒子场
音频驱动的粒子系统，节拍触发粒子爆发效果。

### 🌀 隧道效果
根据音量控制隧道的缩放速度，频谱决定截面形状。

## 效果展示

![可视化效果](/images/music-visualizer.svg)

## 状态

🟢 四种模式均已实现，正在添加麦克风输入支持。

## 链接

- [在线演示](https://example.com/soundwave)（示例链接）
