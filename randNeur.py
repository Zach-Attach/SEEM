import pickle
from lib.neurites import findSEEMNeurites, EPSILON
import time

neurites_random = findSEEMNeurites(random=True)
pickle.dump(neurites_random, open(f'data/pickles/REEM/{time.time_ns()}.pkl', 'wb'))