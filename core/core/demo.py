import sys

from Widget.Text import LineText
from Widget.button import Button
from Widget.combobox import Combobox
from Widget.label import Label
from Widget.place import MIDDLE_X, MIDDLE_Y
from main import run
from tools.Output import OL

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