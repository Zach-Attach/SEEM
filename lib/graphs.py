import networkx as nx

G_Witvliet = [nx.read_gexf(f'data/Witvliet/d{i}/original/xyz_d.gexf') for i in range(1,9)]

G_White = nx.read_gexf(f'data/white/N2U/original/xyz_d.gexf')

G_Kaiser = nx.read_gexf('data/Kaiser/131/original/xyz_d.gexf')
G_Kaiser_PenPals = nx.read_gexf('data/Kaiser/131/compiled/xyzp.gexf')

G_SEEM_FC = nx.read_gexf(f'data/kaiser/131/compiled/xyzp_d_SEEM_FC.gexf')
G_overlap = nx.read_gexf(f'data/kaiser/131/Comparison/K131_Overlap.gexf')
G_uniqueOG = nx.read_gexf(f'data/kaiser/131/Comparison/K131_Unique_OG.gexf')
G_uniqueSEEM = nx.read_gexf(f'data/kaiser/131/Comparison/K131_Unique_SEEM.gexf')

G_overlap_W1 = nx.read_gexf('data/overlaps/W131_Overlap.gexf')
G_uniqueOG_W1 = nx.read_gexf('data/witvliet/d1/compiled/Comparison/W131_Unique_OG_W1.gexf')
G_uniqueSEEM_W1 = nx.read_gexf('data/witvliet/d1/compiled/Comparison/W131_Unique_SEEM_W1.gexf')

dataDir_Overlaps = 'data/overlaps'
G_overlap_W7_W8 = nx.read_gexf(f'{dataDir_Overlaps}/overlap_W7_W8.gexf')
G_overlap_W7_White = nx.read_gexf(f'{dataDir_Overlaps}/overlap_W7_White.gexf')
G_overlap_W8_White = nx.read_gexf(f'{dataDir_Overlaps}/overlap_W8_White.gexf')
G_overlap_W7_W8_White = nx.read_gexf(f'{dataDir_Overlaps}/overlap_W7_W8_White.gexf')
G_unique_W7 = nx.read_gexf(f'{dataDir_Overlaps}/unique_W7.gexf')
G_unique_W8 = nx.read_gexf(f'{dataDir_Overlaps}/unique_W8.gexf')
G_unique_White = nx.read_gexf(f'{dataDir_Overlaps}/unique_White.gexf')

def getCleanGraph():
  return nx.create_empty_copy(G_Witvliet[7])