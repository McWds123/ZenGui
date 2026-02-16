import core.main as root
from core.Widget.Text import LineText, Text
from core.Widget.button import Button
from core.Widget.place import RIGHT
from core.main import Widget
import sys

app, main_window = root.run()
window = Widget.Window()
window.Size(Width=800, Height=600)
window.Title(content="Text/LineText新增功能示例")

# ========== 单行输入框（LineText）使用示例 ==========
line_text = LineText("line1", window.getWindow())
line_text.setSize(300, 40)
line_text.Move(50, 50)
line_text.setPlaceholder("请输入单行内容（密码模式）")  # 占位符
line_text.setEchoMode("password")  # 密码模式
line_text.setAlignment("center")    # 文字居中
line_text.setText("123456")        # 设置初始内容

# ========== 多行输入框（Text）使用示例 ==========
multi_text = Text("multi1", window.getWindow())
multi_text.setSize(500, 200)
multi_text.Move(50, 120)
multi_text.setPlaceholder("请输入多行内容（支持HTML）")  # 占位符
multi_text.setHtml("<h3>多行输入框</h3><p>支持<b>粗体</b>、<i>斜体</i>等HTML格式</p>")  # 富文本
multi_text.setLineWrapMode("widget_width")  # 按控件宽度换行
multi_text.appendText("追加一行内容")  # 追加文本

# 测试获取内容
def get_content():
    print("单行输入框内容：", line_text.getInput())
    print("多行输入框内容：", multi_text.getInput())
    print("多行选中内容：", multi_text.getSelectedText())
btn = Button("获取内容", window.getWindow())
btn.resize(100, 40)
btn.move(RIGHT(window.getWindow(),100), 350)
btn.setCommand(get_content)

main_window.show()
sys.exit(app.exec())