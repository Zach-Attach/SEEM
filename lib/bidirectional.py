def bidirectionalSubgraph(G):
  G_new = G.copy()
  G_new.remove_edges_from(
    filter(lambda e: e[0] not in G[e[1]], 
    G.edges())
    )
  return G_new

def bidirectionalSubgraphArray(Gs):
  return [bidirectionalSubgraph(G) for G in Gs]
