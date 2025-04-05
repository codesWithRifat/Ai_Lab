class MazeSolver:
    def __init__(self, grid, start, target, rows, cols):
        self.grid = grid
        self.start = start
        self.target = target
        self.rows = rows
        self.cols = cols
        self.path = []
        self.goal_found = False

    def iddfs(self):
        max_possible_depth = self.rows + self.cols
        for depth in range(max_possible_depth):
            if self.dls(depth):
                print(f"Path found at depth {depth} using IDDFS")
                print(f"Traversal Order: {self.path}")
                return
        print(f"Path not found at max depth {max_possible_depth} using IDDFS")

    def dls(self, max_depth):
        stack = [(self.start, [self.start], 0)]
        while stack:
            current, path, depth = stack.pop()
            if current == self.target:
                self.path = path
                return True
            if depth < max_depth:
                x, y = current
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in reversed(directions):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.rows and 0 <= ny < self.cols:
                        if self.grid[nx][ny] == 0 and (nx, ny) not in path:
                            new_path = path + [(nx, ny)]
                            stack.append(((nx, ny), new_path, depth + 1))
        return False


def main():
    try:
        rows_cols = input().strip().split()
        rows, cols = int(rows_cols[0]), int(rows_cols[1])
        grid = []
        for _ in range(rows):
            row = list(map(int, input().strip().split()))
            grid.append(row)
        print("start:")
        start_input = input().strip().split()
        start = (int(start_input[0]), int(start_input[1]))
        print("Target:")
        target_input = input().strip().split()
        target = (int(target_input[0]), int(target_input[1]))
        # Solve
        solver = MazeSolver(grid, start, target, rows, cols)
        solver.iddfs()
    except Exception as e:
        print("Wrong Input format")


if __name__ == "__main__":
    main()