# -*- coding: iso-8859-1 -*-
import iris, cartopy, matplotlib
import matplotlib.pyplot as plt
import iris.quickplot as qplt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as feature


  
def update(cube, plotType, projection, cmap, Ncontours, coastlines, gridlines, contourLabels, countries, rivers, 
	     cbMax, cbMin, dim1_name, dim1_index, dim2_name, dim2_index, slicedDimName, 
	    slicedDimIndex, sliceIndex, collapsedNames, collapsedIndices):

  """
  takes in all information about what to plot, and then manages the reduction and plotting
  of the cube.
  """
  missingCoords = getMissingCoords(cube)
  
  if cube.ndim == 1:
    plot1D(cube, gridlines)
    
  else:
    if cube.ndim == 2:
      # if the cube is 2D, no extraction is required
      sub_cube = cube

    else:
      """
      the cube has at least 3 dimensions. We therefore need to extract a sub-cube to plot. 
      """
      if missingCoords == 0:
	sub_cube = getSubCubeByIndex(cube, dim1_index, dim2_index, slicedDimIndex, collapsedIndices)
	newIndex = getCorrectIndex(dim1_index, dim2_index, slicedDimIndex)
	sub_cube = extractCube(sub_cube, [newIndex], [sliceIndex])
      else:                                  
	sub_cube = getSubCubeByName(cube, collapsedNames, collapsedIndices) 
	sub_cube = reduceCube(sub_cube, slicedDimName, sliceIndex)
	  
    plot2D(sub_cube, plotType, projection, cmap, Ncontours, coastlines, gridlines, contourLabels, countries, rivers, cbMax, cbMin)
    
    return sub_cube

    

def plot1D(cube, gridlines):
  """
  Calls quickplot.plot on the cube, and then adds
  gridlines if required
  """
  qplt.plot(cube)
  plt.gca().grid(gridlines) 

def plot2D(cube, plotType, projection, cmap, NContours, coastlines, gridlines, contourLabels, countries, rivers, cbMax, cbMin):
  """
  sets the projection, the calls for the drawing of the plot.
  attempts to draw any desired geographical data such as coastlines,
  but excepts that not all plots have this attribute.
  gridlines added if required
  """
  
  setProjection(projection)
  setPlot(cube, plotType, cmap, NContours, contourLabels, cbMax, cbMin)
  try:
    setGeographical(coastlines, countries, rivers)
  except AttributeError:
    pass
  setGridlines(gridlines)
  
  

def setPlot(cube, plotType, cmap, Ncontours, contourLabels, cbMax, cbMin):
  """
  Produces the desired plot. 
  vmax and vmin control the distribution of the colours accross the colorbar.
  """
  
  if plotType == "Filled Contour":
    qplt.contourf(cube, Ncontours, cmap=getColormap(cmap), levels=getLevels(cube, cbMax, cbMin, Ncontours), vmax=cbMax, vmin=cbMin)
  elif plotType == "Contour":
    contours = qplt.contour(cube, Ncontours, cmap=getColormap(cmap), levels=getLevels(cube, cbMax, cbMin, Ncontours), vmax=cbMax, vmin=cbMin)
    if contourLabels:
      plt.clabel(contours, inline=1, fontsize=8)
  elif plotType == "pcolormesh":
    qplt.pcolormesh(cube, cmap=getColormap(cmap), vmax=cbMax, vmin=cbMin)


def setProjection(projection):
  
  if projection == ("Plate Carree"):
    ax = plt.axes(projection=ccrs.PlateCarree())
  elif projection == ("Lambert Cylindrical"):
    ax = plt.axes(projection=ccrs.LambertCylindrical())     
  elif projection == ("Mercator"):
    ax = plt.axes(projection=ccrs.Mercator())
  elif projection == ("Miller"):
    ax = plt.axes(projection=ccrs.Miller())
  elif projection == ("Mollweide"):
    ax = plt.axes(projection=ccrs.Mollweide())
  elif projection == ("Orthographic"):
    ax = plt.axes(projection=ccrs.Orthographic())
  elif projection == ("Robinson"):
    ax = plt.axes(projection=ccrs.Robinson())
  elif projection == ("Stereographic"):
    ax = plt.axes(projection=ccrs.Stereographic())
  elif projection == ("Transverse Mercator"):
    ax = plt.axes(projection=ccrs.TransverseMercator())
  elif projection == ("Interrupted Goode Homolosine"):
    ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
  elif projection == ("Rotated Pole"):
    ax = plt.axes(projection=ccrs.RotatedPole())
  elif projection == ("OSGB"):
    ax = plt.axes(projection=ccrs.OSGB())
  elif projection == ("EuroPP"):
    ax = plt.axes(projection=ccrs.EuroPP())
  elif projection == ("Gnomonic"):
    ax = plt.axes(projection=ccrs.Gnomonic())
  elif projection == ("North Polar Stereo"):
    ax = plt.axes(projection=ccrs.NorthPolarStereo())
  elif projection== ("OSNI"):
    ax = plt.axes(projection=ccrs.OSNI()) 
  elif projection == ("South Polar Stereo"):
    ax = plt.axes(projection=ccrs.SouthPolarStereo())
  else:	
    pass
  

