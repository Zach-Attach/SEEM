from networkx import DiGraph
import numpy as np
from lib.neurites import findSEEMNeurites
from lib.seem import fullyConnectedGraph, generateInstances
from scipy.stats import wasserstein_distance

def createDistributions(dist1, dist2) -> tuple:
    maxDist = max([max(dist1[0]), max(dist2[0])])

    newDist1, newDist2 = np.zeros(maxDist+1), np.zeros(maxDist+1)
    totalDist1, totalDist2 = sum(dist1[1]), sum(dist2[1])

    for i in range(maxDist+1):
      newDist1[i] = dist1[1][list(dist1[0]).index(i)]/totalDist1 if i in dist1[0] else 0
      newDist2[i] = dist2[1][list(dist2[0]).index(i)]/totalDist2 if i in dist2[0] else 0

    return newDist1, newDist2

def evaluateFitness(neurites: dict, epsilon: float, edgeCount: int, func, comparisonG) -> float:
  n: int = 100

  FCG: DiGraph = fullyConnectedGraph(neurites, epsilon)
  Gs: list = generateInstances(edgeCount, n, FCG)
  dist: tuple = func(Gs, presentation=False, subplot=True)

  wass: float = wasserstein_distance(*createDistributions(dist,comparisonG))

  return wass

def optimizeEpsilon(neurites: dict, epsilons: list, edgeCount: int, func, comparisonG):
  bestEpsilon: float = 0.0
  bestFitness: float = 1.0
  fitnessDict: dict = {}

  for e in epsilons:
    fitness: float = evaluateFitness(neurites, e, edgeCount, func, comparisonG)
    fitnessDict[e] = fitness
    if fitness < bestFitness:
      bestFitness = fitness
      bestEpsilon = e
  
  return bestEpsilon, bestFitness, fitnessDict