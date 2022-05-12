# pyqt-dark-gray-theme
PyQt dark-gray theme

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-dark-gray-theme`

## Included Packages
* <a href="https://github.com/yjg30737/qt-sass-theme-getter.git">qt-sass-theme-getter</a> - For get dark-gray theme css code

## Usage
* `getThemeStyle() -> str` - use it to `QMainWindow`, `QDialog`.
* `getIconButtonStyle() -> str` - use it to `QPushButton/QToolButton` which has an icon. This is for button which contains icon only.
* `getIconTextButtonStyle() -> str` - use it to `QPushButton/QToolButton` which has no icon. This is for button which contains text only or icon and text.
* `getMenuBarStyle(menu_bar: QMenuBar) -> str` use it to `QMenuBar`. This is for dealing with menu bar. You have to give the menu bar you want to change its style. 
* `getMainWidgetStyle() -> str` use it to top level `QWidget`. This is for dealing with the case of `QWidget` as a main window.

## Example
Code Sample

Example GUI app - <a href="https://github.com/yjg30737/pyqt-comic-viewer.git">pyqt-comic-viewer</a> (which is `QMainWindow` as a parent class)
```Python
from PyQt5.QtWidgets import QApplication, QPushButton
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer
from pyqt_dark_gray_theme.darkGrayTheme import getThemeStyle, getIconButtonStyle, getIconTextButtonStyle, \
    getMenuBarStyle


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = ComicBookViewer()
    ex.setStyleSheet(getThemeStyle()) # whole theme
    btns = ex.findChildren(QPushButton) # buttons
    for btn in btns:
        # check if text exists
        if btn.text().strip() == '':
            btn.setStyleSheet(getIconButtonStyle()) # no text - icon button style
        else:
            btn.setStyleSheet(getIconTextButtonStyle()) # text - icon-text button style
    menu_bar = ex.menuBar() # menu bar
    menu_bar_style = getMenuBarStyle(menu_bar)
    menu_bar.setStyleSheet(menu_bar_style)
    ex.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155912764-9857cc04-b2b8-462b-85a4-f35a697207cb.png)

