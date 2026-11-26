"""
Scene 2: Understanding the Function & Partial Derivatives
Student Name: Lohamsa Vallika
Student ID: e25b070627
Newton School of Technology
"""

from manim import *
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers import *

class Scene2Function(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # Header
        header = get_scene_header(
            "PART 1: TWO-VARIABLE FUNCTIONS & PARTIAL DERIVATIVES",
            "Geometry of f(x,y) = x² + y² and Coordinate Slopes"
        )
        self.add_fixed_in_frame_mobjects(header)
        watermark = get_watermark()
        self.add_fixed_in_frame_mobjects(watermark)
        self.play(FadeIn(header), FadeIn(watermark), run_time=1.2)
        
        # --- PHASE 1: 3D Surface & Function Definition (0 - 28s) ---
        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=5.0,
            y_length=5.0,
            z_length=3.2,
            axis_config={"color": AXES_COLOR, "stroke_width": 2}
        ).shift(DOWN*0.5 + RIGHT*1.2)
        
        surface = Surface(
            lambda u, v: axes.c2p(u, v, (u**2 + v**2)),
            u_range=[-1.6, 1.6],
            v_range=[-1.6, 1.6],
            resolution=(18, 18),
            fill_color="#3B82F6",
            fill_opacity=0.7,
            checkerboard_colors=["#1D4ED8", "#3B82F6"],
            stroke_color="#93C5FD",
            stroke_width=0.6
        )
        
        self.set_camera_orientation(phi=65 * DEGREES, theta=-60 * DEGREES, zoom=0.9)
        
        # 2D Info Card on the left
        func_card = get_info_card(width=4.8, height=4.8, stroke_color=ACCENT_BLUE)
        self.add_fixed_in_frame_mobjects(func_card)
        func_card.to_corner(UL, buff=1.4)
        
        card_content = VGroup(
            Text("Surface Equation:", font_size=18, color=ACCENT_CYAN, weight=BOLD),
            Text("z = f(x,y) = x² + y²", font_size=22, color=ACCENT_GOLD, weight=BOLD),
            Line(LEFT*2.0, RIGHT*2.0, color=ACCENT_BLUE, stroke_width=1),
            Text("• Input : Point (x,y) in xy-plane", font_size=16, color=TEXT_COLOR),
            Text("• Output: Vertical height z", font_size=16, color=TEXT_COLOR),
            Text("• Shape : Paraboloid bowl", font_size=16, color=MUTED_TEXT),
            Line(LEFT*2.0, RIGHT*2.0, color=ACCENT_BLUE, stroke_width=1),
            Text("Key Points:", font_size=17, color=ACCENT_GREEN, weight=BOLD),
            Text("f(0,0) = 0² + 0² = 0  (Minimum)", font_size=15, color=TEXT_COLOR),
            Text("f(1,1) = 1² + 1² = 2  (Height = 2)", font_size=15, color=ACCENT_GOLD),
            Text("f(2,0) = 2² + 0² = 4  (Height = 4)", font_size=15, color=TEXT_COLOR)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(func_card.get_center())
        self.add_fixed_in_frame_mobjects(card_content)
        
        self.play(FadeIn(func_card), FadeIn(card_content), run_time=2.0)
        self.play(Create(axes), Create(surface), run_time=3.5)
        
        # Highlight points on surface
        pts = [(0, 0, 0, "Origin (0,0)"), (1, 1, 2, "P(1,1,2)"), (2, 0, 4, "(2,0,4)")]
        dots = VGroup()
        for x, y, z, lbl in pts:
            d = Sphere(center=axes.c2p(x, y, z), radius=0.1, color=ACCENT_GOLD)
            dots.add(d)
            
        self.play(FadeIn(dots), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(19.0)
        self.stop_ambient_camera_rotation()
        
        # --- PHASE 2: Partial Derivatives Explanation (28 - 59.5s) ---
        self.play(FadeOut(dots), run_time=1.0)
        
        # Replace info card with Partial Derivatives Card
        deriv_card = get_info_card(width=5.2, height=5.0, stroke_color=ACCENT_CYAN)
        self.add_fixed_in_frame_mobjects(deriv_card)
        deriv_card.to_corner(UL, buff=1.4)
        
        deriv_content = VGroup(
            Text("Partial Derivatives", font_size=20, color=ACCENT_CYAN, weight=BOLD),
            Line(LEFT*2.2, RIGHT*2.2, color=ACCENT_CYAN, stroke_width=1),
            Text("1. Along x-axis (y held constant):", font_size=16, color=ACCENT_GOLD, weight=BOLD),
            Text("∂f / ∂x = 2x", font_size=20, color=ACCENT_GOLD, weight=BOLD),
            Text("• Slice along y=1: z = x² + 1", font_size=14, color=TEXT_COLOR),
            Text("• Measures rate of change in x direction", font_size=14, color=MUTED_TEXT),
            Line(LEFT*2.2, RIGHT*2.2, color=ACCENT_CYAN, stroke_width=1),
            Text("2. Along y-axis (x held constant):", font_size=16, color=ACCENT_GREEN, weight=BOLD),
            Text("∂f / ∂y = 2y", font_size=20, color=ACCENT_GREEN, weight=BOLD),
            Text("• Slice along x=1: z = 1 + y²", font_size=14, color=TEXT_COLOR),
            Text("• Measures rate of change in y direction", font_size=14, color=MUTED_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(deriv_card.get_center())
        self.add_fixed_in_frame_mobjects(deriv_content)
        
        # 3D Cross sections
        # Curve 1: y = 1 (constant), varying x in [-1.6, 1.6]
        curve_x = ParametricFunction(
            lambda t: axes.c2p(t, 1.0, t**2 + 1.0),
            t_range=[-1.5, 1.5],
            color=ACCENT_GOLD,
            stroke_width=5
        )
        # Curve 2: x = 1 (constant), varying y in [-1.6, 1.6]
        curve_y = ParametricFunction(
            lambda t: axes.c2p(1.0, t, 1.0 + t**2),
            t_range=[-1.5, 1.5],
            color=ACCENT_GREEN,
            stroke_width=5
        )
        
        # Tangent at (1,1,2) along x: direction (1, 0, 2)
        tangent_x = Line(
            axes.c2p(1.0 - 0.4, 1.0, 2.0 - 0.8),
            axes.c2p(1.0 + 0.4, 1.0, 2.0 + 0.8),
            color=ACCENT_GOLD,
            stroke_width=4
        )
        # Tangent at (1,1,2) along y: direction (0, 1, 2)
        tangent_y = Line(
            axes.c2p(1.0, 1.0 - 0.4, 2.0 - 0.8),
            axes.c2p(1.0, 1.0 + 0.4, 2.0 + 0.8),
            color=ACCENT_GREEN,
            stroke_width=4
        )
        
        self.play(
            FadeOut(func_card), FadeOut(card_content),
            FadeIn(deriv_card), FadeIn(deriv_content),
            run_time=1.5
        )
        self.play(Create(curve_x), Create(tangent_x), run_time=2.5)
        self.play(Create(curve_y), Create(tangent_y), run_time=2.5)
        
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(24.0)
        self.stop_ambient_camera_rotation()
        
        self.play(
            FadeOut(surface), FadeOut(axes), FadeOut(curve_x), FadeOut(curve_y),
            FadeOut(tangent_x), FadeOut(tangent_y), FadeOut(deriv_card),
            FadeOut(deriv_content), FadeOut(header), FadeOut(watermark),
            run_time=1.5
        )
