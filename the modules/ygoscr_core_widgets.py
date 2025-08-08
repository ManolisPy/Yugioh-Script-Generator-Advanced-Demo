#-------------------------------------------------------------------------------
# ygoscr_core_widgets

# The menu bar and all the required widgets are included.
#-------------------------------------------------------------------------------

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QTextEdit, QPushButton, QLabel, QComboBox,
                            QWidget, QVBoxLayout, QTextBrowser)
from PyQt6.QtCore import Qt

import inspect



def initialize_methods(self):

    core_menubar(self)
    core_note(self)
    core_combobox(self)
    core_effect_text(self)
    core_button_script(self)
    help_window(self)

def core_menubar(self):

    actioncoreabt = QAction('&About', self)
    actioncoreabt.triggered.connect(lambda: self.helpwnd.show())

    actioncoreexit = QAction('&Exit', self)
    actioncoreexit.setShortcut('Ctrl+Q')
    actioncoreexit.triggered.connect(self.close)

    coremenu = self.menuBar()
    menufile = coremenu.addMenu('&Menu')
    menufile.addAction(actioncoreabt)
    menufile.addAction(actioncoreexit)

def core_note(self):

    self.corenote = QLabel(
        'This is the demo version of a project in mind.'
        '\nSimply choose from the options below and click "Create script".'
        '\nYour option will appear in the text box as if you wrote it manually.'
        '\n\nMore information in Menu/About.',
        self)
    self.corenote.setAlignment(Qt.AlignmentFlag.AlignHCenter)

def core_combobox(self):

    self.corecombo = QComboBox(self)
    self.corecombo.setMaximumWidth(400)
    self.corecombo.addItem(
        'select an option'
        )
    self.corecombo.addItem(
        '[Normal Spell Card] Destroy all monsters on the field.'
        )
    self.corecombo.addItem(
        '[Normal Trap Card] Target 1 monster on the field: It gains '
        '500 ATK until the end of this turn.'
        )

def core_effect_text(self):

    self.coretext = QTextEdit(self)
    self.coretext.setFixedSize(400, 200)
    #self.coretext.setText(self.corecombo.currentText())

def core_button_script(self):

    self.corebtn = QPushButton('Create script', self)
    self.corebtn.setMaximumSize(100, 50)

def help_window(self):

    self.helpwnd = QWidget()
    self.helpwnd.setFixedSize(550, 450)
    self.helpwnd.setWindowTitle('About')

    abttext = QTextBrowser()
    abttext.setHtml(
        "<p align='center'>"
        "<span style='font-size:14pt'>ABOUT THE PROGRAM</span>"
        "<br><br>"
        "<span style='font-size:10pt'>The program is supposed to utilize AI"
        " of some sort, in order to create .lua files"
        "<br>based on a Yu-Gi-Oh! game emulator, commonly known as EDOPro."
        "<br>The idea is to \"read\" the text written in the box and create"
        " the desired file,"
        "<br> instead of manually increasing the dictionaries of key words"
        " and pieces of code,"
        "<br>like I do in my original work here:"
        " <a href='https://github.com/ManolisPy/ScriptGeneratorYGO'>"
        "https://github.com/ManolisPy/ScriptGeneratorYGO</a>"
        "<br>Currently, it merely emulates the process by inserting ready text"
        "<br>and creating the corresponding file."
        "<br>(You can edit the text in the box but there's no point in it.)"
        "<br><br>I'm looking forward to feedback and ideas on whether or not"
        "<br>the concept is worth it."
        "<br><br> e-mail: emmanouilgs@gmail.com"
        "<br>LinkedIn: "
        "<a href='https://www.linkedin.com/in/emmanouil-gkarmpos/'>"
        "https://www.linkedin.com/in/emmanouil-gkarmpos/</span>"
        )
    abttext.setReadOnly(True)
    abttext.setOpenExternalLinks(True)

    abtlayout = QVBoxLayout()
    abtlayout.addWidget(abttext)
    self.helpwnd.setLayout(abtlayout)
