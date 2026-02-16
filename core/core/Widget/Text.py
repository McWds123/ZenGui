from PySide6.QtWidgets import QLineEdit, QTextEdit
from PySide6.QtCore import Qt

from core.tools.Output import OE, typeEOE
from core.main import global_window as globalWindow


class TextError(Exception):
    pass


warning = "Text实例未创建"
name = "Text"


class LineText:
    def __init__(self, textId, parent=None):
        self.textInstance = None
        self.textID = textId
        try:
            if not self.textID:
                OE("没有填写textId")
            if not isinstance(self.textID, str):
                typeEOE(str, self.textID, name)
                return
            if parent is None:
                parent = globalWindow
            if parent is None:
                raise TextError("parent为None，无法创建LineText")

            self.textInstance = QLineEdit(parent)
            self.textInstance.setProperty("class", "Text")
            self.textInstance.setStyleSheet(self.textInstance.styleSheet())
        except TextError as e:
            OE(str(e))
        except AttributeError as e:
            OE(f"属性错误: {str(e)}")
        except NameError as e:
            OE(f"变量未定义: {str(e)}")
        except (ValueError, TypeError) as e:
            OE(f"数据类型错误: {str(e)}")
        except Exception as e:
            OE(f"未知错误: {str(e)}")

    def setSize(self, width, height):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.resize(width, height)

    def getSize(self):
        if not self.textInstance:
            OE(warning)
            return
        return {
            "width": self.textInstance.width(),
            "height": self.textInstance.height()
        }

    def Move(self, x, y):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.move(x, y)

    def getPos(self):
        if not self.textInstance:
            OE(warning)
            return
        return {
            "x": self.textInstance.pos().x(),
            "y": self.textInstance.pos().y()
        }

    def getInput(self):
        if not self.textInstance:
            OE(warning)
            return
        return self.textInstance.text()

    def Style(self, style):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(style, str):
            typeEOE(str, style, name)
            return
        self.textInstance.setStyleSheet(style)

    def setToolTip(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setToolTip(content)

    def setText(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setText(content)

    def clearText(self):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.clear()

    def setPlaceholder(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setPlaceholderText(content)

    def setReadOnly(self, is_readonly: bool):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(is_readonly, bool):
            typeEOE(bool, is_readonly, name)
            return
        self.textInstance.setReadOnly(is_readonly)

    def setEchoMode(self, mode: str):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(mode, str):
            typeEOE(str, mode, name)
            return

        mode_map = {
            "normal": QLineEdit.Normal,
            "password": QLineEdit.Password,
            "noecho": QLineEdit.NoEcho,
            "passwordechoonedit": QLineEdit.PasswordEchoOnEdit
        }
        if mode not in mode_map:
            OE(f"回显模式错误，可选值：{list(mode_map.keys())}")
            return
        self.textInstance.setEchoMode(mode_map[mode])

    def setAlignment(self, align: str):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(align, str):
            typeEOE(str, align, name)
            return

        align_map = {
            "left": Qt.AlignLeft,
            "right": Qt.AlignRight,
            "center": Qt.AlignCenter
        }
        if align not in align_map:
            OE(f"对齐方式错误，可选值：{list(align_map.keys())}")
            return
        self.textInstance.setAlignment(align_map[align])
class Text:
    def __init__(self, textId, parent=None):
        self.textInstance = None
        self.textID = textId
        try:
            if not self.textID:
                OE("没有填写textId")
            if not isinstance(self.textID, str):
                typeEOE(str, self.textID, name)
                return
            if parent is None:
                parent = globalWindow
            if parent is None:
                raise TextError("parent为None，无法创建Text（多行）")

            self.textInstance = QTextEdit(parent)
            self.textInstance.setProperty("class", "Text")
            self.textInstance.setStyleSheet(self.textInstance.styleSheet())
        except TextError as e:
            OE(str(e))
        except AttributeError as e:
            OE(f"属性错误: {str(e)}")
        except NameError as e:
            OE(f"变量未定义: {str(e)}")
        except (ValueError, TypeError) as e:
            OE(f"数据类型错误: {str(e)}")
        except Exception as e:
            OE(f"未知错误: {str(e)}")

    def setSize(self, width, height):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.resize(width, height)

    def getSize(self):
        if not self.textInstance:
            OE(warning)
            return
        return {
            "width": self.textInstance.width(),
            "height": self.textInstance.height()
        }

    def Move(self, x, y):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.move(x, y)

    def getPos(self):
        if not self.textInstance:
            OE(warning)
            return
        return {
            "x": self.textInstance.pos().x(),
            "y": self.textInstance.pos().y()
        }

    def getInput(self):
        if not self.textInstance:
            OE(warning)
            return
        return self.textInstance.toPlainText()

    def Style(self, style):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(style, str):
            typeEOE(str, style, name)
            return
        self.textInstance.setStyleSheet(style)

    def setToolTip(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setToolTip(content)

    def setText(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setPlainText(content)

    def setHtml(self, html_content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(html_content, str):
            typeEOE(str, html_content, name)
            return
        self.textInstance.setHtml(html_content)

    def clearText(self):
        if not self.textInstance:
            OE(warning)
            return
        self.textInstance.clear()

    def setReadOnly(self, is_readonly: bool):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(is_readonly, bool):
            typeEOE(bool, is_readonly, name)
            return
        self.textInstance.setReadOnly(is_readonly)

    def setPlaceholder(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.setPlaceholderText(content)

    def setLineWrapMode(self, mode: str):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(mode, str):
            typeEOE(str, mode, name)
            return

        mode_map = {
            "none": QTextEdit.NoWrap,
            "widgetwidth": QTextEdit.WidgetWidth,
            "fixedpixel": QTextEdit.FixedPixelWidth
        }
        if mode not in mode_map:
            OE(f"换行模式错误，可选值：{list(mode_map.keys())}")
            return
        self.textInstance.setLineWrapMode(mode_map[mode])

    def setAlignment(self, align: str):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(align, str):
            typeEOE(str, align, name)
            return

        align_map = {
            "left": Qt.AlignLeft,
            "right": Qt.AlignRight,
            "center": Qt.AlignCenter,
            "justify": Qt.AlignJustify
        }
        if align not in align_map:
            OE(f"对齐方式错误，可选值：{list(align_map.keys())}")
            return
        self.textInstance.setAlignment(align_map[align])

    def getSelectedText(self):
        if not self.textInstance:
            OE(warning)
            return
        return self.textInstance.textCursor().selectedText()

    def appendText(self, content):
        if not self.textInstance:
            OE(warning)
            return
        if not isinstance(content, str):
            typeEOE(str, content, name)
            return
        self.textInstance.append(content)