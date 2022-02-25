import os, inspect, sys


def getDarkGrayTheme():
    caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(0)).filename)
    f = open(os.path.join(caller_path, 'dark_gray_theme.css'), 'r')
    content = f.read()
    return content
