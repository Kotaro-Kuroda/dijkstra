import numpy as np


class Dijkstra:
    def __init__(self, vertices, distance_map, start, goal):
        self.vertices = vertices
        self.distance_map = distance_map
        self.start = start
        self.goal = goal

    def shortest_path(self):
        list_undefined_vertices = self.vertices
        list_defined_vertices = []
        list_path = {}
        while len(list_undefined_vertices) > 0:
            list_distance = [self.distance_map[self.start, i] for i in list_undefined_vertices]
            index = np.argmin(list_distance)
            vertex = list_undefined_vertices[index]
            shortest_distance = list_distance[index]
            self.distance_map[self.start][vertex] = self.distance_map[vertex][self.start] = shortest_distance
            list_defined_vertices.append(vertex)
            list_undefined_vertices.remove(vertex)
            for v in list_undefined_vertices:
                if shortest_distance + self.distance_map[vertex][v] <= self.distance_map[self.start][v]:
                    self.distance_map[self.start][v] = self.distance_map[v][self.start] = shortest_distance + \
                                                                                          self.distance_map[vertex][v]
                    list_path[v] = vertex
        return list_path, self.distance_map[self.start][self.goal]


def main():
    vertices = [i for i in range(0, 6)]
    distance_map = np.array(
        [[0, 3, 8, np.inf, np.inf, np.inf], [3, 0, np.inf, 4, 9, np.inf], [8, np.inf, 0, 7, 2, np.inf]
            , [np.inf, 4, 7, 0, np.inf, 8], [np.inf, 9, 2, np.inf, 0, 4], [np.inf, np.inf, np.inf, 8, 4, 0]])
    start = 0
    goal = 5
    dijkstra = Dijkstra(vertices, distance_map, start, goal)
    path, distance = dijkstra.shortest_path()
    shortest_path = str(goal)
    prev = goal
    while True:
        prev = path[prev]
        shortest_path = str(prev) + '→' + shortest_path
        if prev == start:
            break

    print(distance, shortest_path)


if __name__ == '__main__':
    main()
