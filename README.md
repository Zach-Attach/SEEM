# SEEM
Spatial Embedded Edge Model for C. Elegans Neural Network

## Steps
1. convert.ipynb
    * convert data files into graphs
2. penpals.ipynb
    * find penpals for each neuron
3. edgeDistance.ipynb
    * find distance of each edge within a graph
4. SEEM.ipynb
    * run SEEM on each graph
5. overlap.ipynb
    * find overlaps between each pair of graphs

## Comparison Graph Creation  
RDDAM.ipynb - creates Random Distance Dependent Attachment Graphs  
random.ipynb - creates Random Graphs  

## Analysis Tools  
overlap.ipynb - looks at overlaps between graphs  
modules.ipynb - applies module/community detection algorithms to graphs  
stats.ipynb - calculates statistics for graphs  
display.ipynb - majority of plots are found here

## Data
* data/ - contains all the data files
    * **/compiled/ - contains the compiled graphs
    * **/original/ - contains the original graphs that are not manipulated or edited
    * **/source/ - contains the source files for the graphs
    * images/ - contains plot images
