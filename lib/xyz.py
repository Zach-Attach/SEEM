import csv

# location of file containing xyz coordinates of each neuron

input_positions = 'data/elegans-atlas/LowResAtlasWithHighResHeadsAndTails.csv'

# convert spatial location file to a dict of 3D coordinates
# - ex: `[ [1.1, 2.2]...]`

def getSpatialPositions(file):
  with open(file) as f:
    return {k:(float(x),float(y),float(z)) for k,x,y,z in csv.reader(f)}

NEURON_POSITIONS = getSpatialPositions(input_positions) # get spatial positions