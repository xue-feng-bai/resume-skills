#!/usr/bin/env python3
"""
将 HTML 简历转换为 PDF
用法: python3 html_to_pdf.py --input <html路径> --output <pdf路径>
依赖: google-chrome (headless)
"""

import argparse
import shutil
import subprocess
import sys
import os


def find_chrome():
    """自动查找系统中可用的 Chrome/Chromium 可执行文件"""
    names = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    # macOS 常见路径
    mac_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for path in mac_paths:
        if os.path.exists(path):
            return path
    return None


def html_to_pdf(html_path, pdf_path, window_size="900,1200"):
    """使用 Chrome headless 将 HTML 转为 PDF"""

    if not os.path.exists(html_path):
        print(f"Error: HTML file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    chrome_path = find_chrome()
    if not chrome_path:
        print("Error: Chrome/Chromium not found. Please install Chrome or Chromium.", file=sys.stderr)
        sys.exit(1)

    # 确保输出目录存在
    os.makedirs(os.path.dirname(pdf_path) if os.path.dirname(pdf_path) else ".", exist_ok=True)

    cmd = [
        chrome_path,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        f"file://{os.path.abspath(html_path)}"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"Chrome error: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        
        if os.path.exists(pdf_path):
            size_kb = os.path.getsize(pdf_path) / 1024
            print(f"PDF generated: {pdf_path} ({size_kb:.0f} KB)")
        else:
            print("Error: PDF was not created", file=sys.stderr)
            sys.exit(1)
            
    except FileNotFoundError:
        print("Error: google-chrome not found. Please install Chrome/Chromium.", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("Error: PDF generation timed out", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="将 HTML 简历转为 PDF")
    parser.add_argument("--input", required=True, help="输入的 HTML 文件路径")
    parser.add_argument("--output", required=True, help="输出的 PDF 文件路径")
    args = parser.parse_args()
    
    html_to_pdf(args.input, args.output)


if __name__ == "__main__":
    main()
