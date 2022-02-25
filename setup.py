from setuptools import setup, find_packages

setup(
    name='pyqt-dark-gray-theme',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt-dark-gray-theme': ['dark_gray_theme.css']},
    description='PyQt dark-gray theme',
    url='https://github.com/yjg30737/pyqt-dark-gray-theme.git'
)