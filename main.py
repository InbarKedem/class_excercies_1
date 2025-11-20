from flask import Flask, request, render_template, redirect, url_for
import math
import itertools

app = Flask(__name__)


def calculate_distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def validate_input(locations_data):
    """
    Validates that input is a list of tuples/lists,
    contains only numbers, and has dimension 2.
    """
    if not isinstance(locations_data, list):
        return False
    if len(locations_data) == 0:
        return False
    for point in locations_data:
        # Check if point is tuple or list and has exactly 2 coordinates
        if not isinstance(point, (list, tuple)) or len(point) != 2:
            return False
        # Check if coordinates are numbers (int or float)
        if not all(isinstance(coord, (int, float)) for coord in point):
            return False
    return True


@app.route('/')
def home():
    # Check if 'locations' parameter exists in URL
    locations_str = request.args.get('locations')

    # If no locations are provided, render the Home Page
    if locations_str is None:
        return render_template('home_page.html')

    # If locations ARE provided, process the TSP logic
    try:
        # Parse the input string using eval() as suggested
        # Note: In a production environment, ast.literal_eval is safer,
        # but we are following the assignment hints.
        locations = eval(locations_str)

        # Validate Input
        if not validate_input(locations):
            raise ValueError("Invalid input format")

        # TSP Logic
        start_node = (0, 0)
        min_distance = float('inf')
        best_path = []

        # Generate all permutations of the locations
        # We fix the start/end at (0,0), so we permute the destinations
        for perm in itertools.permutations(locations):
            current_path = [start_node] + list(perm) + [start_node]
            current_dist = 0

            # Calculate total distance for this permutation
            for i in range(len(current_path) - 1):
                current_dist += calculate_distance(current_path[i], current_path[i + 1])

            # Check if this is the shortest path
            if current_dist < min_distance:
                min_distance = current_dist
                best_path = current_path

        # Prepare data for the table
        # Steps format: (Index, From, To)
        steps = []
        for i in range(len(best_path) - 1):
            steps.append({
                "id": i + 1,
                "from": best_path[i],
                "to": best_path[i + 1]
            })

        # Render Results Page
        return render_template(
            'results.html',
            distance=f"{min_distance:.3f}",
            steps=steps
        )

    except Exception:
        # In case of any error (parsing or logic), show error message
        return render_template('results.html', error=True)


# Handle 404 errors by redirecting to home page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

