from setuptools import setup, find_packages

setup(
    name='pyqt-dark-gray-theme',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_dark_gray_theme': ['theme.css',
                                           'icon_button.css',
                                           'icon_text_button.css']},
    description='PyQt dark-gray theme',
    url='https://github.com/yjg30737/pyqt-dark-gray-theme.git'
)