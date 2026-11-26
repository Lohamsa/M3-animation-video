"""
Helper functions and visual styling for M3 Animation Video Project:
The Gradient — Why Does It Point in the Direction of Steepest Increase?
Student: Lohamsa Vallika (e25b070627)
"""

from manim import *

# Consistent Professional 3Blue1Brown-inspired Color Palette
BG_COLOR = "#0c1017"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#94A3B8"
ACCENT_BLUE = "#38BDF8"
ACCENT_CYAN = "#22D3EE"
ACCENT_GOLD = "#FBBF24"
ACCENT_GREEN = "#34D399"
ACCENT_RED = "#F87171"
ACCENT_PURPLE = "#A78BFA"
SURFACE_COLOR = "#3B82F6"
AXES_COLOR = "#64748B"

def get_scene_header(title_text, subtitle_text=""):
    """Creates a consistent, elegant header across all scenes."""
    title = Text(title_text, font_size=28, weight=BOLD, color=ACCENT_CYAN)
    title.to_edge(UP, buff=0.4).to_edge(LEFT, buff=0.8)
    
    underline = Line(LEFT, RIGHT, color=ACCENT_CYAN, stroke_width=2)
    underline.match_width(title).next_to(title, DOWN, buff=0.1).align_to(title, LEFT)
    
    header_group = VGroup(title, underline)
    if subtitle_text:
        sub = Text(subtitle_text, font_size=18, color=MUTED_TEXT)
        sub.next_to(underline, DOWN, buff=0.1).align_to(title, LEFT)
        header_group.add(sub)
        
    return header_group

def get_info_card(width=5.5, height=3.5, stroke_color=ACCENT_BLUE):
    """Creates a rounded glassmorphic card for formulas or explanations."""
    card = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=height,
        stroke_color=stroke_color,
        stroke_width=1.5,
        fill_color="#131c2e",
        fill_opacity=0.85
    )
    return card

def get_watermark():
    """Subtle bottom corner student credit."""
    watermark = Text(
        "Lohamsa Vallika | e25b070627 | M3 Project",
        font_size=13,
        color=MUTED_TEXT
    )
    watermark.to_edge(DOWN, buff=0.25).to_edge(RIGHT, buff=0.5)
    return watermark
