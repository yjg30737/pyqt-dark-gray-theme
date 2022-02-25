import os, inspect, sys


def getDarkGrayTheme() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'dark_gray_theme.css'), 'r')
    content = f.read()
    return content

def getDarkGrayIconButtonStyle() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'icon_button.css'), 'r')
    content = f.read()
    return content

def getDarkGrayNoIconButtonStyle() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'no_icon_button.css'), 'r')
    content = f.read()
    return content