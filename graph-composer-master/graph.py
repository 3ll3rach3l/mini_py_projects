"""
Implemented Markov Chain Composer Graph object by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        self.value = value #value will be a word from the text
        self.adjacent = {}  # keeps track of which vertices are connect to this vertex, value will be the weight
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])
    
    #adding an edge to the vertex that we're inputing with some weight
    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    #whenever we see a word go to another word that's already in adjacent, we want to add 1
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 #if this vertex is a key, get the value. ot

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0] 



class Graph(object):
    def __init__(self):
        self.vertices = {} #string to vertex mapping

    #what are the values of all the vertices
    def get_vertex_values(self):
        return set(self.vertices.keys()) #return all possible words

    #when we encounter a new word, we want to add a vertex
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    #gets the vertext object
    def get_vertex(self, value):
        if value not in self.vertices: #if the value is not in the graph
            self.add_vertex(value) #obviously, add it
        return self.vertices[value]


    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self): #gets probability mappings for every single vertex
        for vertex in self.vertices.values():
            vertex.get_probability_map()