def setGeographical(coastlines, countries, rivers):
  
  if coastlines:
    plt.gca().coastlines()
    
  if countries:
    countries = feature.NaturalEarthFeature(category='cultural',name='admin_0_countries', scale='50m', facecolor='none')
    plt.gca().add_feature(countries)
      
  if rivers:
    plt.gca().add_feature(feature.RIVERS)
    plt.gca().add_feature(feature.LAKES)
    
    
def setGridlines(gridlines):
  """
  Different methods of adding gridlines exist... 
  
  Quickplot does not add axis labels for lat/lon graphs.
  Therefore by preference, qplt will draw gridlines with labels.
  
  This only works for lat/lon graphs in some projections however, 
  so if the graph is not lat/lon, an attribute error is thrown, 
  but if is not lat/lon, then axis labels exist anyway, so matplotlib
  is able to add gridlines based on these.
  
  if it is mearly unable to add labels to the grid, it will throw a
  Type error... here we allow it to add the grid without labels.
  
  If it is still unable to add gridlines, we print out the error 
  message and move on.
  """
  
  if gridlines:
    try:
      gl = plt.gca().gridlines(draw_labels=True)
      gl.xlabels_top = False
    except AttributeError:
      plt.gca().grid(True)
    except TypeError:
      gl = plt.gca().gridlines(draw_labels=False)
    except Exception as e:
      print e
    
    
def getColormap(cmap):

  if cmap == 'Automatic':
    colormap = None
  else:
    colormap = cmap
  return colormap
     
  

def setFixedColorbar(cube, dim1_name, dim2_name, slicedDimName, dim1_index, dim2_index, slicedDimIndex, collapsedIndices):
  """
  Runs through all slices along the sliced dimension 
  For each slice it takes the maximum and minimum value in the data.
  
  It then scans through and selects the maximum maximum and the minimum minimum, 
  and returns these. 
  """
  if getMissingCoords(cube) != 0:
    pass
  
  if cube.ndim > 2:
    
    sub_cube = getSubCubeByIndex(cube, dim1_index, dim2_index, slicedDimIndex, collapsedIndices)
    
    iterator = sub_cube.slices([dim1_name, dim2_name])
    slice_max = []
    slice_min = []
      
    for i in range(len(cube.coord(slicedDimName).points)):
      cube_slice = iterator.next()
      slice_max.append(np.max(cube_slice.data))
      slice_min.append(np.min(cube_slice.data))
	  
    maxCont = np.max(slice_max)
    minCont = np.min(slice_min)
      
  else:
    maxCont = None
    minCont = None
    
  return maxCont, minCont  
  
  
  
def getLevels(cube, cbMax, cbMin, Ncontours):
  """
  
  another method for manually fixing the colorbar.
  
  subtle difference...
  
  vmax/vmin : sets no. of contours across the range of values in the data
	      sets range of colours in the specified range.
	      ie... if temp data ranges from 295 - 300, and vmin/vmax 200 - 300,
	      will plot 25 shades of red.... which i like.
	      but.. if temp data ranges from 200 - 300, and vmin/vmax 250 - 255,
	      will plot blue across 12 contours, red across 12 and 1 green... which i don't like
	      
  levels :    sets no. of contours across the specified range
	      and sets the range of colours in the specified range.
	      
  conclusion: vmax/vmin much better for when the range of the data is smaller than colorbar range
	      levels much better for when the range of the data is larger than the colorbar range
	      
	      we therefore only set levels when data range > colorbar range.
  """
  if cbMax == None:
    levels = None
  else:
    dataMax = np.max(cube.data)
    dataMin = np.min(cube.data)
    if (dataMax - dataMin) < (cbMax - cbMin):
      levels = None
    else:
      maxLevel = cbMax
      minLevel = cbMin
      seperation = (maxLevel - minLevel) / Ncontours
      levels = []
      for i in range(Ncontours):
	nextLevel = minLevel + (seperation * i)
	levels.append(nextLevel)
  return levels



