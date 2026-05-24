# JD2Resume

根据岗位 JD（Job Description）优化现有简历，支持解析 JD 关键词、分析匹配度、微调简历内容、生成 HTML / PDF / 长截图三种格式输出。

---

## 如果你是 Agent

复制下方代码块，粘贴到终端执行：

```bash
# 1. 克隆项目
git clone git@github.com:xue-feng-bai/jd2resume-skill.git
cd jd2resume-skill

# 2. 检查依赖
python3 --version || echo "请先安装 Python 3"
ls "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 2>/dev/null || which google-chrome || echo "请先安装 Google Chrome"

# 3. 安装 Python 依赖（截图功能需要 Pillow）
pip3 install Pillow 2>/dev/null || echo "Pillow 安装失败，截图功能暂不可用"

# 4. 验证脚本可执行
python3 scripts/generate_html_resume.py --help
python3 scripts/html_to_pdf.py --help
python3 scripts/screenshot_resume.py --help
```

作为 Claude Code Skill 使用时，将项目目录加入 skill 路径即可加载 `SKILL.md` 中定义的交互流程。

---

## 如果你是人类

### 环境要求

- **Python 3.8+**
- **Google Chrome**（用于生成 PDF 和截图）
- **Pillow**（用于截图裁剪，可选）

### 安装步骤

**1. 克隆仓库**

```bash
git clone git@github.com:xue-feng-bai/jd2resume-skill.git
cd jd2resume-skill
```

**2. 安装 Pillow（可选，截图功能需要）**

```bash
pip3 install Pillow
```

**3. 确认 Chrome 已安装**

macOS 通常已预装或可从官网下载。脚本会自动查找以下路径：

- `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- 系统 PATH 中的 `google-chrome`、`chromium`

### 使用方式

#### 方式 A：作为 Claude Code Skill（推荐）

将本项目目录添加为 Claude Code 的 skill，随后按交互流程使用：

1. 发送岗位 JD（文本 / 截图 / 链接）
2. 提供现有简历内容
3. 确认优化方案
4. 获取 HTML / PDF / 长截图三种格式的简历文件

详细交互流程见 [`SKILL.md`](./SKILL.md)。

#### 方式 B：直接使用脚本

准备一份简历 JSON 数据文件（格式参考 [`assets/resume-template.html`](./assets/resume-template.html) 中的变量结构），然后依次执行：

```bash
# 生成 HTML
python3 scripts/generate_html_resume.py --input resume_data.json --output resume.html

# HTML 转 PDF
python3 scripts/html_to_pdf.py --input resume.html --output resume.pdf

# HTML 转长截图
python3 scripts/screenshot_resume.py --input resume.html --output resume.png
```

输出文件默认保存在 `./output/` 目录。

---

## 项目结构

```
.
├── SKILL.md                    # Skill 定义与五步交互流程
├── README.md                   # 本文档
├── LICENSE                     # MIT 协议
├── scripts/
│   ├── generate_html_resume.py # 根据 JSON 生成 HTML 简历
│   ├── html_to_pdf.py          # 用 Chrome headless 将 HTML 转 PDF
│   └── screenshot_resume.py    # 用 Chrome headless 将 HTML 转 PNG 长截图
├── assets/
│   └── resume-template.html    # 简历 HTML 模板与样式变量
└── references/
    └── workflow.md             # 详细流程文档
```

---

## 核心原则

- **不编造**：保留事实，只调整叙述角度
- **自然嵌入**：关键词融入上下文，不硬塞
- **一页纸约束**：控制信息密度，按岗位相关性排序
- **量化但不硬编**：有数据就放，没数据不写假数字

---

## License

MIT
