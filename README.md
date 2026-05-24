<div align="center">

# VOCATION · OS

**职业叙事重构系统**

> 不是改简历。是重构你的职业竞争力。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![Status](https://img.shields.io/badge/Status-Production-00C853?style=flat-square)]()

</div>

---

## 如果你是 Agent

复制下方代码块，粘贴到终端执行：

```bash
# 克隆仓库并加载为 Claude Code Skill
git clone git@github.com:xue-feng-bai/resume-skills.git && cd resume-skills
```

根据用户当前求职阶段，自动路由到对应 Skill：

| 用户意图 | 加载路径 |
|---------|---------|
| "帮我看看简历" / "优化简历" | `resume-polish/SKILL.md` |
| "根据 JD 改简历" / "匹配岗位" | `jd2resume/SKILL.md` |
| "分析匹配度" / "深入讨论" | `jd2resume-discuss/SKILL.md` |
| "准备面试" / "模拟面试" | `jd2resume-interview/SKILL.md` |
| "一次性走完" / "全套准备" | `jd2resume-suite/SKILL.md` |

---

## 如果你是人类

### 这是什么

Vocation OS 是一套面向 Claude Code 的**求职操作系统**，覆盖从简历自检、岗位匹配、深度诊断到面试备战的全链路。

每个 Skill 都是独立的战术单元，组合使用则是一套完整的求职战略。

### 五层架构

```
┌─────────────────────────────────────────────────────────────┐
│  自检层              匹配层              诊断层              备战层   │
│                                                             │
│  resume-polish     jd2resume      jd2resume-discuss   jd2resume-  │
│                                        interview       │
│                                                             │
│  向内审视            向外对标            深度拆解            模拟推演   │
│  无需 JD             需要 JD             需要 JD             需要 JD   │
├─────────────────────────────────────────────────────────────┤
│                    jd2resume-suite                           │
│                    全链编排（可选）                             │
└─────────────────────────────────────────────────────────────┘
```

### 各 Skill 说明

**resume-polish · 自检重构**

五维度扫描引擎：零错误 / 结构完整性 / 叙事质量 / 卖点突出度 / 逻辑一致性。输出 P0/P1/P2 分级问题清单，附带 STAR / CAR / PAR / 量化优先四种写作套路，逐条确认后生成投递文件。

*适用场景：简历初稿完成后第一轮打磨，或长期未更新简历的全面翻新。*

**jd2resume · JD 精准映射**

解析岗位 JD 关键词，分析匹配度，标记已覆盖/偏差/缺失项。基于匹配结果调整叙述角度，自然融入关键词，输出 HTML / PDF / 长截图三种格式。

*适用场景：已锁定目标岗位，需要定向优化。*

**jd2resume-discuss · 深度诊断**

结合简历与 JD 进行多视角对比分析，解释"为什么不对"以及"行业默认写法是什么"。适合对高意向岗位做深度准备。

*适用场景：高意向岗位，愿意花时间深入理解匹配差距。*

**jd2resume-interview · 面试推演**

基于 JD 和简历生成完整面试方案：预测问题、设计回答策略、标注避坑提示、输出准备清单。把面试从临场发挥变成有备而战。

*适用场景：简历已投、面试在即，需要系统性备战。*

**jd2resume-suite · 全链编排**

只需提供一次 JD 和简历，自动串联「深度诊断 → 简历优化 → 面试方案」全流程。

*适用场景：求职高峰期，批量处理多个岗位。*

### 使用方式

```bash
# 1. 克隆仓库
git clone git@github.com:xue-feng-bai/resume-skills.git
cd resume-skills

# 2. 将目录添加为 Claude Code Skill
# 在 Claude Code 中加载对应子目录的 SKILL.md

# 3. 按 Skill 内部流程逐步执行
```

### 设计原则

- **事实优先**：不编造经历，只调整叙述角度
- **具体可执行**：每条建议精确到"改哪一句、怎么改"
- **用户确认机制**：逐条对比原写法 vs 建议写法，由用户选择
- **多格式输出**：HTML（可编辑）、PDF（直接投递）、长截图（手机查看）

---

## License

MIT
