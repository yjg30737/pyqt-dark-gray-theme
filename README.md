# pyqt-dark-gray-theme
PyQt Dark Gray Theme

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-dark-gray-theme.git --upgrade```

OR

Just copy the raw code of each css file and use it whatever you want.

## Usage
* ```getThemeStyle() -> str``` to get the ```dark_gray_theme.css```'s code.
* ```getIconButtonStyle() -> str``` to get the ```icon_button.css```'s code. This is for button which contains icon only.
* ```getIconTextButtonStyle() -> str``` to get the ```icon_text_button.css```'s code. This is for button which contains text only or icon and text.
* ```getMenuBarStyle(menu_bar: QMenuBar) -> str``` to get the ```menu_bar.css```'s code. This is for dealing with menu bar. You have to give the menu bar you want to change its style. 
* ```getMainWidgetStyle() -> str``` to get the ```main_widget.css```'s code. This is for dealing with the case of ```QWidget``` as main window.

## Example
Code Sample

Example GUI app - <a href="https://github.com/yjg30737/pyqt-comic-viewer.git">pyqt-comic-viewer</a>
```Python
from PyQt5.QtWidgets import QApplication, QPushButton
from pyqt_comic_viewer.comicBookViewer import ComicBookViewer
from pyqt_dark_gray_theme.darkGrayTheme import getThemeStyle, getIconButtonStyle, getIconTextButtonStyle, \
    getMenuBarStyle


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = ComicBookViewer()
    ex.setStyleSheet(getThemeStyle())
    btns = ex.findChildren(QPushButton)
    for btn in btns:
        if btn.text().strip() == '':
            btn.setStyleSheet(getIconButtonStyle())
        else:
            btn.setStyleSheet(getIconTextButtonStyle())
    menu_bar = ex.menuBar()
    menu_bar_style = getMenuBarStyle(menu_bar)
    menu_bar.setStyleSheet(menu_bar_style)
    ex.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/155912764-9857cc04-b2b8-462b-85a4-f35a697207cb.png)

