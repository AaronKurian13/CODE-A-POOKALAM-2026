"""
BASIC SHAPE FUNCTIONS
====================
Core drawing functions for circles, sectors, and basic geometric shapes.
"""

import turtle
import math

# =============================================================================
# BASIC CIRCLE FUNCTIONS
# =============================================================================

def draw_filled_circle(radius, color, fill_color=None):
    """Draw a filled circle at the origin."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color, fill_color or color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_sectored_circle(radius, divisions, colors):
    """Draw a circle divided into colored sectors."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, -radius)
    angle_step = 360 / divisions

    for i in range(divisions):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.color(colors[i % len(colors)])
        t.begin_fill()
        t.setheading(90)
        t.right(angle_step * i)
        t.forward(radius)
        t.left(90)
        t.circle(radius, angle_step)
        t.left(90)
        t.forward(radius)
        t.end_fill()

def draw_small_circles_ring(center, big_radius, small_radius, count, color, start_angle=0, inner_rings=0, inner_colors=None):
    """Draw small circles arranged in a ring pattern with optional inner rings."""
    cx, cy = center
    ring_radius = big_radius - small_radius

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(color)
    t.fillcolor(color)

    angle_step = 360 / max(1, count)
    for i in range(count):
        angle = math.radians(start_angle + i * angle_step)
        x = cx + ring_radius * math.cos(angle)
        y = cy + ring_radius * math.sin(angle)

        # Draw main circle
        t.penup()
        t.goto(x, y - small_radius)
        t.pendown()
        t.begin_fill()
        t.circle(small_radius)
        t.end_fill()

        # Draw inner concentric circles
        if inner_rings > 0:
            palette = inner_colors or ["#ffffff", color]
            for j in range(inner_rings):
                inner_radius = small_radius * (inner_rings - j) / (inner_rings + 1)
                t.penup()
                t.goto(x, y - inner_radius)
                t.pendown()
                inner_color = palette[j % len(palette)]
                t.pencolor(inner_color)
                t.fillcolor(inner_color)
                t.begin_fill()
                t.circle(inner_radius)
                t.end_fill()

            # Reset colors
            t.pencolor(color)
            t.fillcolor(color)

def draw_repeating_triangle_pattern(length, color, repeat_count):
    """Draw a repeating triangular pattern around a circle."""
    from pookalam import main_turtle

    main_turtle.color(color)

    for i in range(repeat_count):
        main_turtle.begin_fill()
        main_turtle.forward(length / math.tan(math.pi / 3.6))
        main_turtle.left(130)
        main_turtle.forward(length / math.sin(math.pi / 3.6))
        main_turtle.left(100)
        main_turtle.forward(length / math.sin(math.pi / 3.6))
        main_turtle.left(130)
        main_turtle.forward(length / math.tan(math.pi / 3.6))
        main_turtle.end_fill()
        main_turtle.left(360 / repeat_count)

    main_turtle.left(5)
