# zengui（v1.0）
增强型 PySide6 UI 组件库，简化按钮、输入框、下拉框等组件的创建和操作，降低 PySide6 入门成本。

## 快速开始
### 1. 环境依赖
```bash
pip install PySide6>=6.0.0
```
### 2.示例代码

```python
#也可以参考core.demo
import sys

from core.Widget.Text import LineText
from core.Widget.button import Button
from core.Widget.combobox import Combobox
from core.Widget.label import Label
from core.Widget.place import MIDDLE_X, MIDDLE_Y
from core.main import run
from core.tools.Output import OL

# 初始化应用和窗口
app, global_window = run()

# 1. 按钮
def btn_click():
    OL(f"输入框内容：{line_text.getInput()}")
    OL(f"下拉框选中：{combo.getItem()}")
btn = Button("点击测试", parent=global_window)
btn.move(MIDDLE_X(global_window)-50, MIDDLE_Y(global_window)-60)
btn.resize(100, 40)
btn.setCommand(btn_click)

# 2. 标签
label = Label("测试标签", parent=global_window)
label.Move(MIDDLE_X(global_window)-50, MIDDLE_Y(global_window)-20)
label.setSize(100, 30)

# 3. 单行输入框
line_text = LineText("test_input", parent=global_window)
line_text.Move(MIDDLE_X(global_window)-80, MIDDLE_Y(global_window)+20)
line_text.setSize(160, 30)
line_text.setPlaceholder("请输入内容")

# 4. 下拉框
combo = Combobox("test_combo", parent=global_window)
combo.Move(MIDDLE_X(global_window)-80, MIDDLE_Y(global_window)+70)
combo.setSize(160, 30)
combo.addItem("选项1")
combo.addItem("选项2")

# 运行
global_window.show()
sys.exit(app.exec())
```
### 3.文件结构
```
core/
├── LICENSE
├── README.md
├── pyproject.toml
├── .gitignore
├── core/
│   ├── __init__.py
│   ├── main.py
    ├── demo.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── Output.py  # 日志/错误输出工具
│   ├── widget/
│   │   ├── __init__.py
│   │   ├── button.py  # 按钮组件
│   │   ├── combobox.py  # 下拉框组件
│   │   ├── label.py  # 标签组件
│   │   ├── place.py  # 位置工具
│   │   └── text.py  # 文本框组件
│   └── window/
│       ├── __init__.py
│       └── get.py  # 窗口属性获取
└── test/
    └── test.py  # 基础功能测试用例
```
## 许可声明
zengui 基于 PySide6 开发，PySide6 遵循 LGPLv3 开源协议(https://www.gnu.org/licenses/lgpl-3.0.html)
zengui 仅封装 PySide6 的公开 API，未修改 PySide6 源码；使用 zengui 需遵守 PySide6 的 LGPLv3 协议要求。
