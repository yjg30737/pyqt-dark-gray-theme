import os, inspect, sys


def readFrom(style_sheets: str):
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, style_sheets), 'r')
    content = f.read()
    return content

def getThemeStyle() -> str:
    return readFrom('theme.css')

def getIconButtonStyle() -> str:
    return readFrom('icon_button.css')

def getNoIconButtonStyle() -> str:
    return readFrom('no_icon_button.css')
