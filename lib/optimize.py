from lib.neurites import findSEEMNeurites
from lib.seem import fullyConnectedGraph

def evaluateFitness(neurites: dict, epsilon: float):
  FCG = fullyConnectedGraph(neurites, epsilon)
  

def optimizeEpsilon(epsilons: list):
  bestEpsilon = None
  bestFitness = 1.0

  for e in epsilons:
    fitness = evaluateFitness(e)
    if fitness < bestFitness:
      bestFitness = fitness
      bestEpsilon = e