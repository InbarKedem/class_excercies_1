from flask import Flask, request, render_template, redirect, url_for
import math
import itertools

app = Flask(__name__)


def calculate_distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    return math.dist(p1, p2)


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

    # [cite_start]If no locations are provided, render the Home Page [cite: 38]
    if locations_str is None:
        return render_template('home_page.html')

    # If locations ARE provided, process the TSP logic
    try:
        # [cite_start]Parse the input string using eval() as suggested [cite: 63]
        # Note: In a production environment, ast.literal_eval is safer,
        # but we are following the assignment hints.
        locations = eval(locations_str)

        # [cite_start]Validate Input [cite: 30, 31]
        if not validate_input(locations):
            raise ValueError("Invalid input format")

        # TSP Logic
        [cite_start]
        start_node = (0, 0)  # [cite: 8]
        min_distance = float('inf')
        best_path = []

        # [cite_start]Generate all permutations of the locations [cite: 61]
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

        # [cite_start]Prepare data for the table [cite: 20]
        # Steps format: (Index, From, To)
        steps = []
        for i in range(len(best_path) - 1):
            steps.append({
                "id": i + 1,
                "from": best_path[i],
                "to": best_path[i + 1]
            })

        # [cite_start]Render Results Page [cite: 54]
        return render_template(
            'results.html',
            [cite_start]
        distance = f"{min_distance:.3f}",  # Round to 3 decimal places [cite: 17]
        steps = steps
        )

        except Exception:
        # [cite_start]In case of any error (parsing or logic), show error message [cite: 33, 64]
        return render_template('results.html', error=True)


# [cite_start]Handle 404 errors by redirecting to home page [cite: 35]
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)