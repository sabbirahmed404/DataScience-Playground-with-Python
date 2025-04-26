import random

def generate_and_save_data(filename="cluster_data.txt"):
    points = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(100)]
    centroids = [(random.randint(0, 20), random.randint(0, 20)) for _ in range(10)]
    
    with open(filename, 'w') as f:
        f.write("Points:\n")
        for point in points:
            f.write(f"{point[0]},{point[1]}\n")
        
        f.write("\nCentroids:\n")
        for centroid in centroids:
            f.write(f"{centroid[0]},{centroid[1]}\n")
    
    return points, centroids

def load_data(filename="cluster_data.txt"):
    points = []
    centroids = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        points_section = False
        centroids_section = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line == "Points:":
                points_section = True
                centroids_section = False
                continue
            elif line == "Centroids:":
                points_section = False
                centroids_section = True
                continue
            if points_section:
                try:
                    x, y = map(int, line.split(','))
                    points.append((x, y))
                except ValueError:
                    print(f"Skipping invalid line in Points section: {line}")
            elif centroids_section:
                try:
                    x, y = map(int, line.split(','))
                    centroids.append((x, y))
                except ValueError:
                    print(f"Skipping invalid line in Centroids section: {line}")
    return points, centroids

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def kMeansClustering(points, centroids):
    assignments = [-1] * len(points)
    prev_centroids = centroids[:]
    
    max_iterations = 100
    converged = False
    
    for iteration in range(max_iterations):
        for i, point in enumerate(points):
            distances = [manhattan_distance(point, centroid) for centroid in centroids]
            closest_cluster = distances.index(min(distances))
            assignments[i] = closest_cluster
        
        new_centroids = []
        for i in range(len(centroids)):
            assigned_points = [points[j] for j in range(len(points)) if assignments[j] == i]
            if assigned_points:
                new_center = (sum(p[0] for p in assigned_points) // len(assigned_points), 
                              sum(p[1] for p in assigned_points) // len(assigned_points))
            else:
                new_center = centroids[i]
            new_centroids.append(new_center)
        
        if new_centroids == centroids:
            converged = True
            break
        else:
            centroids = new_centroids

    return points, centroids, assignments, converged

def visualize_clusters(points, centroids, assignments):
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for i, centroid in enumerate(centroids):
        x, y = centroid
        if 0 <= x <= max_x and 0 <= y <= max_y:
            grid[y][x] = f'C{i}'
    
    for i, point in enumerate(points):
        x, y = point
        cluster = assignments[i]
        if 0 <= x <= max_x and 0 <= y <= max_y:
            grid[y][x] = str(cluster)
    
    for row in grid:
        print(' '.join(row))

points, centroids = generate_and_save_data("cluster_data.txt")
print("Data saved to 'cluster_data.txt'.")

points, centroids = load_data("cluster_data.txt")

points, centroids, assignments, converged = kMeansClustering(points, centroids)
print("\nClustered points with centroids visualized:")
visualize_clusters(points, centroids, assignments)

print("\nFinal centroid locations:")
for i, centroid in enumerate(centroids):
    print(f"Centroid C{i}: {centroid}")
    
if converged:
    print("\nThe algorithm has converged.")
else:
    print("\nThe algorithm reached the maximum iterations without converging.")

