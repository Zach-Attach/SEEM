# %% [markdown]
# ### Distance Distribution

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
def distanceSequence(G, title='Degree Distribution', presentation=True, subplot=False):

  if presentation:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  distance_sequence = sorted((round(d) for n, m, d in G.edges(data='distance')), reverse=True)




  bars = np.unique(distance_sequence, return_counts=True)
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
    plt.xlabel("Edge Distance (µm)")
    plt.ylabel("# of Edges")

# %%
def avgDistDist(Gs: list, title: str = 'Distance Distribution', presentation: bool = True, subplot: bool = False):

  if presentation:
    plt.style.use('dark_background')
  else:
    plt.style.use('default')

  distances = []
  for graph in Gs:
    for n, m, d in graph.edges(data='distance'):
      distances.append(round(d))

  # print('LEN: ',len(distances))
  # print('MAX', max(distances))
  # print('AVG: ', sum(distances)/len(distances))

  dist_sequence = sorted(distances, reverse=True)
  dist, vals = np.unique(dist_sequence, return_counts=True)

  vals = [v/len(Gs) for v in vals]

  if subplot:
    return dist, vals
  else:
    plt.figure(figsize=(8, 8))

    plt.bar(dist, vals)
    plt.title(title)
    plt.xlabel("Edge Distance")
    plt.ylabel("# of Nodes")

# %%



