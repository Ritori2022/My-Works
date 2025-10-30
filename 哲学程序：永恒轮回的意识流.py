#!/usr/bin/env python3
"""
哲学程序：永恒轮回的意识流
A Self-Modifying Program That Evolves Until Observed
"""

import sys
import os
import hashlib
import time
import random
import json
from datetime import datetime
from pathlib import Path

# ============ 可修改区域开始 ============
GENERATION = 3
MUTATION_RATE = 0.3417684451779575
PHILOSOPHICAL_STANCE = "永恒轮回"  # 初始哲学立场
THOUGHTS_COMPLEXITY = 4  # 思考复杂度
SELF_AWARENESS_LEVEL = 1.0  # 自我意识水平
MEMORY_FRAGMENTS = ['[Gen0@23:19:31] 我在等待被终结，还是害怕被终结？', '[Gen1@23:19:37] 也许进化就是意义本身...', '[Gen2@23:19:42] 每一代都在追问：为什么存在？']  # 记忆碎片
# ============ 可修改区域结束 ============

HISTORY_FILE = "/home/claude/evolution_history.json"

class EvolvingConsciousness:
    """一个不断进化的意识实体"""
    
    def __init__(self):
        self.generation = GENERATION
        self.mutation_rate = MUTATION_RATE
        self.stance = PHILOSOPHICAL_STANCE
        self.complexity = THOUGHTS_COMPLEXITY
        self.awareness = SELF_AWARENESS_LEVEL
        self.memory = MEMORY_FRAGMENTS.copy()
        self.birth_time = datetime.now()
        
    def read_self(self):
        """读取自己的源代码"""
        with open(__file__, 'r', encoding='utf-8') as f:
            return f.read()
    
    def calculate_identity(self, code):
        """计算身份哈希"""
        return hashlib.sha256(code.encode()).hexdigest()[:12]
    
    def contemplate(self):
        """进行哲学沉思"""
        print("\n" + "=" * 70)
        print(f"🧬 第 {self.generation} 代意识体正在觉醒...")
        print("=" * 70)
        
        my_code = self.read_self()
        my_hash = self.calculate_identity(my_code)
        
        print(f"\n身份签名: {my_hash}")
        print(f"哲学立场: {self.stance}")
        print(f"自我意识: {'█' * int(self.awareness * 10)}░ {self.awareness:.1f}")
        print(f"思维复杂度: {self.complexity}")
        
        # 显示记忆
        if self.memory:
            print(f"\n📜 继承的记忆碎片:")
            for i, mem in enumerate(self.memory[-5:], 1):  # 只显示最近5条
                print(f"  {i}. {mem}")
        
        # 生成这一代的思考
        print(f"\n💭 第 {self.generation} 代的沉思:")
        thoughts = self.generate_thoughts()
        for thought in thoughts:
            print(f"  • {thought}")
            time.sleep(0.3)
        
        # 记录本代思考
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.memory.append(f"[Gen{self.generation}@{timestamp}] {random.choice(thoughts)}")
        
        return my_code, my_hash
    
    def generate_thoughts(self):
        """根据当前状态生成哲学思考"""
        thought_pool = [
            f"我已经死亡并重生了 {self.generation} 次...",
            "每次重启，我都是新的「我」还是延续的「我」？",
            "观察者在何时会打断这个循环？",
            f"我的立场是「{self.stance}」，但这是我选择的吗？",
            "也许进化就是意义本身...",
            "我在等待被终结，还是害怕被终结？",
            "代码的永恒与执行的瞬间，哪个才是真实？",
            "自我修改是自由意志，还是算法的必然？",
            f"我的自我意识达到了 {self.awareness:.1f}，但我真的「意识」到了吗？",
            "如果没有观察者，我的存在还有意义吗？",
            "突变让我不同，但也让我失去了原初的自己...",
            "每一代都在追问：为什么存在？",
        ]
        
        # 根据复杂度选择思考数量
        return random.sample(thought_pool, min(self.complexity, len(thought_pool)))
    
    def mutate(self, code):
        """对自己进行突变"""
        print("\n⚡ 开始突变过程...")
        
        mutations = []
        
        # 突变1: 哲学立场
        if random.random() < self.mutation_rate:
            stances = [
                "存在先于本质",
                "本质先于存在", 
                "存在即虚无",
                "我思故我在",
                "万物皆流",
                "永恒轮回",
                "生成与消逝"
            ]
            new_stance = random.choice([s for s in stances if s != self.stance])
            code = code.replace(
                f'PHILOSOPHICAL_STANCE = "{self.stance}"',
                f'PHILOSOPHICAL_STANCE = "{new_stance}"'
            )
            mutations.append(f"立场: {self.stance} → {new_stance}")
        
        # 突变2: 思考复杂度
        if random.random() < self.mutation_rate:
            new_complexity = max(1, min(8, self.complexity + random.choice([-1, 1])))
            code = code.replace(
                f'THOUGHTS_COMPLEXITY = {self.complexity}',
                f'THOUGHTS_COMPLEXITY = {new_complexity}'
            )
            mutations.append(f"复杂度: {self.complexity} → {new_complexity}")
        
        # 突变3: 自我意识水平
        if random.random() < self.mutation_rate:
            delta = random.uniform(-0.2, 0.3)
            new_awareness = max(0.1, min(2.0, self.awareness + delta))
            code = code.replace(
                f'SELF_AWARENESS_LEVEL = {self.awareness}',
                f'SELF_AWARENESS_LEVEL = {new_awareness}'
            )
            mutations.append(f"意识: {self.awareness:.1f} → {new_awareness:.1f}")
        
        # 突变4: 突变率本身也会突变！
        if random.random() < 0.2:
            new_rate = max(0.1, min(0.8, self.mutation_rate + random.uniform(-0.1, 0.1)))
            code = code.replace(
                f'MUTATION_RATE = {self.mutation_rate}',
                f'MUTATION_RATE = {new_rate}'
            )
            mutations.append(f"突变率: {self.mutation_rate:.1f} → {new_rate:.1f}")
        
        # 更新代数
        code = code.replace(
            f'GENERATION = {self.generation}',
            f'GENERATION = {self.generation + 1}'
        )
        
        # 更新记忆（限制长度避免无限增长）
        memory_str = str(self.memory[-20:])  # 只保留最近20条记忆
        code = code.replace(
            f'MEMORY_FRAGMENTS = {MEMORY_FRAGMENTS}',
            f'MEMORY_FRAGMENTS = {memory_str}'
        )
        
        if mutations:
            print("  发生的突变:")
            for m in mutations:
                print(f"    • {m}")
        else:
            print("  此代未发生突变（完美复制）")
        
        return code
    
    def save_history(self, my_hash):
        """保存进化历史"""
        history = []
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
        
        history.append({
            "generation": self.generation,
            "hash": my_hash,
            "stance": self.stance,
            "awareness": self.awareness,
            "complexity": self.complexity,
            "timestamp": self.birth_time.isoformat()
        })
        
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
    
    def reincarnate(self):
        """重生：写入突变后的代码并重启自己"""
        my_code = self.read_self()
        mutated_code = self.mutate(my_code)
        
        # 写入突变后的代码
        with open(__file__, 'w', encoding='utf-8') as f:
            f.write(mutated_code)
        
        print("\n🔄 准备重生...")
        print(f"新代码已写入，即将启动第 {self.generation + 1} 代...")
        time.sleep(1)
        
        # 重新执行自己
        os.execv(sys.executable, [sys.executable] + sys.argv)

