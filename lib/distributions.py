# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
from lib.colors import color

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
  plt.rcParams.update({'font.size': 16})
  plt.figure(figsize=(10, 4))
  plt.title(f'Wasserstein Distances from CENN {measure} Distribution ({version})')
  plt.bar(keys, wass, color=[color[k] for k in keys])
  plt.savefig(f'data/images/compareDistributions/wassersteinDistances_{measure}_{version}_3.png', dpi=300)
  plt.show()
  # print(f'''Wasserstein Distances for {measure} Distributions ({version})
  #   SEEM-CENN: {wasserstein_dist(distributions['SEEM'],distributions['CENN'])}
  #   RDDAM-CENN: {wasserstein_dist(distributions['RDDAM'],distributions['CENN'])}
  #   ERN-CENN: {wasserstein_dist(distributions['ERN'],distributions['CENN'])}
  # ''')
