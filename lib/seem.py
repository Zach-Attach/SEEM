from lib.graphs import getCleanGraph
from lib.geometry import closestPoints, edgeLength
from numpy import random

def fullyConnectedGraph(neurites: dict, epsilon: float):
  G = getCleanGraph()

  neuron_neurite_Tuples = neurites.items()

  for neuron1, neurite1 in neuron_neurite_Tuples:
    for neuron2, neurite2 in neuron_neurite_Tuples:
      if (neuron1 != neuron2): 
        dist = closestPoints(neurite1, neurite2)[2]
        if (dist <= epsilon):
          distance = edgeLength(G, neuron1, neuron2)
          G.add_edge(neuron1, neuron2, distance=distance)
  print('Number of Edges in Fully Connected SEEM Graph: ', G.number_of_edges())
  return G

def seemInstance(edgeCount: int, FC_Graph):
  if FC_Graph.number_of_edges() < edgeCount:
    print('ERROR: edge count too high')
    return False

  rng = random.default_rng()
  keptEdges = rng.choice(list(FC_Graph.edges().data()), size=edgeCount, replace=False)
  
  G = getCleanGraph()

  G.add_edges_from(keptEdges)

  return G

def generateInstances(edgeCount: int, n: int, FC_Graph):
  return [seemInstance(edgeCount, FC_Graph) for i in range(n)]