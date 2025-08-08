#-------------------------------------------------------------------------------
# Name:        ygoscr_scripts
# Purpose:
#
# Author:      ManolakisHD
#
# Created:     06/08/2025
# Copyright:   (c) ManolakisHD 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtCore import QFileInfo

import ygoscr_core_widgets
import ygoscr_example_scripts



def file_creation(self):

    if self.corecombo.currentIndex() == 0:
        QMessageBox.information(self, 'Error','Please select an option.')
    else:
        comboboxval = str(self.corecombo.currentIndex())
        tempname, _ = QFileDialog.getSaveFileName(self,
                                                     'Save as', "scriptno" + comboboxval, 'Lua Files (*.lua)')
        if not tempname:
            return
        else:
            savedFile = QFileInfo(tempname)

        if savedFile:
            codenum = savedFile.baseName()

        file = open(savedFile.absoluteFilePath(), 'w')
        if self.corecombo.currentIndex() == 1:
            file.write(ygoscr_example_scripts.spell_card)
        elif self.corecombo.currentIndex() == 2:
            file.write(ygoscr_example_scripts.trap_card)

        file.close()
        QMessageBox.information(self, 'Success','Script creation completed!')