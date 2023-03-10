import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from lib.positions import getPositions

# Plot Graphs with Neuron Positions

## 2D

def plot2D(G, darkmode=False, labels=False):
  # plt.figure(facecolor='black')
  faceColor, edgeColor = ('black', 'white') if darkmode else ('white', 'black')
  plt.rcParams['axes.facecolor'] = faceColor
  plt.figure(figsize=(16, 8), dpi=80)
  nx.draw_networkx(G,getPositions(G),node_size=100, with_labels=labels, edge_color=edgeColor, node_color='red')

## 3D

# TODO: Clean this up
def plot3D(Gs, titles, filename, darkmode=True, nodeColors=[]):

  titles2 = [titles[2],'',
            titles[4],'',
            titles[0],'',
            titles[1],'',
            titles[3], ]

  if darkmode:
    edgeColor, nodeTraceColor, bgColor = 'white', 'black', 'black'
  else:
    edgeColor, nodeTraceColor, bgColor = 'black', 'white', 'white'
  
  fig = make_subplots(rows=3, cols=3, vertical_spacing=0, horizontal_spacing=0, subplot_titles=titles2, specs=[[{'type': 'scene'},    {'type': 'scene'},{'type': 'scene'}],
                           [{'type': 'scene'}, {'type': 'scene'},{'type': 'scene'}], [{'type': 'scene'}, {'type': 'scene'},{'type': 'scene'}]])
  fig2 = make_subplots(rows=3, cols=3, vertical_spacing=0, horizontal_spacing=0, subplot_titles=titles2, specs=[[{'type': 'scene'},    {'type': 'scene'},{'type': 'scene'}],
                           [{'type': 'scene'}, {'type': 'scene'},{'type': 'scene'}], [{'type': 'scene'}, {'type': 'scene'},{'type': 'scene'}]])

  for n, (G, title, nodeColor) in enumerate(zip(Gs, titles, nodeColors)):
    #We also need a list of edges to include in the plot
    edge_list = G.edges()
    nodeDict = G.nodes(True)

    #we  need to create lists that contain the starting and ending coordinates of each edge.
    x_edges=[]
    y_edges=[]
    z_edges=[]
    
    #need to fill these with all of the coordiates
    for edge in edge_list:
        node_i = edge[0]
        node_j = edge[1]

        #format: [beginning,ending,None]
        x_coords = [nodeDict[node_i]['x'],nodeDict[node_j]['x'],None]
        x_edges += x_coords
    
        y_coords = [nodeDict[node_i]['y'],nodeDict[node_j]['y'],None]
        y_edges += y_coords
    
        z_coords = [nodeDict[node_i]['z'],nodeDict[node_j]['z'],None]
        z_edges += z_coords
    #create a trace for the edges
    trace_edges = go.Scatter3d(x=x_edges, y=y_edges, z=z_edges, mode='lines', opacity=0.5,
                          line=dict(color=edgeColor, width=2), hoverinfo='none')

    #we need to seperate the X,Y,Z coordinates for Plotly
    x_nodes = list(nx.get_node_attributes(G,'x').values()) # x-coordinates of nodes
    y_nodes = list(nx.get_node_attributes(G,'y').values()) # x-coordinates of nodes
    z_nodes = list(nx.get_node_attributes(G,'z').values()) # x-coordinates of nodes
    
    #create a trace for the nodes
    trace_nodes = go.Scatter3d(x=x_nodes,
                            y=y_nodes,
                            z=z_nodes,
                            mode='markers',
                            marker=dict(symbol='circle',
                                        color=nodeColor,
                                        size=10,
                                        line=dict(color=nodeTraceColor, width=0.5))
                                        )
    # we need to set the axis for the plot 

    #also need to create the layout for our plot
    mapping = [(2,2),(1,1),(1,3),(3,1),(3,3)]
    fig.add_trace(
      trace_edges,
      row=mapping[n][0], col=mapping[n][1]
    )

    fig.add_trace(
      trace_nodes,
      row=mapping[n][0], col=mapping[n][1]
    )

    # fig = go.Figure(data=data, layout=layout)
    # fig.show()
    # fig.write_image(f'data/images/3D/{filename}.png')

    fig2.add_trace(
      trace_edges,
      row=mapping[n][0], col=mapping[n][1]
    )

    fig2.add_trace(
      trace_nodes,
      row=mapping[n][0], col=mapping[n][1]
    )

    # fig2.show()
    # fig2.write_image(f'data/images/3D/{filename}_middle.png')
    # return fig

  axis = dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title='')

  # layout = go.Layout(#title=title,
  #               width=650,
  #               height=625,
  #               showlegend=False, #True,
  #               scene=dict(xaxis=dict(axis), yaxis=dict(axis), zaxis=dict(axis)),
  #               margin=dict(t=100),
  #               hovermode='closest',
  #               paper_bgcolor=bgColor)
  
  fig.update_layout(#title=title,
              width=900,
              height=900,
              showlegend=False, #True,
              scene1={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene2={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene3={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene4={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene5={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene6={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene7={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene8={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              scene9={'xaxis':axis, 'yaxis':axis, 'zaxis':axis, 'camera':{'eye': {'x': 1.75, 'y': 1, 'z': 1}}},
              margin=dict(t=30, b=0, l=0, r=0),
              hovermode='closest',
              paper_bgcolor=bgColor)

  name = 'default'
  # Default parameters which are used when `layout.scene.camera` is not provided
  camera = dict(
    # up=dict(x=0.2, y=0.85, z=0.1),
    # center=dict(x=0, y=0, z=0),
    eye=dict(x=1.7, y=0, z=0)
  )
  axis = dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title='')

  fig2.update_layout(#title=title,
                width=900,
                height=900,
                showlegend=False, #True,
                scene1={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene2={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene3={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene4={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene5={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene6={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene7={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene8={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                scene9={'xaxis':axis, 'yaxis':axis, 'zaxis':axis},
                margin=dict(t=30, b=0, l=0, r=0),
                hovermode='closest',
                paper_bgcolor=bgColor)

  fig2.update_layout(scene_camera=camera)#, title=title

  fig2.layout.scene1.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene1.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene2.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene2.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene3.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene3.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene4.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene4.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene5.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene5.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene6.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene6.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene7.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene7.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene8.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene8.camera.center = dict(x=0, y=-0.25, z=0)
  fig2.layout.scene9.camera.eye = dict(x=1.7, y=0, z=0)
  fig2.layout.scene9.camera.center = dict(x=0, y=-0.25, z=0)

  # fig2.layout.scene1.camera.eye = dict(x=1.7, y=0, z=0)
    
  fig.write_image(f'data/images/3D/{filename}.png')
  fig2.write_image(f'data/images/3D/{filename}_middle.png')

  fig.show()
  fig2.show()

# Multi Bar Plot

def multiBarPlot(dims, data, subtitles, title, figsize, maxX=None, maxY=None, save=None):
  rows, cols = dims
  fig,axes = plt.subplots(rows, cols, figsize=figsize)
  plt.rcParams.update({'font.size': 12})
  fig.suptitle(title, fontsize=18)
  colors = ['red','#1f77b4','#ff7f0e','#2ca02c', '#9467bd']
  if cols == 1:
    for i in range(rows):
      axes[i].bar(*data[i*cols],color=colors[i*cols])
      axes[i].set_title(subtitles[i*cols])
      if maxX:
        axes[i].set_xlim(0, maxX)
      if maxY:
        axes[i].set_ylim(0, maxY)
  else:
    for j in range(cols):
      for i in range(rows):
          indx = j*rows+i
          if indx >= len(data):
            break
          axes[i,j].bar(*data[indx], color=colors[indx])
          axes[i,j].set_title(subtitles[indx])
          if maxX:
            axes[i,j].set_xlim(0, maxX)
          if maxY:
            axes[i,j].set_ylim(0, maxY)
  
  if save:
    plt.savefig(save)

  plt.show()

def multiLinePlot():
  fig,axes = plt.subplots(rows, cols, figsize=figsize)
  plt.rcParams.update({'font.size': 12})
  fig.suptitle(title, fontsize=18)
  colors = ['red','#1f77b4','#ff7f0e','#2ca02c', '#9467bd']
  if cols == 1:
    for i in range(rows):
      axes[i].bar(*data[i*cols],color=colors[i*cols])
      axes[i].set_title(subtitles[i*cols])
      if maxX:
        axes[i].set_xlim(0, maxX)
      if maxY:
        axes[i].set_ylim(0, maxY)
  else:
    for j in range(cols):
      for i in range(rows):
          indx = j*rows+i
          if indx >= len(data):
            break
          axes[i,j].bar(*data[indx], color=colors[indx])
          axes[i,j].set_title(subtitles[indx])
          if maxX:
            axes[i,j].set_xlim(0, maxX)
          if maxY:
            axes[i,j].set_ylim(0, maxY)
  
  if save:
    plt.savefig(save)

  plt.show()