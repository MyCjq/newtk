# newtk

NewTk is a modern, lightweight GUI enhancement library for Python's built-in tkinter. It brings smooth animations, modern styling, and interactive effects to your desktop applications with just a few lines of code.

NewTk 是一个为 Python 内置 tkinter 打造的现代化、轻量级 GUI 增强库。只需几行代码，就能为你的桌面应用带来平滑的动画、现代 UI 样式和交互效果。

## ✨ Features (核心特性)

- **Smooth Animations**: Add `fade_in` and `fade_out` window transitions effortlessly.
- **Modern UI Components**: Beautiful flat-design buttons and input fields to replace ugly native widgets.
- **Interactive Hover Effects**: Responsive background color changes on mouse hover.
- **Smart Entry Placeholder**: Built-in support for placeholder text that disappears on focus, including password mask (`*`) handling.
- **Theme Support**: Easily switch between dark (`dark`) and light (`light`) modes.
- **Safe & Robust**: Defensive checks included to prevent crashes if methods are called out of order.

## 📦 Installation (安装)

Install `newtk` via pip:

```bash
pip install newtk
🚀 Quick Start (快速开始)
Here is a simple example to create a modern window with an animated button, hover effects, and a smart placeholder entry:

python
import tkinter as tk
import newtk

def main():
    root = tk.Tk()
    root.geometry("350x250")
    root.title("NewTk Demo")

    # 1. Initialize window wrapper, fade-in animation, and dark theme
    app = newtk.Widget(root)
    app.Fade_in()
    app.dark()

    # 2. Create a modern button with hover effect and click command
    # Clicking the button will fade out and close the window
    btn = newtk.NewButton(root, text="Hover Me & Click", bg="#0078D7", cmd=app.Fade_out)
    btn.use().pack(pady=20)
    btn.hover(hover_bg="#005A9E", leave_bg="#0078D7")

    # 3. Create a smart Entry with placeholder and password mask
    entry = newtk.NewEntry(root, bg="#2d2d2d", size=12, width=25, hovertext="Enter your password...", show="*")
    entry.use().pack(pady=10)
    entry.hover_text() # Enable placeholder behavior
    
    # Try adding text programmatically
    # entry.add("MySecret123")
    
    # Try clearing text
    # entry.clear()

    root.mainloop()

if __name__ == '__main__':
    main()

📝 Changelog (更新日志)
v0.2.0 (Current)

Added NewEntry component with smart placeholder (hover_text), password mask (show), manual insertion (add), and precise deletion (clear) support.

Improved window animation logic (Fade_in and Fade_out).

Added defensive checks (prevent None value errors).

Fixed potential width="" and cmd=None crashes.

v0.1.0

Initial release.

Added Widget base class and NewButton component with hover effects.

📄 License (开源协议)
This project is licensed under the MIT License - see the LICENSE file for details.
Copyright (c) 2026 cjq.
This project is licensed under the MIT License - see the LICENSE file for details.
Copyright (c) 2026 cjq.
