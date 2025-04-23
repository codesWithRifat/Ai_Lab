import random

GRID_SIZE = 20
POINT_COUNT = 100
CLUSTER_COUNT = 10
points = []
k_centers = []
visual_grid = []

def create_point(x, y):
    return {'x': x, 'y': y, 'cluster': -1}

def generate_data():
    global points, k_centers
    points = [create_point(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
              for _ in range(POINT_COUNT)]
    k_centers = [create_point(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
                 for _ in range(CLUSTER_COUNT)]

    with open('data.txt', 'w') as f:
        f.write("Points:\n")
        for p in points:
            f.write(f"{p['x']},{p['y']}\n")
        f.write("\nCluster Centers:\n")
        for c in k_centers:
            f.write(f"{c['x']},{c['y']}\n")

def manhattan_distance(p1, p2):
    return abs(p1['x'] - p2['x']) + abs(p1['y'] - p2['y'])

def assign_clusters():
    for p in points:
        min_dist = float('inf')
        cluster = -1
        for j, center in enumerate(k_centers):
            dist = manhattan_distance(p, center)
            if dist < min_dist:
                min_dist = dist
                cluster = j
        p['cluster'] = cluster

def update_centers():
    converged = True
    old_centers = [create_point(c['x'], c['y']) for c in k_centers]

    for j in range(CLUSTER_COUNT):
        cluster_points = [p for p in points if p['cluster'] == j]
        if not cluster_points:
            continue

        x_coords = sorted([p['x'] for p in cluster_points])
        y_coords = sorted([p['y'] for p in cluster_points])
        median_x = x_coords[len(x_coords) // 2]
        median_y = y_coords[len(y_coords) // 2]


        if k_centers[j]['x'] != median_x or k_centers[j]['y'] != median_y:
            converged = False
            k_centers[j]['x'] = median_x
            k_centers[j]['y'] = median_y

    return converged


def calculate_intra_distances():
    for j in range(CLUSTER_COUNT):
        total = 0
        for p in points:
            if p['cluster'] == j:
                total += manhattan_distance(p, k_centers[j])
        print(f"Cluster {j + 1} Intra-distance = {total}")


def create_visualization():
    global visual_grid
    visual_grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for p in points:
        x, y = p['x'], p['y']
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            visual_grid[x][y] = chr(ord('a') + p['cluster'])

    for j, c in enumerate(k_centers):
        x, y = c['x'], c['y']
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            visual_grid[x][y] = chr(ord('A') + j)

    # Print the grid
    print("\n2D Visualization (20x20 grid):")
    for y in reversed(range(GRID_SIZE)):
        print(' '.join([visual_grid[x][y] for x in range(GRID_SIZE)]))


def main():
    generate_data()
    iterations = 0

    while True:
        iterations += 1
        assign_clusters()
        converged = update_centers()
        if converged:
            break

    print(f"Converged after {iterations} iterations")
    calculate_intra_distances()
    create_visualization()


if __name__ == "__main__":
    main()