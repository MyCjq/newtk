[![PyPI version](https://badge.fury.io/py/newtk.svg)](https://badge.fury.io/py/newtk)
[![Downloads](https://pepy.tech/badge/newtk)](https://pepy.tech/project/newtk)
```
# newtk
NewTk is a modern, lightweight GUI enhancement library for Python's built-in tkinter. It brings smooth animations, modern rounded widgets and interactive hover effects to your desktop applications with just a few lines of code.

NewTk 是一个为 Python 内置 tkinter 打造的现代化、轻量级 GUI 增强库。只需几行代码，就能为你的桌面应用带来平滑动画、现代化圆角控件与交互悬浮效果。

✨ Features (核心特性)
Smooth Animations: Add fade_in and fade_out window transitions effortlessly.

Modern Rounded UI Components: Rounded label, rounded rectangle button and circle button to replace native widgets.

Interactive Hover Effects: Responsive background color changes on mouse hover.

Safe & Robust: Defensive checks included to prevent crashes if methods are called out of order.

> Note: Dark/Light theme mode and input entry component are not available in v0.3.0, planned for future versions.
> 说明：明暗主题模式、输入框组件在 v0.3.0 暂未提供，计划在后续版本开发。

📦 Installation (安装)
Install newtk via pip:

```bash
pip install newtk
```

🚀 Quick Start (快速开始)
Here is a simple example to create a window with fade animation, rounded button, circle button and rounded label with hover effects:

```
import tkinter as tk
import newtk

def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("NewTk Demo")

# 1. Initialize window wrapper, fade-in animation
    app = newtk.Widget(root)
    app.Fade_in()

# 2. Rounded label
    lab = newtk.NewLabel(root, text="Rounded Label", width=140, height=40, radius=8)
    lab.pack(pady=10)

# 3. Rounded rectangle button with hover effect
    btn1 = newtk.NewButton(root, text="Rounded Button", width=120, height=40, radius=6,
                           command=lambda: print("Rounded Button clicked"))
    btn1.pack(pady=5)

# 4. Circle button
    btn2 = newtk.CircleButton(root, text="GO", width=60,
                             command=lambda: print("Circle Button clicked"))
    btn2.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
```

📝 Changelog (更新日志)
v0.3.0
- Refactored project structure, each widget is an independent file
- Extract common logic to Widget base class
- Add new components: NewLabel (rounded label), NewButton (rounded rectangle button), CircleButton (circle button)
- Temporarily remove NewEntry input component, will be redeveloped later
- Keep window fade_in / fade_out animation
- Standardize module exports


v0.2.0

- Added NewEntry component with smart placeholder (hover_text), password mask (show), manual insertion (add), and precise deletion (clear) support.
- Improved window animation logic (Fade_in and Fade_out).
- Added defensive checks (prevent None value errors).
- Fixed potential width="" and cmd=None crashes.

v0.1.0

- Initial release.
- Added Widget base class and NewButton component with hover effects.
- 
📄 License (开源协议)
This project is licensed under the MIT License - see the LICENSE file for details.
Copyright (c) 2026 cjq.
