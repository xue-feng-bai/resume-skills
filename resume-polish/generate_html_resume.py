#!/usr/bin/env python3
"""
生成优化后的简历 HTML 文件
用法: python3 generate_html_resume.py --input <简历内容JSON> --output <输出路径>
"""

import argparse
import json
import sys
from datetime import datetime


def generate_resume_html(data, template_path=None):
    """根据简历数据生成完整 HTML"""
    
    # 基础样式
    base_css = """
    <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
        background: #f5f5f5; color: #333; line-height: 1.6;
    }
    .container {
        max-width: 900px; margin: 40px auto; background: #fff;
        padding: 40px 50px; box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    .header {
        border-bottom: 2px solid #1a1a1a; padding-bottom: 20px; margin-bottom: 24px;
    }
    .name { font-size: 32px; font-weight: 700; color: #1a1a1a; letter-spacing: 2px; margin-bottom: 8px; }
    .target { font-size: 15px; color: #ff6b35; font-weight: 600; margin-bottom: 12px; letter-spacing: 0.5px; }
    .contact { font-size: 13.5px; color: #555; display: flex; flex-wrap: wrap; gap: 6px 20px; }
    .contact .sep { color: #ccc; }
    .section { margin-bottom: 20px; }
    .section-title {
        font-size: 15px; font-weight: 700; color: #1a1a1a;
        border-left: 4px solid #ff6b35; padding-left: 10px; margin-bottom: 12px;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .skills-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 24px; }
    .skill-item {
        font-size: 13.5px; color: #444; padding: 6px 0;
        border-bottom: 1px dashed #eee; line-height: 1.7;
    }
    .skill-item strong { color: #1a1a1a; font-weight: 600; }
    .project-header, .job-header {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 6px; flex-wrap: wrap; gap: 4px;
    }
    .project-name, .company { font-size: 15px; font-weight: 700; color: #1a1a1a; }
    .project-meta, .job-time { font-size: 13px; color: #888; }
    .job-title { font-size: 13.5px; color: #555; font-weight: 500; }
    .job-location { font-size: 12.5px; color: #aaa; }
    .project-link {
        display: inline-block; font-size: 12.5px; color: #ff6b35;
        text-decoration: none; border: 1px solid #ff6b35;
        padding: 2px 10px; border-radius: 3px; margin-top: 6px;
    }
    .project-desc { font-size: 13.5px; color: #444; margin-bottom: 8px; line-height: 1.8; }
    .detail-list { list-style: none; padding-left: 0; }
    .detail-list li {
        font-size: 13.5px; color: #444; padding: 4px 0 4px 18px;
        position: relative; line-height: 1.7;
    }
    .detail-list li::before { content: "▸"; position: absolute; left: 0; color: #ff6b35; font-size: 12px; }
    .edu-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; }
    .edu-name { font-size: 14.5px; font-weight: 600; color: #1a1a1a; }
    .edu-major { font-size: 13.5px; color: #555; }
    .edu-tag { font-size: 12px; color: #ff6b35; border: 1px solid #ff6b35; padding: 1px 8px; border-radius: 2px; }
    @media (max-width: 768px) {
        .container { padding: 30px 24px; margin: 20px auto; }
        .skills-grid { grid-template-columns: 1fr; }
        .project-header, .job-header { flex-direction: column; align-items: flex-start; }
    }
    @media print {
        body { background: #fff; }
        .container { box-shadow: none; margin: 0; padding: 30px 40px; }
    }
    </style>
    """
    
    # 构建 HTML 内容
    html_parts = []
    
    # 头部信息
    header = data.get("header", {})
    contact_items = header.get("contact", [])
    contact_html = ""
    for i, item in enumerate(contact_items):
        contact_html += f'<span>{item}</span>'
        if i < len(contact_items) - 1:
            contact_html += ' <span class="sep">|</span> '
    html_parts.append(f"""
    <div class="header">
        <div class="name">{header.get("name", "")}</div>
        <div class="target">求职方向：{header.get("target", "")}</div>
        <div class="contact">
            {contact_html}
        </div>
    </div>
    """)
    
    # 核心能力
    skills = data.get("skills", [])
    if skills:
        skills_html = "\n".join([f'<div class="skill-item"><strong>{s["title"]}：</strong>{s["desc"]}</div>' for s in skills])
        html_parts.append(f"""
    <div class="section">
        <div class="section-title">核心能力</div>
        <div class="skills-grid">
            {skills_html}
        </div>
    </div>
        """)
    
    # 项目经历
    projects = data.get("projects", [])
    for project in projects:
        details = "\n".join([f'<li><strong>{d["label"]}：</strong>{d["content"]}</li>' for d in project.get("details", [])])
        link_html = f'<span class="project-link">{project.get("link", "")}</span>' if project.get("link") else ""
        html_parts.append(f"""
    <div class="section">
        <div class="section-title">项目经历</div>
        <div class="project-header">
            <span class="project-name">{project.get("name", "")}</span>
            <span class="project-meta">{project.get("meta", "")}</span>
        </div>
        <div class="project-desc">{project.get("desc", "")}{link_html}</div>
        <ul class="detail-list">
            {details}
        </ul>
    </div>
        """)
    
    # 工作经历
    jobs = data.get("jobs", [])
    if jobs:
        jobs_html = ""
        for job in jobs:
            details = "\n".join([f'<li>{d}</li>' for d in job.get("details", [])])
            jobs_html += f"""
        <div style="margin-bottom: 16px;">
            <div class="job-header">
                <div><span class="company">{job.get("company", "")}</span> <span class="job-title">· {job.get("title", "")}</span></div>
                <div><span class="job-time">{job.get("time", "")}</span> <span class="job-location">{job.get("location", "")}</span></div>
            </div>
            <ul class="detail-list">
                {details}
            </ul>
        </div>
            """
        html_parts.append(f"""
    <div class="section">
        <div class="section-title">工作经历</div>
        {jobs_html}
    </div>
        """)
    
    # 教育经历
    education = data.get("education", {})
    if education:
        html_parts.append(f"""
    <div class="section">
        <div class="section-title">教育经历</div>
        <div class="edu-header">
            <div><span class="edu-name">{education.get("school", "")}</span> <span class="edu-major">· {education.get("major", "")} · {education.get("degree", "")}</span></div>
            <span class="edu-tag">{education.get("tag", "")}</span>
        </div>
    </div>
        """)
    
    # 组装完整 HTML
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{header.get("name", "简历")} - {header.get("target", "")}</title>
{base_css}
</head>
<body>
<div class="container">
    {''.join(html_parts)}
</div>
</body>
</html>"""
    
    return full_html


def main():
    parser = argparse.ArgumentParser(description="生成简历 HTML 文件")
    parser.add_argument("--input", required=True, help="输入的简历 JSON 文件路径")
    parser.add_argument("--output", required=True, help="输出的 HTML 文件路径")
    args = parser.parse_args()
    
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    html = generate_resume_html(data)
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"HTML resume generated: {args.output}")


if __name__ == "__main__":
    main()
