"""
UTILITY FUNCTIONS
=================
Vector mathematics, color utilities, and helper functions for the Pookalam project.
"""

import math

# =============================================================================
# VECTOR UTILITIES
# =============================================================================

def vector_length(p):
    """Calculate the length of a 2D vector."""
    return math.hypot(p[0], p[1])

def vector_subtract(a, b):
    """Subtract two 2D vectors."""
    return (a[0] - b[0], a[1] - b[1])

def vector_add(a, b):
    """Add two 2D vectors."""
    return (a[0] + b[0], a[1] + b[1])

def vector_multiply(a, k):
    """Multiply a 2D vector by a scalar."""
    return (a[0] * k, a[1] * k)

def vector_dot(a, b):
    """Calculate the dot product of two 2D vectors."""
    return a[0] * b[0] + a[1] * b[1]

def vector_normalize(a):
    """Normalize a 2D vector."""
    length = vector_length(a)
    if length == 0:
        return (0.0, 0.0)
    return (a[0] / length, a[1] / length)

def vector_rotate(p, degrees):
    """Rotate a 2D vector by given degrees."""
    radians = math.radians(degrees)
    cos_r = math.cos(radians)
    sin_r = math.sin(radians)
    return (p[0] * cos_r - p[1] * sin_r, p[0] * sin_r + p[1] * cos_r)

def calculate_signed_area(points):
    """Calculate the signed area of a polygon."""
    area = 0.0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return area / 2.0
