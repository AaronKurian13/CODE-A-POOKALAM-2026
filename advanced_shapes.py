"""
ADVANCED SHAPE FUNCTIONS
========================
Complex geometric shapes including rounded triangles and radial ellipses.
"""

import turtle
import math
from utils import (
    vector_length, vector_subtract, vector_add, vector_multiply,
    vector_dot, vector_normalize, vector_rotate, calculate_signed_area
)

# =============================================================================
# ROUNDED TRIANGLE FUNCTIONS
# =============================================================================

def draw_rounded_triangle_sides(center=(0, 0), sides=(4.0, 6.0, 8.0), radius=60,
                               rotation_deg=0, edge_color="#3478F6", fill_color="#FFA500",
                               thickness=18, step_deg=5, scale=50.0):
    """Draw a triangle with rounded corners using specified side lengths."""

    def draw_arc_for_triangle(t, center, radius, start_angle, end_angle, step=5):
        """Helper function to draw arcs for rounded triangles."""
        if step <= 0:
            step = 5
        direction = 1 if end_angle >= start_angle else -1
        angle = start_angle

        t.goto(center[0] + radius * math.cos(math.radians(angle)),
               center[1] + radius * math.sin(math.radians(angle)))
        t.pendown()

        while (direction == 1 and angle < end_angle) or (direction == -1 and angle > end_angle):
            angle += direction * min(step, abs(end_angle - angle))
            t.goto(center[0] + radius * math.cos(math.radians(angle)),
                   center[1] + radius * math.sin(math.radians(angle)))

    a, b, c = map(float, sides)
    if not (a + b > c and b + c > a and c + a > b):
        raise ValueError("Invalid triangle side lengths")

    # Calculate triangle vertices
    x = (a * a + c * c - b * b) / (2 * a)
    y_squared = c * c - x * x
    y = math.sqrt(max(0.0, y_squared))

    local_points = [(0.0, 0.0), (a, 0.0), (x, y)]
    local_points = [vector_rotate((px * scale, py * scale), rotation_deg) for (px, py) in local_points]

    cx, cy = center
    points = [vector_add(p, (cx, cy)) for p in local_points]

    if calculate_signed_area(points) < 0:
        points = [points[0], points[2], points[1]]

    n = 3
    arc_data = []

    for i in range(n):
        prev_idx = (i - 1) % n
        next_idx = (i + 1) % n
        current = points[i]
        prev_point = points[prev_idx]
        next_point = points[next_idx]

        u = vector_normalize(vector_subtract(prev_point, current))
        v = vector_normalize(vector_subtract(next_point, current))

        cos_theta = max(-1.0, min(1.0, vector_dot(u, v)))
        theta = math.acos(cos_theta)

        distance_limit = 0.45 * min(vector_length(vector_subtract(current, prev_point)),
                                   vector_length(vector_subtract(current, next_point)))
        nominal_distance = radius / max(1e-9, math.tan(theta / 2.0))
        distance = min(nominal_distance, distance_limit)

        effective_radius = distance * math.tan(theta / 2.0)
        start_point = vector_add(current, vector_multiply(u, distance))
        end_point = vector_add(current, vector_multiply(v, distance))

        bisector = vector_normalize(vector_add(u, v))
        center_distance = effective_radius / max(1e-9, math.sin(theta / 2.0))
        arc_center = vector_add(current, vector_multiply(bisector, center_distance))

        angle_start = math.degrees(math.atan2(start_point[1] - arc_center[1],
                                             start_point[0] - arc_center[0]))
        angle_end = math.degrees(math.atan2(end_point[1] - arc_center[1],
                                           end_point[0] - arc_center[0]))

        while angle_end <= angle_start:
            angle_end += 360.0

        arc_data.append((start_point, end_point, arc_center, effective_radius, angle_start, angle_end))

    # Draw the rounded triangle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(thickness)
    t.pencolor(edge_color)

    if fill_color is not None:
        t.fillcolor(fill_color)

    t.penup()
    t.goto(arc_data[0][0])
    t.pendown()

    if fill_color is not None:
        t.begin_fill()

    for i in range(n):
        _, _, arc_center, effective_radius, angle_start, angle_end = arc_data[i]
        draw_arc_for_triangle(t, arc_center, effective_radius, angle_start, angle_end, step_deg)
        next_start = arc_data[(i + 1) % n][0]
        t.goto(next_start)

    if fill_color is not None:
        t.end_fill()

    t.penup()

# =============================================================================
# RADIAL ELLIPSE FUNCTIONS
# =============================================================================

def draw_radial_ellipse(t, center_x, center_y, radius, stretch_factor, unit_x, unit_y, color, fill=True):
    """Draw an ellipse oriented radially outward from a center point."""
    t.pencolor(color)
    t.fillcolor(color)

    if fill:
        t.begin_fill()

    for angle_step in range(37):  
        angle = angle_step * 10
        radians = math.radians(angle)

        # Create ellipse in local coordinates
        local_x = radius * math.cos(radians) * stretch_factor
        local_y = radius * math.sin(radians)

        # Rotate to align with radial direction
        rotated_x = local_x * unit_x - local_y * unit_y
        rotated_y = local_x * unit_y + local_y * unit_x

        # Calculate final position
        final_x = center_x + rotated_x
        final_y = center_y + rotated_y

        if angle_step == 0:
            t.penup()
            t.goto(final_x, final_y)
            t.pendown()
        else:
            t.goto(final_x, final_y)

    if fill:
        t.end_fill()
