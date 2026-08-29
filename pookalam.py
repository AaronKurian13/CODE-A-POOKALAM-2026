"""
MAIN POOKALAM DRAWING FUNCTIONS
===============================
Orchestrates all the components to create the complete pookalam design.
"""

import turtle
from shapes import (
    draw_filled_circle, draw_sectored_circle, draw_small_circles_ring,
    draw_repeating_triangle_pattern
)
from diya import draw_diyas_around_pookalam
from border import draw_circular_border
from sunflower import draw_phyllotactic_sunflower

# Global turtle instance 
main_turtle = turtle.Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)

# =============================================================================
# MAIN POOKALAM LAYERS
# =============================================================================

def draw_outer_rings():
    """Draw the outermost decorative rings of the pookalam."""
    draw_filled_circle(600, "#370617")

    draw_small_circles_ring(
        center=(0, 0), big_radius=580, small_radius=14, count=48,
        color="#4cc9f0", start_angle=11, inner_rings=3,
        inner_colors=["#4361ee", "#3a0ca3", "#6b0f9c", "#f72585"]
    )

    draw_small_circles_ring(
        center=(0, 0), big_radius=590, small_radius=120, count=12,
        color="#6a040f", start_angle=15, inner_rings=3,
        inner_colors=["#9d0208", "#d00000", "#6a040f"]
    )

def draw_triangle_layers():
    """Draw the layered triangular patterns."""
    triangle_patterns = [
        (580, "#DC2F02", 12),
        (560, "#E85D04", 12),
        (540, "#FAA307", 12),
        (520, "#FFBA08", 12),
        (500, "white", 12)
    ]

    for length, color, repeat_count in triangle_patterns:
        draw_repeating_triangle_pattern(length, color, repeat_count)
        main_turtle.right(3)

def draw_middle_section():
    """Draw the middle decorative section with circles and triangles."""
    draw_filled_circle(460, "#38b000")
    draw_filled_circle(445, "#fefae0")

    inner_patterns = [
        (440, "#7D82B8", 36),
        (400, "#613F75", 36),
        (360, "#03071e", 36)
    ]

    for length, color, repeat_count in inner_patterns:
        draw_repeating_triangle_pattern(length, color, repeat_count)

def draw_sectored_layers():
    """Draw the colorful sectored circular layers."""
    draw_filled_circle(330, "white")

    # Color gradients for each layer
    color_palettes = [
        ['#B22222', '#D9412C', '#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC'],
        ['#D9412C', '#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222'],
        ['#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C'],
        ['#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C', '#FF6600'],
        ['#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C', '#FF6600', '#FF8C1A']
    ]

    layer_radii = [290, 260, 230, 200, 170]

    for radius, colors in zip(layer_radii, color_palettes):
        draw_sectored_circle(radius, 28, colors)

def draw_center_section():
    """Draw the center section featuring a phyllotactic sunflower."""
    center_colors = [
        (140, ['#0077b6', '#023e8a']),
        (135, ['#1a7fc0', '#0f418d']),
        (130, ['#3387ca', '#1c4490']),
        (125, ['#4d8fd4', '#294793']),
        (120, ['#6697de', '#364a96']),
        (115, ['#809fe8', '#434d99']),
        (110, ['#99a7f2', '#50509c']),
        (105, ['#b3affc', '#5d539f']),
        (100, ['#ccb7ff', '#6a56a2']),
        (95, ['#d9c1ff', '#7559a5']),
        (90, ['#e6cbff', '#805ca8']),
        (85, ['#f3d5ff', '#8b5fab']),
        (80, ['#ffdfff', '#9662ae']),
        (75, ['#ffe5ff', '#a165b1']),
        (70, ['#ffebff', '#ac68b4']),
        (65, ['#fff1ff', '#b76bb7']),
        (60, ['#fff5ff', '#c26eba']),
        (55, ['#fff7ff', '#cd71bd']),
        (50, ['#fff9ff', '#d874c0']),
        (45, ['#fffbff', '#e377c3']),
        (40, ['#fffdff', '#ee7ac6']),
        (35, ['#ffffff', '#f97dc9']),
        (30, ['#ffffff', '#ff80cc']),
        (25, ['#ffffff', '#ff83cf']),
        (20, ['#ffffff', '#ff86d2']),
        (15, ['#ffffff', '#ff89d5']),
        (10, ['#ffffff', '#ff8cd8'])
    ]

    for radius, colors in center_colors:
        draw_sectored_circle(radius, 8, colors)

    draw_phyllotactic_sunflower(turtle.Turtle(), 88, 64)

def draw_complete_pookalam():
    """Main function to draw the complete pookalam design."""

    draw_circular_border()
    draw_outer_rings()
    draw_triangle_layers()
    draw_middle_section()
    draw_sectored_layers()
    draw_center_section()

    draw_diyas_around_pookalam(
        center=(0, 0), pookalam_radius=690, diya_radius=25, diya_count=8,
        diya_color="#582f0e", flame_colors=["#260701", "#ffb20f", "#ffe548"],
        flame_count=4, start_angle=0
    )

# =============================================================================
# DISPLAY FUNCTIONS
# =============================================================================

def display_festival_message():
    """Display the festive Onam message."""

    # Display main festival greeting
    greeting_turtle = turtle.Turtle()
    greeting_turtle.speed(0)
    greeting_turtle.penup()
    greeting_turtle.goto(-1250, 500)
    greeting_turtle.pendown()
    greeting_turtle.color("#d00000")
    greeting_turtle.write("Happy Onam!", font=("Courier", 50, "bold italic"))
    greeting_turtle.hideturtle()
