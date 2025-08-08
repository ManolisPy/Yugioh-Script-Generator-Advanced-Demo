#-------------------------------------------------------------------------------
# ygoscr_core_window

# The main window is created and the necessary modules with
# the widgets and scripts are initialized.
#-------------------------------------------------------------------------------

import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow,
                            QLineEdit, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

import ygoscr_core_widgets
import ygoscr_scripts



class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ygoscr_core_widgets.initialize_methods(self)
        self.base_window()

    def base_window(self):

        self.setFixedSize(500, 600)
        self.setWindowTitle("Yugioh Script Generator Advanced - Demo")

        scrnrescenter = self.screen().availableGeometry().center()
        corewingeo = self.frameGeometry()
        corewingeo.moveCenter(scrnrescenter)
        self.move(corewingeo.topLeft())

        self.core_layout()
        self.signals()

    def core_layout(self):

        corelayout = QVBoxLayout()
        corelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        corelayout.addWidget(self.corenote, alignment=Qt.AlignmentFlag.AlignTop)
        corelayout.addWidget(self.corecombo, alignment=Qt.AlignmentFlag.AlignTop)
        corelayout.addWidget(self.coretext, alignment=Qt.AlignmentFlag.AlignCenter)
        corelayout.addWidget(self.corebtn, alignment=Qt.AlignmentFlag.AlignHCenter)

        corewnd = QWidget()
        corewnd.setLayout(corelayout)
        self.setCentralWidget(corewnd)

    '''ignore the following code. It does not work for some reason.'''
        #bgcolor = QPalette()
        #bgcolor.setColor(QPalette.window, QColor.black)
        #self.bgcolor.setAutoFillBackground(true)
        #corewnd.setPalette(bgcolor)

    def signals(self):

        self.corebtn.clicked.connect(lambda: ygoscr_scripts.file_creation(self))
        self.corecombo.currentTextChanged.connect(lambda: self.combo_to_text())
    '''The following, alternative line of lambda code for the text also works.
    However, I wanted to make the default option become disabled after the
    first change, without writing a new method for a measly "if".'''
       #(lambda: self.coretext.setText(self.corecombo.currentText()))

    def combo_to_text(self):

        self.coretext.setText(self.corecombo.currentText())
        self.corecombo.model().item(0).setEnabled(False)



# The following lines can be included in a method and called from there.
ygoapp = QApplication([])
mainwnd = MyMainWindow()
mainwnd.show()
ygoapp.exec()
