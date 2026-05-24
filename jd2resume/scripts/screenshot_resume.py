#!/usr/bin/env python3
"""
生成简历长截图（精确裁剪，无底部空白）
用法: python3 screenshot_resume.py --input <html路径> --output <png路径>
依赖: google-chrome (headless), python3-pil
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


def screenshot_fullpage(html_path, png_path, window_width=900):
    """
    截图并自动裁剪底部空白。
    方案：
    1. Chrome 以足够大的高度截图，确保覆盖全部内容
    2. PIL 裁剪底部空白区域
    """

    if not os.path.exists(html_path):
        print(f"Error: HTML file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    chrome_path = find_chrome()
    if not chrome_path:
        print("Error: Chrome/Chromium not found. Please install Chrome or Chromium.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(png_path) if os.path.dirname(png_path) else ".", exist_ok=True)

    tmp_png = png_path + ".tmp.png"

    # Step 1: Chrome 截图 — 使用足够大的高度确保覆盖全部内容
    cmd = [
        chrome_path,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--screenshot={tmp_png}",
        f"--window-size={window_width},3000",  # 足够大，覆盖全部内容
        "--hide-scrollbars",
        f"file://{os.path.abspath(html_path)}"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"Chrome error: {result.stderr}", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"Screenshot error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Step 2: PIL 裁剪底部空白
    try:
        from PIL import Image
        
        img = Image.open(tmp_png)
        width, height = img.size
        
        # 从底部往上扫描，找到第一个有内容的行
        # "有内容"的定义：该行有至少一个像素明显不是白色（< 240）
        # 采样间隔：每 5 个像素检查一次，加速
        padding = 20  # 底部保留 padding
        
        content_bottom = height  # 默认保留全部
        
        # 从底部往上扫描
        for y in range(height - 1, 0, -1):
            has_content = False
            # 每隔 10 像素采样
            for x in range(0, width, 10):
                pixel = img.getpixel((x, y))
                if len(pixel) == 4:
                    r, g, b, a = pixel
                    if a < 128:
                        continue
                else:
                    r, g, b = pixel[:3]
                
                # 如果像素明显不是白色，认为有内容
                if r < 245 or g < 245 or b < 245:
                    has_content = True
                    break
            
            if has_content:
                content_bottom = y + 1 + padding
                break
        
        # 如果内容很少（异常情况），保留原图
        if content_bottom < 200:
            content_bottom = height
        
        # 裁剪
        crop_height = min(content_bottom, height)
        cropped = img.crop((0, 0, width, crop_height))
        cropped.save(png_path, "PNG")
        
        # 清理临时文件
        os.remove(tmp_png)
        
        size_kb = os.path.getsize(png_path) / 1024
        print(f"Screenshot generated: {png_path} ({size_kb:.0f} KB, cropped to {crop_height}px)")
        
    except ImportError:
        os.rename(tmp_png, png_path)
        print(f"Screenshot generated (PIL not available, no crop): {png_path}")
    except Exception as e:
        if os.path.exists(tmp_png):
            os.rename(tmp_png, png_path)
        print(f"Screenshot generated (crop failed: {e}): {png_path}")


def main():
    parser = argparse.ArgumentParser(description="截取简历长截图（精确裁剪，无空白）")
    parser.add_argument("--input", required=True, help="输入的 HTML 文件路径")
    parser.add_argument("--output", required=True, help="输出的 PNG 文件路径")
    args = parser.parse_args()
    
    screenshot_fullpage(args.input, args.output)


if __name__ == "__main__":
    main()
