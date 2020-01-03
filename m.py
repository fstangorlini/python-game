import networkx as nx
import random

class M:
    
    def __init__(self, depth):
        self.depth = depth
        self.m = nx.Graph()
        nodes = []
        seq = 1
        # Populate nodes
        for i in range(0,depth):
            nodes.append(seq)
            seq += 1
        
        # Put nodes in graph
        self.m.add_nodes_from(nodes)
        
        # Add edges
        for node in self.m: self._add_random_edges_(self.m,node)
        
        # Find longest path
        longest_path = self._find_longest_path_(self.m)
        
        # Sets start and end nodes
        self.start = longest_path[0]
        self.end   = longest_path[len(longest_path)-1]
        
#        print('start:',start)
#        print('end:',end)
#        nx.draw(m, with_labels=True, font_color='w', node_size=700)
        
    def _add_random_edges_(self, graph, source_node):
        r = random.choices(population=[1,2,3],weights=[0.4, 0.4, 0.2],k=1)[0]
        l = []
        nodes = []
        for n in graph: nodes.append(n)
        for i in range(r):
            while True:
                t = random.choice(nodes)
                if((t not in l)&(t!=source_node)):
                    l.append(t)
                    break
        for target in l:
            graph.add_edge(source_node,target)
        return
    
    def _find_longest_path_(self, graph):
        longest_path = []
        for i in range(1,len(graph)):
            for j in range(i,len(graph)):
                current_path = nx.shortest_path(self.m,i,j)
                if len(longest_path) < len(current_path): longest_path = current_path
        return longest_path
    
    def print_m(self):
        nx.draw(self.m, with_labels=True, font_color='w', node_size=700)
