#!/usr/bin/env python
"""Test script to verify TSP logic"""

import math
import itertools

def calculate_distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def solve_tsp(locations):
    """Solve TSP problem"""
    start_node = (0, 0)
    min_distance = float('inf')
    best_path = []

    for perm in itertools.permutations(locations):
        current_path = [start_node] + list(perm) + [start_node]
        current_dist = 0

        for i in range(len(current_path) - 1):
            current_dist += calculate_distance(current_path[i], current_path[i + 1])

        if current_dist < min_distance:
            min_distance = current_dist
            best_path = current_path

    return best_path, min_distance

# Test with the example from the assignment
locations = [(1, 1), (-1, -1), (2, 3)]
path, distance = solve_tsp(locations)

print("Test: locations =", locations)
print("Shortest path:", path)
print(f"Distance: {distance:.3f}")
print("\nTable:")
for i in range(len(path) - 1):
    print(f"{i+1}\t{path[i]}\t{path[i+1]}")

