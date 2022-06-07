from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenuBar, QToolButton

from qt_sass_theme.qtSassTheme import QtSassTheme

t = QtSassTheme()

def getThemeStyle() -> str:
    return t.getThemeStyle()

def getIconButtonStyle() -> str:
    return t.getIconButtonStyle()

def getIconTextButtonStyle() -> str:
    return t.getIconTextButtonStyle()

def getMenuBarStyle(menu_bar: QMenuBar) -> str:
    tool_button = menu_bar.findChild(QToolButton)
    tool_button.setArrowType(Qt.RightArrow)
    return t.getMenuBarStyle()

def getMainWidgetStyle() -> str:
    return t.getMainWidgetStyle()
