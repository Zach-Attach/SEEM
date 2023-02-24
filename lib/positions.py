import numpy as np
import networkx as nx

def getPositions(G):
  x=nx.get_node_attributes(G,'x')
  y=nx.get_node_attributes(G,'y')
  z=nx.get_node_attributes(G,'z')

  pos={}

  for i in x.keys():
    pos[i] = (x[i],y[i], z[i])

  return pos

def coordArr(point):
  return np.array([point['x'],point['y'],point['z']])

def pointArr(point):
  return np.array([float(point.x),float(point.y),float(point.z)])

def getBounds(G, epsilon):
  bounds = []
  for i in ('x','y','z'):
    vals = nx.get_node_attributes(G, i).values()
    maxVal = max(vals) + epsilon
    minVal = min(vals) - epsilon
    bounds.append((minVal,maxVal))
  return bounds