def getMissingCoords(cube):
  
  dimensionNames = [dimCoord.name() for dimCoord in cube.dim_coords]
  missingCoords = cube.ndim - len(dimensionNames)
  return missingCoords
  
  
def getCorrectIndex(dim1_index, dim2_index, slicedDimIndex):
  """
  this section ensures that the index of the coordinate for the original cube is mapped to the correct coordinate of the 
  smaller 3D cube
  """
  newIndex = 0
  if slicedDimIndex > dim1_index or slicedDimIndex > dim2_index:
    newIndex = 1
  if slicedDimIndex > dim1_index and slicedDimIndex > dim2_index:
    newIndex = 2
      
  return newIndex 
  
def getSubCubeByIndex(cube, dim1_index, dim2_index, slicedDimIndex, collapsedIndices):
  """
  This function returns a 3 Dimensional cube, with the 3 remaining dimensions being the 2 chosen axes dimensions and the 
  slice Dimension.
    
  The extraction itself is done by the extractCube function, so the main role of this method is to pass on the correct 
  inputs for the extraction. 
  """  
  coord_indices = []
  collapsed_dim_indices = []
  i = 0
  for dim_num in range(cube.ndim):
    if dim_num != dim1_index and dim_num != dim2_index and dim_num != slicedDimIndex:
      index = collapsedIndices[i]
      coord_indices.append(index)
      collapsed_dim_indices.append(dim_num)
      i += 1
  new_cube= extractCube(cube, collapsed_dim_indices, coord_indices)
  return new_cube
    
      
def extractCube(cube, dim_nums, coord_indices):
    
  slices = [slice(None)] * cube.ndim
  for i in range(len(dim_nums)):
    slices[dim_nums[i]] = coord_indices[i]
    i += 1
  newCube = cube[tuple(slices)]
  return newCube

      
      
def getSubCubeByName(cube, collapsedNames, collapsedIndices):
                                                       #dimensions, collapsing all but 2 dimensions onto the chosen values
  newCube = cube
  for i in range(cube.ndim - 3):
    dim_name = collapsedNames[i]  #Gets the name of the dimension to be collapsed on this iteration
    index = collapsedIndices[i]   #Gets the index of the point to be collapsed onto
    newCube = reduceCube(cube, dim_name, index)               #Passes the cube, dimension and index onto the extract function
  return newCube
    
    
def reduceCube(cube, name, index):
    
  value = cube.coord(name).points[index]                               #calculates the value of the coord at the given index
  if len(cube.coord(name).points) == 1:                                #Issues arise due to the precision of floating point numbers with
    lower_bound = value - 10                                                #constraints (constraint returns None)... I therefore use this 
    upper_bound = value + 10                                                #section of code to generate bounds for the values.
  else:                                                                                   
    valueDifference = cube.coord(name).points[1] - cube.coord(name).points[0]     
    lower_bound = value - valueDifference/10
    upper_bound = value + valueDifference/10
  constraint = iris.Constraint(coord_values = {name: lambda cell: lower_bound <= cell <= upper_bound})
  reduced_cube = cube.extract(constraint)
  return reduced_cube 

  
    
def loadAllSlices(cube, dim1_index, dim2_index, slicedDimIndex, collapsedNames, collapsedIndices):
  
  """
  THIS METHOD IS NOT CURRENTLY IN USE!!!
  
  The concept here was to allow for quicker transitions between slices by doing all of the calculation in advance. 
  As such, this method was created to make an iterator to step through and create all of the slices along the 
  sliced dimension. The cubes were then added to a cube list and so could be accessed easily, without further 
  calcutaion. 
  
  However, the increase in speed was dissapointingly small, as I think the dominant delay is due to the rendering
  of the image rather than in reducing the cube. 
  
  The method is kept here was I believe that it could still be useful if I ever attempt to add animation tools...
  combining this method with some way to save the images to a cache could be a simple method of allowing the 
  program to cycle through the slices very quickyl. 
  """
  
  missingCoords = getMissingCoords(cube)
  
  if missingCoords == 0:
    sub_cube = getSubCubeByIndex(cube, dim1_index, dim2_index, slicedDimIndex, collapsedIndices)
  else:
    sub_cube = getSubCubeByName(cube, collapsedNames, collapsedIndices)

  allSlices = []
  
  iterator = sub_cube.slices([dim1_name, dim2_name])
  for i in range(len(cube.coord(slicedDimName).points)):
    cube_slice = iterator.next()
    allSlices.append(cube_slice)
    
  return allSlices  
  
  