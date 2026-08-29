"""
POOKALAM MAIN ENTRY POINT
========================
Main script to run the complete Pookalam drawing program.
"""

import turtle
from pookalam import draw_complete_pookalam, display_festival_message

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=3000, height=1500)
    screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
    screen.bgcolor("white")
    screen.title("Code-A-Pookalam 2026")
    
    # Drawing the pookalam 
    draw_complete_pookalam()

    # Display festive message and information
    display_festival_message()

    turtle.Screen().exitonclick()
