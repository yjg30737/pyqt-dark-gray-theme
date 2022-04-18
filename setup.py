from setuptools import setup, find_packages

setup(
    name='pyqt-dark-gray-theme',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt dark-gray theme',
    url='https://github.com/yjg30737/pyqt-dark-gray-theme.git',
    install_requires=[
        'PyQt5>=5.8',
        'qt-sass-theme-getter @ git+https://git@github.com/yjg30737/qt-sass-theme-getter.git@main'
    ]
)