import numpy as np
from sympy import Point3D, Ray3D
from lib.positions import coordArr, getBounds
from lib.geometry import createBoundingBox, testBoundingBox, getBoundingPoint
from lib.graphs import G_Kaiser_PenPals

EPSILON = 3 #10 #0.001

def neurite(origin, midPoint, boundingBox):
  ray = Ray3D(Point3D(origin), Point3D(midPoint))
  endPoint = getBoundingPoint(ray, boundingBox)
  return (origin, endPoint)

def getNeurites(G):
  neurites = {}
  bounds = getBounds(G, EPSILON)
  boundingBox = createBoundingBox(bounds)

  for k,n in G.nodes(True):
    origin = coordArr(n)
    penpal = G.nodes[n['PenPal']]
    destination = coordArr(penpal)

    neurites[k] = neurite(origin, destination, boundingBox)
  
  return neurites

def getNeurites_Random(G):
  neurites = {}
  bounds = getBounds(G, EPSILON)
  boundingBox = createBoundingBox(bounds)
  # print('test')
  for k,n in G.nodes(True):
    origin = coordArr(n)
    destination = np.array(
      [np.random.uniform(bounds[0][0],bounds[0][1]),
       np.random.uniform(bounds[1][0],bounds[1][1]),
       np.random.uniform(bounds[2][0],bounds[2][1])])
    # print(origin)
    # print(destination)

    neurites[k] = neurite(origin, destination, boundingBox)
  
  return neurites

def findSEEMNeurites(random=False):
  #
  if random:
    return getNeurites_Random(G_Kaiser_PenPals)
  else:
    return getNeurites(G_Kaiser_PenPals)