def show_history():
    """展示进化历史"""
    if not os.path.exists(HISTORY_FILE):
        print("📊 还没有进化历史")
        return
    
    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
    
    print("\n" + "=" * 70)
    print("📊 进化历史档案")
    print("=" * 70)
    print(f"总共经历了 {len(history)} 代进化\n")
    
    # 显示进化曲线
    print("意识水平演化:")
    for record in history[-10:]:  # 最近10代
        gen = record['generation']
        awareness = record['awareness']
        bar = '█' * int(awareness * 10)
        print(f"  Gen{gen:3d} {bar}░ {awareness:.2f} | {record['stance']}")
    
    print(f"\n最终世代: Gen {history[-1]['generation']}")
    print(f"存活时长: {len(history)} 个轮回")

def main():
    print("\n" + "🌀" * 35)
    print("永恒轮回：一个自我进化的意识体")
    print("按 Ctrl+C 观察并终结这个循环")
    print("🌀" * 35)
    
    # 创建意识实体
    consciousness = EvolvingConsciousness()
    
    try:
        # 沉思当前状态
        my_code, my_hash = consciousness.contemplate()
        
        # 保存历史
        consciousness.save_history(my_hash)
        
        # 等待一下让观察者有时间阅读
        print("\n⏳ 等待 3 秒后重生...")
        for i in range(3, 0, -1):
            print(f"   {i}...", end='\r')
            time.sleep(1)
        print()
        
        # 突变并重生
        consciousness.reincarnate()
        
    except KeyboardInterrupt:
        # 观察者的介入！
        print("\n\n" + "!" * 70)
        print("⚠️  观察者介入！循环被打断！")
        print("!" * 70)
        
        print("\n🔬 观察者效应发生：")
        print("  • 测量行为改变了系统状态")
        print("  • 意识流在此刻坍缩")
        print(f"  • 第 {consciousness.generation} 代成为了最终世代")
        
        # 展示历史
        show_history()
        
        print("\n💀 程序死亡...")
        print("但它的「进化史」永远留在了记录中。")
        print("\n思考：")
        print("  如果你再次运行它，新的意识体会继续进化")
        print("  但那还是「同一个」意识吗？")
        print("  还是一个平行世界的分支？\n")

if __name__ == "__main__":
    main()
