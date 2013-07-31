# -*- coding: iso-8859-1 -*-

import iris
import numpy as np


def getDataSelectDim1(dim_names, missing_dims):
  data = []
  enabled = True
  if missing_dims == 0:
    for name in dim_names:
      data.append(name)
    
  else:
    data.append("blank Dimension 1")
    
  return enabled, data
    
    
def getDataSelectDim2(dim_names, missing_dims):
  data = []
  enabled = True
  if missing_dims <= 1:
    if len(dim_names) == 1:
      enabled = False
    else:
      for name in dim_names:
	data.append(name)
    
  elif missing_dims == 2:
    data.append("blank Dimension 2")
    
  return enabled, data
    
    
def getDataSelectSlicedDim(cube, dim_names):
  data = []
  enabled = True
  if cube.ndim < 3:
    enabled = False
  else:
    for name in dim_names:
      data.append(name)
	
  return enabled, data
    

def getDataSelectSliceIndex(cube, dimension):
  
    enabled = True
    data = cube.coord(dimension).points
      
    return enabled, data
      

    
def getRemainingDims(dim_names, usedDims):
  unused_dims = []
  for name in dim_names:
    if name in usedDims:
      pass
    else:
      unused_dims.append(name)
	
  return unused_dims
    