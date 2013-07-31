# -*- coding: iso-8859-1 -*-


import matplotlib, sys
from PySide import QtGui, QtCore
from matplotlib import use
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class MplCanvas(FigureCanvas):
 
  def __init__(self):
    
    self.fig = Figure()
    self.fig = plt.gcf()

    FigureCanvas.__init__(self, self.fig)
    FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
    FigureCanvas.updateGeometry(self)
 
 
class matplotlibWidget(QtGui.QWidget):
 
  def __init__(self, parent = None):
    QtGui.QWidget.__init__(self, parent)
    self.canvas = MplCanvas()
    self.vbl = QtGui.QVBoxLayout()
    self.vbl.addWidget(self.canvas)
    self.setLayout(self.vbl)