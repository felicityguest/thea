# -*- coding: iso-8859-1 -*-

import sys
import theaMainWindow
from PySide import QtGui

def main():
  
  app = QtGui.QApplication(sys.argv)
  gui = theaMainWindow.GUI()
  sys.exit(app.exec_())
  
    
if __name__ == '__main__':
  main()