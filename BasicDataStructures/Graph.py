class Graph:
    def __init__(self):
        self.no_of_nodes = 0
        self.adj_list = {}

    def add_node(self, node):
        self.no_of_nodes = self.no_of_nodes + 1
        self.adj_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adj_list.keys():
            if node2 in self.adj_list.keys():
                self.adj_list[node1].append(node2)
                self.adj_list[node2].append(node1)
            else:
                print(str(node2) + " does not exist in graph")
        else:
            print(str(node1)+" does not exist in graph")


g = Graph()

g.add_node(3)
print(g.adj_list, g.no_of_nodes)
g.add_node(4)
g.add_edge(3, 2)
g.add_edge(2, 3)
g.add_node(2)
print(g.adj_list, g.no_of_nodes)
g.add_edge(2, 3)
g.add_edge(4, 3)
print(g.adj_list, g.no_of_nodes)
