# code from https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments
import numpy as np
from scipy.spatial.distance import euclidean, sqeuclidean
from sympy import Point3D, Line3D, Plane

from lib.positions import coordArr, pointArr

def edgeLength(G,n,m):
    nodeAttr = G.nodes(True)
    return euclidean(coordArr(nodeAttr[n]), coordArr(nodeAttr[m]))

def closestPoints(A,B):

    ''' Given two lines defined by numpy.array pairs (a0,a1,b0,b1)
        Return the closest points on each segment and their distance
    '''
    a0, a1 = A
    b0, b1 = B

    # Calculate denomitator
    A = a1 - a0
    B = b1 - b0
    magA = np.linalg.norm(A)
    magB = np.linalg.norm(B)
    
    _A = A / magA
    _B = B / magB
    
    cross = np.cross(_A, _B);
    denom = np.linalg.norm(cross)**2
    
    
    # If lines are parallel (denom=0) test if lines overlap.
    # If they don't overlap then there is a closest point solution.
    # If they do overlap, there are infinite closest positions, but there is a closest distance
    if not denom:
        d0 = np.dot(_A,(b0-a0))
        d1 = np.dot(_A,(b1-a0))
        
        # Is segment B before A?
        if d0 <= 0 >= d1:
            if np.absolute(d0) < np.absolute(d1):
                return a0,b0,np.linalg.norm(a0-b0)
            return a0,b1,np.linalg.norm(a0-b1)
            
            
        # Is segment B after A?
        elif d0 >= magA <= d1:
            if np.absolute(d0) < np.absolute(d1):
                return a1,b0,np.linalg.norm(a1-b0)
            return a1,b1,np.linalg.norm(a1-b1)
                
                
        # Segments overlap, return distance between parallel segments
        return None,None,np.linalg.norm(((d0*_A)+a0)-b0)
        
    
    
    # Lines criss-cross: Calculate the projected closest points
    t = (b0 - a0);
    detA = np.linalg.det([t, _B, cross])
    detB = np.linalg.det([t, _A, cross])

    t0 = detA/denom;
    t1 = detB/denom;

    pA = a0 + (_A * t0) # Projected closest point on segment A
    pB = b0 + (_B * t1) # Projected closest point on segment B

    # clamp projections
    if t0 < 0:
        pA = a0
    elif t0 > magA:
        pA = a1
    
    if t1 < 0:
        pB = b0
    elif t1 > magB:
        pB = b1
        
    # Clamp projection A
    if (t0 < 0) or (t0 > magA):
        dot = np.dot(_B,(pA-b0))
        if dot < 0:
            dot = 0
        elif dot > magB:
            dot = magB
        pB = b0 + (_B * dot)

    # Clamp projection B
    if (t1 < 0) or (t1 > magB):
        dot = np.dot(_A,(pB-a0))
        if dot < 0:
            dot = 0
        elif dot > magA:
            dot = magA
        pA = a0 + (_A * dot)

    
    return pA,pB,np.linalg.norm(pA-pB)

def createBoundingBox(ranges):
  BoundingBox = []

  def makePoint(selection, ranges):
    point = [ranges[i][j] for i, j in enumerate(selection)]

    return Point3D(point)

  for i in (0,1):
    for j in (0,1,2):
      start = [i,i,i]
      p0 = makePoint(start, ranges)
    
      start[j] = not start[j]
      p1 = makePoint(start, ranges)

      k = (j+1) % 3
      start[k] = not start[k]
      p2 = makePoint(start, ranges)

      side = Plane(p0,p1,p2)
      BoundingBox.append(side)
  return BoundingBox

def testBoundingBox():
  testRanges = [(-1,1),(-1,1),(-1,1)]
  boundingbox1 = createBoundingBox(testRanges)

  line1 = Line3D((1,1,1),(3,3,3))
  # assert line1.intersect(boundingbox1) == [(-1,-1,-1),(1,1,1)]
  return (line1.intersect(boundingbox1)) # TODO: run the proper loop to test this

# testBoundingBox()

def getBoundingPoint(ray, boundingBox): # fix this up
  intersections = []
  for side in boundingBox:
    intersect = side.intersection(ray)
    if len(intersect) > 0:
      intersections.append(intersect[0])

  distances = []
  for i in intersections:
    distances.append(sqeuclidean(ray.source,i))
#   distances = np.array([sqeuclidean(ray.source,i) for i in intersections])
  endpoint = intersections[np.argmin(distances)]
  return pointArr(endpoint)