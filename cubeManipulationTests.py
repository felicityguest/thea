# -*- coding: iso-8859-1 -*-

import iris
import matplotlib.pyplot as plt
import iris.quickplot as qplt
import numpy as np
import unittest
import CubeControl as cc


class CubeControlTests(unittest.TestCase):
  """
  how do you test the output figure?
  """
  def testPlot1DwithGridlines(self):
    cube = iris.load_cube(iris.sample_data_path('SOI_Darwin.nc'))
    plt.subplot(1,2,1)
    cc.plot1D(cube, True)
    plt.subplot(1,2,2)
    qplt.plot(cube)
    plt.gca().grid(True)
    plt.show()
    
  def testPlot1DwithoutGridlines(self):
    cube = iris.load_cube(iris.sample_data_path('SOI_Darwin.nc'))
    plt.subplot(1,2,1)
    cc.plot1D(cube, False)
    plt.subplot(1,2,2)
    qplt.plot(cube)
    plt.show()
    
  def testSetPlotFilledContourPlain(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "Filled Contour", "Automatic", 15, False, None, None)
    plt.subplot(1,2,2)
    qplt.contourf(cube, 15)
    plt.show()
    
  def testSetPlotContourPlain(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "Contour", "Automatic", 15, False, None, None)
    plt.subplot(1,2,2)
    qplt.contour(cube, 15)
    plt.show()
    
  def testSetPlotpcolormeshPlain(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "pcolormesh", "Automatic", 15, False, None, None)
    plt.subplot(1,2,2)
    qplt.pcolormesh(cube)
    plt.show()
    
  def testSetPlotFilledContourLargeRange(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "Filled Contour", "brewer_Blues_09", 15, True, 400, 200)
    plt.subplot(1,2,2)
    qplt.contourf(cube, 15, cmap="brewer_Blues_09", vmin=200, vmax=400)
    
    plt.show()
    
  def testSetPlotContourLargeRange(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "Contour", "brewer_Blues_09", 15, True, 400, 200)
    plt.subplot(1,2,2)
    contours = qplt.contour(cube, 15, cmap="brewer_Blues_09", vmin=200, vmax=400)
    plt.clabel(contours, inline=1, fontsize=8)
    plt.show()
    
  def testSetPlotpcolormeshLargeRange(self):
    cube = iris.load_cube(iris.sample_data_path('air_temp.pp'))
    plt.subplot(1,2,1)
    cc.setPlot(cube, "pcolormesh", "brewer_Blues_09", 15, True, 400, 200)
    plt.subplot(1,2,2)
    qplt.pcolormesh(cube, cmap="brewer_Blues_09", vmin=200, vmax=400)
    plt.show()
    
    
    
def main():
    unittest.main()

if __name__ == '__main__':
    main()