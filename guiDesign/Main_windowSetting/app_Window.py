#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program centers a window
on the screen.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
                             QPushButton, QApplication)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon,QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set font for tip words
        QToolTip.setFont(QFont('SansSerif', 10))

        # Create a button to control exit of program
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(300, 300)

        # Set window size and center it on user's device screen
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.resize(600, 600)
        self.center()

        # Set window title and icon, then display it
        self.setWindowTitle('Test program')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        # Give warning when user attempting to close the window
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        elif reply == QMessageBox.No:
            event.ignore()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())