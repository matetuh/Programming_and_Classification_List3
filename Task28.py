import nltk
import networkx
from nltk.corpus import stopwords
from string import punctuation
import matplotlib.pyplot as plt
import numpy as np
from nltk.book import text2


L = 200
S = 10

interpunction = str.maketrans("","", punctuation)
stopwords = set(stopwords.words('english'))
text_2 = [el.translate(interpunction) for el in text2 if not el in stopwords]
pairs = [(x, text2.count(x)) for x in set(text2)]
word = [x for x,y in pairs if y >= l and x != ""]

graph = networkx.Graph()
graph.add_nodes_from(word)

for elem1 in word:
    for elem2 in word:
        if elem1 != elem2:
            dist = nltk.edit_distance(elem1, elem2)
            if(d <= s):
                graph.add_edge(elem1, elem2, distance = dist)

position = nx.spring_layout(graph)
networkx.draw_networkx_nodes(graph, position, node_size = 35, node_color= 'green')
networkx.draw_networkx_edges(graph, position, width = 0.5, edge_color = 'b', style = 'dotted')
networkx.draw_networkx_labels(graph, position, font_size = 15)
plt.show()



