
from pyvis.network import Network
import networkx as nx
import sqlite3
import os
conn = sqlite3.connect('Visualisation/data.db')

net = Network(notebook=True)
cursor = conn.execute("SELECT LABEL,COUNT,NEIGHBOURSBOOL from MAIN")
for row in cursor:
    net.add_node(row[0],size=row[1]+10,title = "Label used "+str(row[1])+" times.")
cursor = conn.execute("SELECT LABEL,COUNT,NEIGHBOURSBOOL from MAIN")
for row in cursor:
    if(int(row[2])==1):
        edgeCursor = conn.execute("SELECT LABEL,COUNT from {currentNode}".format(currentNode=row[0].replace(" ","_")))
        for edgeRow in edgeCursor:
            net.add_edge(row[0],edgeRow[0],width = edgeRow[1]*5,title = "Labels used together "+str(edgeRow[1])+" times.")
print("Graph created")
net.set_options('''var options = {
  "nodes": {
    "font": {
      "color": "rgba(0,0,0,1)",
      "size": 18,
      "background": "rgba(249,255,86,1)"
    },
    "scaling": {
      "max": 41
    }
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "physics": {
    "minVelocity": 0.75,
    "barnesHut": {
      "springConstant": 0,
      "avoidOverlap": 0.2
    }
  }
}''')
net.show("Visualisation/Output.html")
conn.close()
os.system("start Visualisation/Output.html")


