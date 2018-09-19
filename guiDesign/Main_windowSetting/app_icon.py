#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    workdir_List=[sys.argv, 'D:/Users/lanwei/Desktop/test_1/icons'] #/test_1/icons'] #/icons
    print(workdir_List[0])
    app = QApplication(workdir_List)
    ex = Example()
    sys.exit(app.exec_())