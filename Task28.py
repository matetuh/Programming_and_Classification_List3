import nltk
import networkx
from nltk.corpus import stopwords
from nltk.book import text2
from string import punctuation
import matplotlib.pyplot as plt
import numpy as np

L = 300
S = 20

interpunction = str.maketrans("","", punctuation)
stopwords = set(stopwords.words('english'))
text_2 = [el.translate(interpunction) for el in text2 if not el in stopwords]
pairs = [(x, text2.count(x)) for x in set(text2)]
word = [x for x,y in pairs if y >= L and x != ""]

graph = networkx.Graph()
graph.add_nodes_from(word)

for elem1 in word:
    for elem2 in word:
        if elem1 != elem2:
            dist = nltk.edit_distance(elem1, elem2)
            if(dist <= S):
                graph.add_edge(elem1, elem2, distance = dist)

position = networkx.spring_layout(graph)
networkx.draw_networkx_nodes(graph, position, node_size = 35, node_color= 'red')
networkx.draw_networkx_edges(graph, position, width = 0.1, edge_color = 'green', style = 'dashed')
networkx.draw_networkx_labels(graph, position, font_size = 15)
plt.show()



