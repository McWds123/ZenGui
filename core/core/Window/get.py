from PySide6.QtWidgets import QMainWindow

from core.tools.Output import typeEOE


def getWindowSize(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return {
            "width": Window.width(),
            "height": Window.height()
        }
def getWindowTitle(Window):
    if not isinstance(Window, QMainWindow):
        typeEOE(QMainWindow, Window, "Window")
    else:
        return Window.windowTitle()