#!/usr/bin/env python
"""Test URL parameter parsing"""

# Simulating what Flask receives
test_urls = [
    "[(1,1),(-1,-1),(2,3)]",  # Direct
    "%5B%281%2C1%29%2C%28-1%2C-1%29%2C%282%2C3%29%5D",  # URL encoded
]

for url_param in test_urls:
    print(f"\nTesting: {url_param}")
    try:
        # URL decode if needed
        from urllib.parse import unquote
        decoded = unquote(url_param)
        print(f"Decoded: {decoded}")

        locations = eval(decoded)
        print(f"Parsed: {locations}")
        print(f"Type: {type(locations)}")
        print(f"First item: {locations[0]}, type: {type(locations[0])}")
    except Exception as e:
        print(f"Error: {e}")

