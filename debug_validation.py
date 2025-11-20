#!/usr/bin/env python
"""Direct inline test of validation
Group 30
Oz Levi - 209999739
Inbar Kedem - 325298438
Eylon Chodnik - 325130417
"""

# Test data
locations_data = [(1, 1), (-1, -1), (2, 3)]

print("Testing validation inline:")
print(f"Input: {locations_data}")
print(f"Is list: {isinstance(locations_data, list)}")
print(f"Length > 0: {len(locations_data) > 0}")

for i, point in enumerate(locations_data):
    print(f"\nPoint {i}: {point}")
    print(f"  Is tuple or list: {isinstance(point, (list, tuple))}")
    print(f"  Length == 2: {len(point) == 2}")
    if len(point) == 2:
        print(f"  Coord 0: {point[0]}, is int/float: {isinstance(point[0], (int, float))}, not bool: {not isinstance(point[0], bool)}")
        print(f"  Coord 1: {point[1]}, is int/float: {isinstance(point[1], (int, float))}, not bool: {not isinstance(point[1], bool)}")

# Now test the actual function
def validate_input(locations_data):
    if not isinstance(locations_data, list):
        return False
    if len(locations_data) == 0:
        return False
    for point in locations_data:
        if not isinstance(point, (list, tuple)) or len(point) != 2:
            return False
        if not all(isinstance(coord, (int, float)) and not isinstance(coord, bool) for coord in point):
            return False
    return True

result = validate_input(locations_data)
print(f"\nValidation result: {result}")

