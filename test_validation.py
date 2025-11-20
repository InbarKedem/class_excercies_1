#!/usr/bin/env python
"""Test validation with negative numbers
Group 30
Oz Levi - 209999739
Inbar Kedem - 325298438
Eylon Chodnik - 325130417
"""

def validate_input(locations_data):
    """
    Validates that input is a list of tuples/lists,
    contains only numbers, and has dimension 2.
    Accepts both positive and negative numbers.
    """
    if not isinstance(locations_data, list):
        return False
    if len(locations_data) == 0:
        return False
    for point in locations_data:
        # Check if point is tuple or list and has exactly 2 coordinates
        if not isinstance(point, (list, tuple)) or len(point) != 2:
            return False
        # Check if coordinates are numbers (int or float) - both positive and negative
        if not all(isinstance(coord, (int, float)) and not isinstance(coord, bool) for coord in point):
            return False
    return True

# Test cases
test_cases = [
    ([(1, 1), (-1, -1), (2, 3)], True, "Mixed positive and negative"),
    ([(0, 0)], True, "Single point at origin"),
    ([(1.5, -2.5)], True, "Float coordinates"),
    ([], False, "Empty list"),
    ([(1, 2, 3)], False, "3D point"),
    ([(1, "a")], False, "Non-numeric coordinate"),
]

for test_input, expected, description in test_cases:
    result = validate_input(test_input)
    status = "✓" if result == expected else "✗"
    print(f"{status} {description}: {test_input} -> {result} (expected {expected})")

