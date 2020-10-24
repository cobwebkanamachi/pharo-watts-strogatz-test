import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

G1 = nx.watts_strogatz_graph(50,4,0.04);
plt.figure()
nx.draw_spring(G1)

plt.show()
for a in G1.edges():
  print(str(a[0]+1),'->',str(a[1]+1),',',end='')
