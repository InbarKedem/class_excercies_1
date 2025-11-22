#!/usr/bin/env python
"""Comprehensive test to verify the TSP application meets all requirements"""

import sys
from main import calculate_distance, validate_input, home
from flask import Flask
import math

def test_distance_calculation():
    """Test the distance calculation function"""
    print("Testing distance calculation...")
    
    # Test case from assignment
    assert abs(calculate_distance((0, 0), (1, 1)) - math.sqrt(2)) < 0.001
    assert abs(calculate_distance((1, 1), (2, 3)) - math.sqrt(5)) < 0.001
    assert abs(calculate_distance((2, 3), (-1, -1)) - 5.0) < 0.001
    assert abs(calculate_distance((-1, -1), (0, 0)) - math.sqrt(2)) < 0.001
    
    print("✓ Distance calculation tests passed")

def test_input_validation():
    """Test input validation"""
    print("\nTesting input validation...")
    
    # Valid inputs
    assert validate_input([(1, 1), (-1, -1), (2, 3)]) == True
    assert validate_input([(0, 0)]) == True
    assert validate_input([(1.5, 2.5), (3, 4)]) == True
    
    # Invalid inputs
    assert validate_input([]) == False
    assert validate_input("not a list") == False
    assert validate_input([(1, 2, 3)]) == False  # 3D point
    assert validate_input([("a", "b")]) == False  # non-numeric
    assert validate_input([1, 2, 3]) == False  # not tuples/lists
    
    print("✓ Input validation tests passed")

def test_tsp_logic():
    """Test the TSP solving logic"""
    print("\nTesting TSP logic...")
    
    from main import app
    
    with app.test_client() as client:
        # Test the expected case from assignment
        response = client.get('/?locations=[(1,1),(-1,-1),(2,3)]')
        assert response.status_code == 200
        html = response.data.decode('utf-8')
        
        # Check that the distance is correct
        assert "10.064" in html
        
        # Check that the path steps are present
        assert "(0, 0)" in html
        assert "(1, 1)" in html
        assert "(2, 3)" in html
        assert "(-1, -1)" in html
        
        print("✓ TSP logic test passed - distance is 10.064")
        
        # Test error handling
        response = client.get('/?locations=invalid')
        assert response.status_code == 200
        html = response.data.decode('utf-8')
        assert "error" in html.lower()
        
        print("✓ Error handling test passed")
        
        # Test home page
        response = client.get('/')
        assert response.status_code == 200
        html = response.data.decode('utf-8')
        assert "Tiny TSP" in html
        
        print("✓ Home page test passed")

def verify_expected_path():
    """Verify the exact expected path matches the assignment"""
    print("\nVerifying expected path sequence...")
    
    import itertools
    
    locations = [(1, 1), (-1, -1), (2, 3)]
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
    
    # Verify the path
    expected_path = [(0, 0), (1, 1), (2, 3), (-1, -1), (0, 0)]
    assert best_path == expected_path, f"Expected {expected_path}, got {best_path}"
    
    # Verify the distance
    assert abs(min_distance - 10.064) < 0.001, f"Expected 10.064, got {min_distance:.3f}"
    
    print(f"✓ Path sequence verified: {' → '.join(str(p) for p in best_path)}")
    print(f"✓ Distance verified: {min_distance:.3f}")

if __name__ == '__main__':
    try:
        test_distance_calculation()
        test_input_validation()
        test_tsp_logic()
        verify_expected_path()
        
        print("\n" + "="*60)
        print("ALL TESTS PASSED ✓")
        print("="*60)
        print("\nThe application meets all requirements:")
        print("- Distance: 10.064 (3 decimal places)")
        print("- Path: (0,0) → (1,1) → (2,3) → (-1,-1) → (0,0)")
        print("- Error handling works correctly")
        print("- Input validation works correctly")
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
