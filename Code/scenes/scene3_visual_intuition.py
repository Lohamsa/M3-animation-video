"""
Scene 3: Visual Intuition & The Gradient Vector
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

class Scene3VisualIntuition(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # Header & Watermark
        header = get_scene_header(
            "PART 2: CONTOUR LINES & GRADIENT VECTOR FIELD",
            "Connecting 2D Level Curves to the Gradient Vector"
        )
        watermark = get_watermark()
        self.play(FadeIn(header), FadeIn(watermark), run_time=1.2)
        
        # --- 2D Coordinate Plane for Contours ---
        plane = NumberPlane(
            x_range=[-3.2, 3.2, 1],
            y_range=[-3.2, 3.2, 1],
            x_length=6.0,
            y_length=6.0,
            background_line_style={"stroke_color": "#1E293B", "stroke_width": 1.2},
            axis_config={"color": AXES_COLOR, "stroke_width": 2}
        ).shift(RIGHT*2.8)
        
        x_lbl = Text("x", font_size=16, color=AXES_COLOR).next_to(plane.x_axis.get_end(), RIGHT, buff=0.12)
        y_lbl = Text("y", font_size=16, color=AXES_COLOR).next_to(plane.y_axis.get_end(), UP, buff=0.12)
        plane_labels = VGroup(x_lbl, y_lbl)
        
        # Contour Circles for f(x,y) = x^2 + y^2 = c
        contours = VGroup()
        contour_labels = VGroup()
        c_values = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0]
        c_colors = ["#1E40AF", "#2563EB", "#06B6D4", "#10B981", "#F59E0B", "#EF4444"]
        
        for c, col in zip(c_values, c_colors):
            r = np.sqrt(c)
            circ = Circle(
                radius=r * (plane.x_length / 6.4),
                color=col,
                stroke_width=2.5
            ).move_to(plane.c2p(0, 0))
            contours.add(circ)
            
            # Label at top of circle
            lbl = Text(f"c={c}", font_size=13, color=col)
            lbl.next_to(circ.get_top(), UP, buff=0.08)
            contour_labels.add(lbl)
            
        # Left Info Card
        card = get_info_card(width=5.5, height=5.2, stroke_color=ACCENT_BLUE).to_edge(LEFT, buff=0.6).shift(DOWN*0.3)
        
        card_text1 = VGroup(
            Text("Contour Lines (Level Curves)", font_size=19, color=ACCENT_CYAN, weight=BOLD),
            Text("f(x,y) = c  (constant height)", font_size=17, color=ACCENT_GOLD),
            Line(LEFT*2.3, RIGHT*2.3, color=ACCENT_BLUE, stroke_width=1),
            Text("• For f(x,y) = x² + y² = c:", font_size=15, color=TEXT_COLOR),
            Text("  Concentric circles centered at origin", font_size=14, color=MUTED_TEXT),
            Text("• Walking ALONG a contour:", font_size=15, color=TEXT_COLOR),
            Text("  Height does not change (Rate = 0)", font_size=14, color=ACCENT_GREEN),
            Text("• Crossing BETWEEN contours:", font_size=15, color=TEXT_COLOR),
            Text("  Height changes rapidly!", font_size=14, color=ACCENT_GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(card.get_center())
        
        self.play(Create(plane), Write(plane_labels), FadeIn(card), FadeIn(card_text1), run_time=2.0)
        self.play(Create(contours), Write(contour_labels), run_time=3.5)
        self.wait(12.0)
        
        # --- Introduce Point P(1,1) & Gradient Vector ---
        p_pt = plane.c2p(1, 1)
        p_dot = Dot(p_pt, color=ACCENT_GOLD, radius=0.09)
        p_label = Text("P(1,1)", font_size=16, color=ACCENT_GOLD).next_to(p_dot, UR, buff=0.08)
        
        # Gradient vector: (2, 2)
        grad_dest = plane.c2p(1 + 0.9, 1 + 0.9) # scaled for visual clarity
        grad_arrow = Arrow(
            p_pt, grad_dest,
            buff=0, color=ACCENT_GOLD, stroke_width=4.5, max_tip_length_to_length_ratio=0.22
        )
        grad_label = Text("∇f(1,1) = (2,2)", font_size=16, color=ACCENT_GOLD, weight=BOLD).next_to(grad_arrow.get_end(), UR, buff=0.1)
        
        # Vector components
        comp_x = DashedLine(p_pt, plane.c2p(1 + 0.9, 1), color=ACCENT_CYAN, stroke_width=2.5)
        comp_y = DashedLine(plane.c2p(1 + 0.9, 1), grad_dest, color=ACCENT_GREEN, stroke_width=2.5)
        comp_x_lbl = Text("∂f/∂x = 2", font_size=13, color=ACCENT_CYAN).next_to(comp_x, DOWN, buff=0.08)
        comp_y_lbl = Text("∂f/∂y = 2", font_size=13, color=ACCENT_GREEN).next_to(comp_y, RIGHT, buff=0.08)
        
        # Tangent line to contour c=2 at (1,1): tangent slope = -1
        tangent_line = Line(
            plane.c2p(1 - 0.7, 1 + 0.7),
            plane.c2p(1 + 0.7, 1 - 0.7),
            color=ACCENT_RED,
            stroke_width=3
        )
        tangent_label = Text("Tangent (Contour direction)", font_size=13, color=ACCENT_RED).next_to(tangent_line.get_start(), UL, buff=0.08)
        
        # Right-angle indicator between tangent and gradient
        right_angle = RightAngle(
            Line(p_pt, plane.c2p(1 - 0.4, 1 + 0.4)),
            Line(p_pt, plane.c2p(1 + 0.4, 1 + 0.4)),
            length=0.22, color=TEXT_COLOR
        )
        
        # Update Card to Gradient Insights
        card_text2 = VGroup(
            Text("The Gradient Vector ∇f", font_size=19, color=ACCENT_GOLD, weight=BOLD),
            Text("∇f(x,y) = ( ∂f/∂x, ∂f/∂y ) = (2x, 2y)", font_size=16, color=TEXT_COLOR),
            Line(LEFT*2.3, RIGHT*2.3, color=ACCENT_BLUE, stroke_width=1),
            Text("At Point P(1,1):", font_size=16, color=ACCENT_CYAN, weight=BOLD),
            Text("∇f(1,1) = (2, 2)", font_size=18, color=ACCENT_GOLD, weight=BOLD),
            Line(LEFT*2.3, RIGHT*2.3, color=ACCENT_BLUE, stroke_width=1),
            Text("Key Geometric Insights:", font_size=16, color=ACCENT_GREEN, weight=BOLD),
            Text("1. Orthogonal (⟂) to contour circle", font_size=14, color=TEXT_COLOR),
            Text("2. Points towards HIGHEST contours", font_size=14, color=ACCENT_GOLD),
            Text("3. Combines both coordinate slopes", font_size=14, color=TEXT_COLOR)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(card.get_center())
        
        self.play(FadeIn(p_dot), Write(p_label), run_time=1.5)
        self.play(FadeOut(card_text1), FadeIn(card_text2), run_time=1.5)
        self.play(Create(comp_x), Write(comp_x_lbl), Create(comp_y), Write(comp_y_lbl), run_time=2.5)
        self.play(GrowArrow(grad_arrow), Write(grad_label), run_time=2.0)
        self.play(Create(tangent_line), Write(tangent_label), Create(right_angle), run_time=2.5)
        
        self.wait(29.0)
        
        # Fade out
        self.play(
            FadeOut(plane), FadeOut(plane_labels), FadeOut(contours), FadeOut(contour_labels),
            FadeOut(p_dot), FadeOut(p_label), FadeOut(grad_arrow), FadeOut(grad_label),
            FadeOut(comp_x), FadeOut(comp_y), FadeOut(comp_x_lbl), FadeOut(comp_y_lbl),
            FadeOut(tangent_line), FadeOut(tangent_label), FadeOut(right_angle),
            FadeOut(card), FadeOut(card_text2), FadeOut(header), FadeOut(watermark),
            run_time=1.5
        )
