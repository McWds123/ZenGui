from PySide6.QtWidgets import QComboBox
from core.tools.Output import OL, OE, typeEOE
from core.main import global_window as globalWindow


class ComboboxError(Exception):
    pass


warning = "Combobox实例未创建"
name = "Combobox"


class Combobox:
    def __init__(self, ComboboxId, parent=None):
        self.comboxInstance = None  # 统一实例变量名
        self.ComboboxID = ComboboxId
        try:
            # 1. 先校验ComboboxId的合法性，不合法直接终止
            if not ComboboxId:
                OE("ComboboxID没有创建 请检查有没有写ComboboxID")
                return  # 终止初始化，避免后续无效逻辑
            if not isinstance(ComboboxId, str):
                typeEOE(str, ComboboxId, "ComboboxId")
                return

            # 2. 处理父对象逻辑
            if parent is None:
                parent = globalWindow
            if parent is None:
                raise ComboboxError("parent为None，无法创建Combobox")

            # 3. 修正实例变量名：labelInstance → comboxInstance
            self.comboxInstance = QComboBox(parent)
            self.comboxInstance.setProperty("class", "Combobox")
            self.comboxInstance.setStyleSheet(self.comboxInstance.styleSheet())

        except ComboboxError as e:
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
        if not self.comboxInstance:
            OE(warning)
            return
        if not isinstance(width, int):
            typeEOE(int, width, "width")
            return
        if not isinstance(height, int):
            typeEOE(int, height, "height")
            return
        self.comboxInstance.resize(width, height)
        size = self.getSize()
        OL(f"{self.ComboboxID}的大小已重置为x:{size['width']},y:{size['height']}")
    def getSize(self):
        if not self.comboxInstance:
            OE(warning)
            return None  # 明确返回None，避免字典取值报错
        return {
            "width": self.comboxInstance.width(),
            "height": self.comboxInstance.height()
        }
    def Move(self, x, y):
        if not self.comboxInstance:
            OE(warning)
            return
        if not isinstance(x, int):
            typeEOE(int, x, "move.x")
            return
        # 修正错误：type → typeEOE
        if not isinstance(y, int):
            typeEOE(int, y, "move.y")
            return
        self.comboxInstance.move(x, y)
    def Style(self,style):
        if not self.comboxInstance:
            OE(warning)
            return
        if not isinstance(style,str):
            typeEOE(str,style,name)
            return
        self.comboxInstance.setStyleSheet(style)
        OL(f"{self.ComboboxID}的style设置成功")
    def addItem(self,text,data = None):
        if not self.comboxInstance:
            OE(warning)
            return
        if not isinstance(text,str):
            typeEOE(str,text,name)
        if data is not None:
            self.comboxInstance.addItem(text, data)
        else:
            self.comboxInstance.addItem(text)
        OL(f"{self.ComboboxID}已添加选项: {text}")
    def removeItem(self,data):
        if not self.comboxInstance:
            OE(warning)
        self.comboxInstance.removeItem(data)
        OL(f"已经把{self.ComboboxID}的第{data}个Item删除")
    def cleanItem(self):
        if not self.comboxInstance:
            OE(warning)
        self.comboxInstance.clear()
        OL(f"已经把{self.ComboboxID}的Item清空")
    def getItem(self):
        if not self.comboxInstance:
            OE(warning)
            return ""
        return self.comboxInstance.currentText()
    def setCurrentIndex(self, index):
        if not self.comboxInstance:
            OE(warning)
            return
        if not isinstance(index, int):
            typeEOE(int, index, "setCurrentIndex.index")
            return
        count = self.comboxInstance.count()
        if index < 0 or index >= count:
            OE(f"{self.ComboboxID}设置选中项失败: 索引{index}超出范围（0~{count-1}）")
            return
        self.comboxInstance.setCurrentIndex(index)
        OL(f"{self.ComboboxID}已选中索引{index}的选项: {self.getCurrentText()}")
    def getPos(self):
        if not self.comboxInstance:
            OE(warning)
        return {
            "x": self.comboxInstance.pos().x(),
            "y": self.comboxInstance.pos().y()
        }