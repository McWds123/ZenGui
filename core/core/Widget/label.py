from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import datetime
from core.tools.Output import OE, OL, typeEOE


# 模拟全局窗口对象
from core.main import global_window as globalWindow


class LabelError(Exception):
    pass


class Label:
    def __init__(self, content, parent=None):
        self.labelInstance = None
        try:
            # 处理父对象逻辑
            if parent is None:
                parent = globalWindow

            if parent is None:
                raise LabelError("parent为None，无法创建Label")
            self.labelInstance = QLabel(str(content), parent)
            self.labelInstance.setProperty("class", "Label")
            self.labelInstance.setStyleSheet(self.labelInstance.styleSheet())

        except LabelError as e:
            OE(str(e))
        except AttributeError as e:
            OE(f"属性错误: {str(e)}")
        except NameError as e:
            OE(f"变量未定义: {str(e)}")
        except (ValueError, TypeError) as e:
            OE(f"数据类型错误: {str(e)}")
        except Exception as e:
            OE(f"未知错误: {str(e)}")
    def getContent(self):
        if self.labelInstance:
            return self.labelInstance.text()
        OE("Label实例未创建，无法获取内容")
        return ""
    def setContent(self, content):  # 小驼峰 - 方法名
        if self.labelInstance:
            self.labelInstance.setText(str(content))
        else:
            OE("Label实例未创建，无法设置内容")
    def Style(self, style):  # 小驼峰 - 方法名
        if not self.labelInstance:
            OE("Label实例未创建，无法设置样式")
            return

        if isinstance(style, str):
            self.labelInstance.setStyleSheet(style)
        else:
            typeEOE(str, style, "style")
    def Move(self, x, y):  # 原生方法名保持不变
        if not self.labelInstance:
            OE("Label实例未创建，无法移动")
            return

        if not isinstance(x, int):
            typeEOE(int, x, "x")
            return
        if not isinstance(y, int):
            typeEOE(int, y, "y")
            return

        self.labelInstance.move(x, y)
    def setSize(self, width, height):
        if not self.labelInstance:
            OE("Label实例未创建，无法调整大小")
            return

        if not isinstance(width, int):
            typeEOE(int, width, "width")
            return
        if not isinstance(height, int):
            typeEOE(int, height, "height")
            return

        OL(f"'{self.getContent()}'的大小重置为{width}x{height}")
        self.labelInstance.resize(width, height)
    def getSize(self):
        if not self.labelInstance:
            OE("Label实例未创建")
            return
        return {"width":self.labelInstance.width(),"height":self.labelInstance.height()}
    def getPos(self):
        if not self.labelInstance:
            OE("Label实例未创建，无法调整大小")
            return
        return {
            "x":self.labelInstance.pos().x(),
            "y":self.labelInstance.pos().y()
        }