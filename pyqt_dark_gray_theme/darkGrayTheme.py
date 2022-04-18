import os, inspect, sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenuBar, QToolButton

from qt_sass_theme_getter.qtSassThemeGetter import QtSassThemeGetter


def readFrom(style_sheets: str):
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, style_sheets), 'r')
    content = f.read()
    return content

def getThemeStyle() -> str:
    t = QtSassThemeGetter()
    return t.getThemeStyle()

def getIconButtonStyle() -> str:
    t = QtSassThemeGetter()
    return t.getIconButtonStyle()

def getIconTextButtonStyle() -> str:
    t = QtSassThemeGetter()
    return t.getIconTextButtonStyle()

def getMenuBarStyle(menu_bar: QMenuBar) -> str:
    tool_button = menu_bar.findChild(QToolButton)
    tool_button.setArrowType(Qt.RightArrow)
    t = QtSassThemeGetter()
    return t.getMenuBarStyle()

def getMainWidgetStyle() -> str:
    t = QtSassThemeGetter()
    return t.getMainWidgetStyle()
