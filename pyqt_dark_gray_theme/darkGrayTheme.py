import os, inspect, sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenuBar, QToolButton


def readFrom(style_sheets: str):
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, style_sheets), 'r')
    content = f.read()
    return content

def getThemeStyle() -> str:
    return readFrom('theme.css')

def getIconButtonStyle() -> str:
    return readFrom('icon_button.css')

def getIconTextButtonStyle() -> str:
    return readFrom('icon_text_button.css')

def getMenuBarStyle(menu_bar: QMenuBar) -> str:
    tool_button = menu_bar.findChild(QToolButton)
    tool_button.setToolButtonStyle(Qt.ToolButtonTextOnly)
    tool_button.setText('»')
    return readFrom('menu_bar.css')

def getMainWidgetStyle() -> str:
    return readFrom('main_widget.css')
