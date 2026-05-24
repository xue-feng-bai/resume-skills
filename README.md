# Claude Resume Skills

一套围绕简历优化与求职准备的 Claude Code Skills，覆盖从简历自检、JD 匹配、深度讨论到面试准备的全流程。

## Skills 列表

| Skill | 功能 | 触发场景 |
|-------|------|---------|
| [jd2resume](./jd2resume) | 根据岗位 JD 优化简历，解析关键词、分析匹配度、生成 HTML/PDF/截图 | 用户发送 JD 并要求改简历 |
| [resume-polish](./resume-polish) | 纯简历自检与优化，无需 JD，五维度扫描质量问题 | 用户说"帮我看看简历" |
| [jd2resume-discuss](./jd2resume-discuss) | 结合简历与 JD 深度讨论，多视角拆解匹配差距 | 用户想深入分析某个岗位 |
| [jd2resume-interview](./jd2resume-interview) | 基于 JD 和简历生成面试准备方案，预测问题与回答策略 | 用户要准备面试 |
| [jd2resume-suite](./jd2resume-suite) | 一站式求职套件，串联讨论 → 优化 → 面试全流程 | 用户想一次性走完求职准备 |

## 使用方式

1. 将整个目录添加为 Claude Code 的 Skill
2. 根据具体场景选择对应的 Skill 使用
3. 各 Skill 内部有完整的交互流程说明

## 项目结构

```
.
├── jd2resume/              # JD 驱动的简历优化
│   ├── SKILL.md
│   ├── scripts/            # 生成 HTML / PDF / 截图
│   ├── assets/             # 简历模板
│   └── references/         # 流程文档
├── resume-polish/          # 纯简历自检优化
│   ├── SKILL.md
│   └── scripts/            # 同上
├── jd2resume-discuss/      # 深度讨论分析
│   └── SKILL.md
├── jd2resume-interview/    # 面试准备
│   └── SKILL.md
└── jd2resume-suite/        # 全流程套件
    └── SKILL.md
```

## License

MIT
