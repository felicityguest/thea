# -*- coding: iso-8859-1 -*-
import ColorbarRange
from PySide import QtGui, QtCore

class ColorbarOptions(QtGui.QDialog, ColorbarRange.Ui_ColorbarDialog):

  """
  This class controls the colorbar Range selection dialog box.

  The majority of the code for this class was generated from Qt,
  and is called using the setupUi command. This code can be found
  in ColorbarRange.py
  """
  
  def __init__(self):
    
    super(ColorbarOptions,self).__init__()
    self.setupUi(self)