import matplotlib.pyplot as plt
import numpy as np

# Degree Sequences

def degreeSequence(G, title='Degree Distribution', presentation=True, subplot=False):

  if presentation:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  degree_sequence = sorted((d for n, d in G.degree()), reverse=True)

  bars = np.unique(degree_sequence, return_counts=True)
  if subplot:
    return bars
  else:
    plt.figure(figsize=(8, 8)) #, facecolor='black')
    # plt.rcParams.update({'text.color': "white",
    #                    'axes.labelcolor': "white",
    #                    'axes.edgecolor': "white"})

    # ax = plt.axes()
    # ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
    # ax.tick_params(axis='y', colors='white')

    plt.bar(*bars)
    plt.title(title)
    plt.xlabel("Degree")
    plt.ylabel("# of Nodes")


# Average Degree Distribution

def avgDegDist(G, title= 'Degree Distribution', presentation=True, subplot=False):

  if presentation:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  degrees = []
  for graph in G:
    degrees += dict(graph.degree()).values()

  degree_sequence = sorted(degrees, reverse=True)
  degs, vals = np.unique(degree_sequence, return_counts=True)

  vals = [v/len(G) for v in vals]

  if subplot:
    return (degs, vals)

  plt.figure(figsize=(8, 8))

  plt.bar(degs, vals)
  plt.title(title)
  plt.xlabel("Degree")
  plt.ylabel("# of Nodes")




