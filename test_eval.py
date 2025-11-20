#!/usr/bin/env python
"""Test eval with negative numbers
Group 30
Oz Levi - 209999739
Inbar Kedem - 325298438
Eylon Chodnik - 325130417
"""

test_strings = [
    "[(1, 1), (-1, -1), (2, 3)]",
    "[(1,1),(-1,-1),(2,3)]",
]

for test_str in test_strings:
    print(f"\nTesting: {test_str}")
    try:
        result = eval(test_str)
        print(f"  Success: {result}")
        print(f"  Type: {type(result)}")
        print(f"  Item 0: {result[0]}, type: {type(result[0])}")
        print(f"  Item 1: {result[1]}, type: {type(result[1])}")
    except Exception as e:
        print(f"  Error: {e}")
        print(f"  Error type: {type(e).__name__}")

