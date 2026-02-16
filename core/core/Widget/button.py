
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from core.main import global_window, Window
from core.tools.Output import OE, OL, typeEOE
class ButtonError(Exception):
    pass


class Button:
    def __init__(self, content, parent=None):
        self.buttonInstance = None
        try:
            if parent is None:
                parent = global_window

            if not parent:
                raise ButtonError("parent为None，无法创建按钮")

            self.buttonInstance = QPushButton(str(content), parent)
            self.buttonInstance.setProperty("class", "Button")
            self.buttonInstance.setStyleSheet(self.buttonInstance.styleSheet())

        except ButtonError as e:
            OE(str(e))
        except AttributeError as e:
            OE(f"属性错误: {str(e)}")
        except NameError as e:
            OE(f"变量未定义: {str(e)}")
        except (ValueError, TypeError) as e:
            OE(f"数据类型错误: {str(e)}")
        except Exception as e:
            OE(f"未知错误: {str(e)}")
    def setCommand(self, function):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法绑定点击事件")
            return

        if callable(function):
            self.buttonInstance.clicked.connect(function)
        else:
            OE(f"绑定的函数无效，期望可调用对象，实际{type(function).__name__}")
    def setStyle(self, style):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法设置样式")
            return

        if isinstance(style, str):
            self.buttonInstance.setStyleSheet(style)
        else:
            typeEOE(str, style, "style")
    def move(self, x, y):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法移动")
            return

        if not isinstance(x, int):
            typeEOE(int, x, "x")
            return
        if not isinstance(y, int):
            typeEOE(int, y, "y")
            return

        self.buttonInstance.move(x, y)
    def resize(self, width, height):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法调整大小")
            return

        if not isinstance(width, int):
            typeEOE(int, width, "width")
            return
        if not isinstance(height, int):
            typeEOE(int, height, "height")
            return

        OL(f"'{self.getContent()}'的大小重置为{width}x{height}")
        self.buttonInstance.resize(width, height)
    def getPos(self):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法获取位置")
            return None

        relativePos = self.buttonInstance.pos()
        return {
            "x": relativePos.x(),
            "y": relativePos.y()
        }
    def getContent(self):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法获取内容")
            return ""

        return self.buttonInstance.text()
    def getSize(self):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法获取尺寸")
            return None

        return {
            "width": self.buttonInstance.width(),
            "height": self.buttonInstance.height()
        }
    def setContent(self, content):
        if not self.buttonInstance:
            OE("按钮实例未创建，无法设置内容")
            return

        self.buttonInstance.setText(str(content))