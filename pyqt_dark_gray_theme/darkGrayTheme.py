import os, inspect, sys


def getThemeStyle() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'theme.css'), 'r')
    content = f.read()
    return content

def getIconButtonStyle() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'icon_button.css'), 'r')
    content = f.read()
    return content

def getNoIconButtonStyle() -> str:
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'no_icon_button.css'), 'r')
    content = f.read()
    return content