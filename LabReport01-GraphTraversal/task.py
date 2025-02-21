import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.moves = [(1, 0, "Moving Down"), (-1, 0, "Moving Up"), (0, 1, "Moving Right"), (0, -1, "Moving Left")]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0

    def pos(self, graph):
        while True:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if graph[x][y] == 1:
                return x, y

    def init(self):
        self.N = random.randint(4, 7)
        graph = []
        for i in range(self.N):
            row = []
            for j in range(self.N):
                row.append(random.choice([0, 1]))
            graph.append(row)
        print("N = ", self.N)
        print("Matrix:")
        for row in graph:
            print("[", end=" ")
            for value in row:
                print(value, end=" ")
            print("]")

        source_x, source_y = self.pos(graph)
        goal_x, goal_y = self.pos(graph)

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)
        print(f"\nSource: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})\n")
        print("Move required: ")
        self.st_dfs(graph, self.source)
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal cannot be reached from the starting block")

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for dx, dy, direction in self.moves:
            v_x = u.x + dx
            v_y = u.y + dy
            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                print(f"{direction} ({v_x}, {v_y})")
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal.depth = v_depth
                    return
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
                if self.found:
                    return

def main():
    d = DFS()
    d.init()

if __name__ == "__main__":
    main()
