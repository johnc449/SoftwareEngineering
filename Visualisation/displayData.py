
from pyvis.network import Network #for visuallising networks
import re    #for validat
import sqlite3
import os
colours = ["#000000","#00FF00","#0000FF","#FF0000","#01FFFE","#FFA6FE","#FFDB66","#006401","#010067",
"#95003A","#007DB5","#FF00F6","#FFEEE8","#774D00","#90FB92","#0076FF","#D5FF00","#FF937E","#6A826C",
"#FF029D","#FE8900","#7A4782","#7E2DD2","#85A900","#FF0056","#A42400","#00AE7E","#683D3B","#BDC6FF",
"#263400","#BDD393","#00B917","#9E008E","#001544","#C28C9F","#FF74A3","#01D0FF","#004754","#E56FFE",
"#788231","#0E4CA1","#91D0CB","#BE9970","#968AE8","#BB8800","#43002C","#DEFF74","#00FFC6","#FFE502"
"#620E00","#008F9C","#98FF52","#7544B1","#B500FF","#00FF78","#FF6E41","#005F39","#6B6882","#5FAD4E",
"#A75740","#A5FFD2","#FFB167","#009BFF","#E85EBE"] #selection of high contrast colours 
conn = sqlite3.connect('Visualisation/data.db')    #db address
colourDict = {}    #dict for giving each node a colour
net = Network(notebook=True)    
cursor = conn.execute("SELECT LABEL,COUNT,NEIGHBOURSBOOL from MAIN") #fecthes everything in main table
i = 0
for row in cursor:
    net.add_node(row[0],size=row[1]+10,title = "Label used "+str(row[1])+" times.") #creates nodes
    colourDict[row[0]] = colours[i%len(colours)]   #gives each node an edge colour
    i += 1
cursor = conn.execute("SELECT LABEL,COUNT,NEIGHBOURSBOOL from MAIN")
for row in cursor:
    if(int(row[2])==1):
        edgeCursor = conn.execute("SELECT LABEL,COUNT from {currentNode}".format(currentNode=re.sub("[^0-9a-zA-Z]+", "_",row[0])))
        for edgeRow in edgeCursor:
            if row[1] > edgeRow[1]:
              edgeColour = colourDict[row[0]]    #creates edges and uses colour from bigger node
            else:
              edgeColour = colourDict[edgeRow[0]]
            net.add_edge(row[0],edgeRow[0],width = edgeRow[1]*5,title = "Labels used together "+str(edgeRow[1])+" times.",
            color=edgeColour)
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
      "avoidOverlap": 0.5
    }
  }
}''')
net.show("Visualisation/Output.html")
conn.close()
os.system("start Visualisation/Output.html")