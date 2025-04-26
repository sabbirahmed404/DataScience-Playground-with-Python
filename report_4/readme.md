# K-Means Clustering with Manhattan Distance

This project implements a modified K-Means clustering algorithm in Python. The objective is to cluster 100 randomly generated Cartesian points using 10 initial centroids, with the Manhattan distance metric used for calculating distances between points and centroids. Additionally, the clustered data is visualized in a 2D matrix format, where each cell represents a coordinate on the plane and displays either a data point or a cluster center.

## Features

- **Data Generation**: 100 Cartesian points and 10 initial centroids are generated randomly in the range [0, 20].
- **Manhattan Distance**: The distance metric used for clustering is the Manhattan distance, calculated as the sum of the absolute differences between the x and y coordinates.
- **K-Means Clustering**: The K-Means algorithm assigns points to the closest centroids, updates centroids, and iterates until convergence or a maximum of 100 iterations.
- **2D Visualization**: The final clusters and centroids are displayed in a simple 2D matrix format using Python’s `print()` function.

## Requirements

- Python 3.x
- No external libraries are required for this implementation.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/k-means-manhattan.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd k-means-manhattan
   ```

## Usage

1. To generate the data, run the Python script:
   ```bash
   python test.py
   ```

2. The script will:
   - Generate 100 random points and 10 initial centroids.
   - Perform K-Means clustering using the Manhattan distance metric.
   - Save the data to a file (`cluster_data.txt`).
   - Display the clustering results and centroids in a 2D matrix format.

## Output Example

The final output will look like this:

```
Data saved to 'cluster_data.txt'.

Clustered points with centroids visualized:
  C0     0     1  0 C1  2   2  
  1   C3  3  C4  0    0   C5  
  C6      3     4   0      

Final centroid locations:
Centroid C0: (5, 6)
Centroid C1: (12, 13)
Centroid C2: (2, 3)
Centroid C3: (8, 8)
Centroid C4: (15, 10)
Centroid C5: (11, 5)
Centroid C6: (1, 2)
Centroid C7: (18, 19)
Centroid C8: (7, 9)
Centroid C9: (13, 14)

The algorithm has converged.
```

