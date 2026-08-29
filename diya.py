"""
DIYA DRAWING FUNCTIONS
=====================
Functions for drawing festive diyas with flames around the pookalam.
"""

import turtle
import math
from advanced_shapes import draw_radial_ellipse

# =============================================================================
# DIYA FLAME FUNCTIONS
# =============================================================================

def draw_diya_flames(t, x, y, center_x, center_y, radius, flame_colors, flame_count=5):
    """Draw flames emanating from a diya."""
    dx = x - center_x
    dy = y - center_y
    distance = math.sqrt(dx*dx + dy*dy)

    if distance > 0:
        unit_x = dx / distance
        unit_y = dy / distance
    else:
        unit_x, unit_y = 0, -1

    shift_distance = radius * 1.2
    flame_start_x = x + unit_x * shift_distance
    flame_start_y = y + unit_y * shift_distance

    for flame_idx in range(flame_count):
        flame_radius = radius * (flame_count - flame_idx) / (flame_count + 1)
        flame_x = flame_start_x - unit_x * flame_radius
        flame_y = flame_start_y - unit_y * flame_radius
        flame_color = flame_colors[flame_idx] if flame_idx < len(flame_colors) else flame_colors[-1]
        stretch_factor = 1 + flame_idx * 0.4

        draw_radial_ellipse(t, flame_x, flame_y, flame_radius, stretch_factor, unit_x, unit_y, flame_color)

def draw_single_diya(t, x, y, center_x, center_y, diya_radius, diya_color, flame_colors, flame_count=5):
    """Draw a complete diya with flames."""
    dx = x - center_x
    dy = y - center_y
    distance = math.sqrt(dx*dx + dy*dy)

    if distance > 0:
        unit_x = dx / distance
        unit_y = dy / distance
    else:
        unit_x, unit_y = 0, -1

    # Draw main diya body
    draw_radial_ellipse(t, x, y, diya_radius, 1.0, unit_x, unit_y, diya_color)
    # Draw flames
    draw_diya_flames(t, x, y, center_x, center_y, diya_radius, flame_colors, flame_count)

def draw_diyas_around_pookalam(center, pookalam_radius, diya_radius=25, diya_count=8,
                              diya_color="#582f0e", flame_colors=None, flame_count=4, start_angle=0):
    """Draw multiple diyas arranged around the pookalam."""
    if flame_colors is None:
        flame_colors = ["#260701", "#ffb20f", "#ffe548"]

    cx, cy = center
    ring_radius = pookalam_radius - diya_radius

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    angle_step = 360 / max(1, diya_count)
    for i in range(diya_count):
        angle = math.radians(start_angle + i * angle_step)
        x = cx + ring_radius * math.cos(angle)
        y = cy + ring_radius * math.sin(angle)
        draw_single_diya(t, x, y, cx, cy, diya_radius, diya_color, flame_colors, flame_count)
