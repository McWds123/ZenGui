from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

# 定义全局的窗口实例（供Widget操作）
global_window = None


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("初始窗口")
        self.resize(500, 400)
        self.a = QPushButton("a")


class Widget:
    class Window:
        def __init__(self):
            self.window = global_window

        def Size(self, Width, Height):
            if self.window:
                self.window.resize(Width, Height)

        def Title(self, content):
            if self.window:
                self.window.setWindowTitle(content)

        def Icon(self, icon):
            if self.window:
                self.window.setWindowIcon(icon)
        def getWindow(self):
            if self.window:
                return self.window

def init_app():
    global global_window  # 声明使用全局变量
    app = QApplication(sys.argv)

    # 创建唯一的窗口实例，并赋值给全局变量
    global_window = Window()
    global_window.show()

    # 注意：sys.exit(app.exec())会阻塞后续代码，需调整调用方式
    sys.exit(app.exec())


# 供外部调用的初始化函数（非阻塞）
def run():
    """初始化应用和窗口，不进入事件循环，供test.py调用"""
    global global_window
    app = QApplication.instance()  # 避免重复创建QApplication
    if not app:
        app = QApplication(sys.argv)
    global_window = Window()
    return app, global_window