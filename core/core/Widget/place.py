from PySide6.QtWidgets import QMainWindow

from core.tools.Output import typeEOE
from core.Window.get import getWindowSize

def MIDDLE_Y(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return getWindowSize(Window)["height"] // 2
def TOP(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return 0
def BOTTOM(Window, WidgetHeight):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return getWindowSize(Window)["height"] - WidgetHeight

def MIDDLE_X(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return getWindowSize(Window)["width"] // 2
def LEFT(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return 0
def RIGHT(Window, WidgetWidth):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return getWindowSize(Window)["width"] - WidgetWidth