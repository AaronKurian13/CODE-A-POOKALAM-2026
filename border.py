"""
BORDER DESIGN FUNCTIONS
=======================
Functions for drawing decorative borders around the pookalam.
"""

import turtle

# =============================================================================
# CIRCULAR BORDER FUNCTIONS
# =============================================================================

def draw_circular_border():
    """Draw a decorative circular border with colored stamps."""
    main_turtle = turtle.Turtle()
    main_turtle.hideturtle()
    main_turtle.speed(0)
    main_turtle.goto(0, -603)
    main_turtle.shapesize(stretch_wid=2, stretch_len=2, outline=None)
    main_turtle.shape("circle")

    border_colors = ["#ff5400", "#ffb600", "#006400", "#38b000", "#ffd400"]

    for i in range(100):
        main_turtle.circle(604, 360 / 100)
        main_turtle.color(border_colors[i % 5])
        main_turtle.stamp()

    main_turtle.goto(0, 0)
