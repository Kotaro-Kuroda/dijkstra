import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt', help='path to text file')
    parser.add_argument('--start', type=int, default=0, help='start node')
    parser.add_argument('--goal', type=int, default=0, help='goal node')
    args = parser.parse_args()
    return args


class Dijkstra:
    def __init__(self, vertices, distance_map):
        self.vertices = vertices
        self.distance_map = distance_map

    def shortest_path(self, start, goal):
        list_undefined_vertices = self.vertices
        list_defined_vertices = []
        list_path = {}
        while len(list_undefined_vertices) > 0:
            list_distance = [self.distance_map[start, i] for i in list_undefined_vertices]
            index = np.argmin(list_distance)
            vertex = list_undefined_vertices[index]
            shortest_distance = list_distance[index]
            self.distance_map[start][vertex] = self.distance_map[vertex][start] = shortest_distance
            list_defined_vertices.append(vertex)
            list_undefined_vertices.remove(vertex)
            for v in list_undefined_vertices:
                if shortest_distance + self.distance_map[vertex][v] <= self.distance_map[start][v]:
                    self.distance_map[start][v] = self.distance_map[v][start] = shortest_distance + \
                        self.distance_map[vertex][v]
                    list_path[v] = vertex
        return list_path, self.distance_map[start][goal]


def show_graph(distance_map):
    G = nx.Graph()
    edge_labels = {}
    for i in range(len(distance_map) - 1):
        for j in range(i + 1, len(distance_map)):
            distance = distance_map[i][j]
            if distance < np.inf:
                G.add_weighted_edges_from([(i, j, distance)])
                edge_labels[(i, j)] = distance
    pos = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='white', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=1)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, label_pos=0.3, edge_labels=edge_labels)
    plt.show()


def main():
    args = parse_args()
    text_file = open(args.txt, 'r', encoding='UTF-8')
    lines = text_file.readlines()
    num_vertices = int(lines[0])
    distance_map = np.ones((num_vertices, num_vertices)) * np.inf
    for i in range(num_vertices):
        distance_map[i][i] = 0
    for i in range(1, len(lines)):
        line = lines[i].split(',')
        distance_map[int(line[0])][int(line[1])] = distance_map[int(line[1])][int(line[0])] = int(line[2])

    list_vertices = [i for i in range(0, num_vertices)]

    show_graph(distance_map)
    start = args.start
    goal = args.goal
    dijkstra = Dijkstra(list_vertices, distance_map)
    path, distance = dijkstra.shortest_path(start, goal)
    shortest_path = str(goal)
    prev = goal
    while True:
        prev = path[prev]
        shortest_path = str(prev) + '→' + shortest_path
        if prev == start:
            break

    print(f'shortest distance:{distance}')
    print(f'shortest_path:{shortest_path}')


if __name__ == '__main__':
    main()
