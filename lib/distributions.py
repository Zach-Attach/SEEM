# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
from lib.style import color

# %%

def wass(dist1, dist2) -> float:
    # NOTE: maxdist assumes int distribution for x axis
    maxDist = max([max(dist1[0]), max(dist2[0])])

    newDist1, newDist2 = np.zeros(maxDist+1), np.zeros(maxDist+1)
    totalDist1, totalDist2 = sum(dist1[1]), sum(dist2[1])

    for i in range(maxDist+1):
      newDist1[i] = dist1[1][list(dist1[0]).index(i)]/totalDist1 if i in dist1[0] else 0
      newDist2[i] = dist2[1][list(dist2[0]).index(i)]/totalDist2 if i in dist2[0] else 0

    return wasserstein_distance(newDist1, newDist2)
# %%
# create Distributions
def createDistributions(distSeqs):
    maxDist = max([max(ls[0]) for ls in distSeqs.values()])

    distributions = {}
    totalDist = {}
    for k in distSeqs.keys():
      distributions[k] = np.zeros(maxDist+1)
      totalDist[k] = sum(distSeqs[k][1])

    for i in range(maxDist+1):
      for key in distributions.keys():
          if i in distSeqs[key][0]:
              distributions[key][i] = distSeqs[key][1][list(distSeqs[key][0]).index(i)]/totalDist[key]
          else:
              distributions[key][i] = 0

    return distributions

# %%
# KL Divergence
from scipy.special import kl_div

#calculate (P || Q)

def kl_divergence(P,Q):
  return sum([(x if x != np.Inf else 0) for x in kl_div(P, Q)])


# %%
#calculate (P || Q)

def wasserstein_dist(P,Q):
  return wasserstein_distance(P, Q)

# %%

def wassersteinDistances(seq, measure, version):
  distributions = createDistributions(seq)
  keys = ['SEEM', 'RDDAM', 'ERN', 'REEM']

  wass = [wasserstein_distance(distributions[k],distributions['CENN']) for k in keys]

  plt.clf()
  plt.rcParams.update({'font.size': 6})
  plt.figure(figsize=(3, 4))
  plt.title(f'Wasserstein Distances from CENN {measure} Distribution ({version})', fontsize=6)
  plt.bar(keys, wass, color=[color[k] for k in keys])
  plt.savefig(f'data/images/compareDistributions/wassersteinDistances_{measure}_{version}_3.png', dpi=300)
  plt.show()
  # print(f'''Wasserstein Distances for {measure} Distributions ({version})
  #   SEEM-CENN: {wasserstein_dist(distributions['SEEM'],distributions['CENN'])}
  #   RDDAM-CENN: {wasserstein_dist(distributions['RDDAM'],distributions['CENN'])}
  #   ERN-CENN: {wasserstein_dist(distributions['ERN'],distributions['CENN'])}
  # ''')
