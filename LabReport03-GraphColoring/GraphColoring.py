class GraphColoring:
    def __init__(self):
        self.V = 0
        self.numOfColors = 0
        self.color = []
        self.adj = []
        self.solution_found = False

    def graph_color(self, adj, noc):
        self.V = len(adj)
        self.numOfColors = noc
        self.color = [0] * self.V
        self.adj = adj

        self.solve(0)

        if not self.solution_found:
            print(f"Coloring Not Possible with {self.numOfColors} Colors")
        else:
            print(f"Coloring Possible with {self.numOfColors} Colors")
            print("Color Assignment:", self.color)

    def solve(self, v):
        if v == self.V:
            self.solution_found = True
            return True

        for c in range(1, self.numOfColors + 1):
            if self.is_possible(v, c):
                self.color[v] = c
                if self.solve(v + 1):
                    return True
                self.color[v] = 0

        return False

    def is_possible(self, v, c):
        for neighbor in self.adj[v]:
            if c == self.color[neighbor]:
                return False
        return True

# input file name you want to run
def read_input_from_file(filename="case1.txt"):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            N, M, K = map(int, lines[0].split())

            adj = [[] for _ in range(N)]

            for line in lines[1:M + 1]:
                u, v = map(int, line.split())
                adj[u].append(v)
                adj[v].append(u)

        return adj, K
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
        return None, None
    except Exception as e:
        print(f"Error reading input: {e}")
        return None, None


if __name__ == "__main__":
    adj, K = read_input_from_file()
    if adj is not None and K is not None:
        gc = GraphColoring()
        gc.graph_color(adj, K)
    else:
        print("Program terminated due to input error.")