"""
Scene 4: Complete Worked Example with Step-by-Step Intermediate Calculations
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

class Scene4WorkedExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # Header & Watermark
        header = get_scene_header(
            "PART 3: STEP-BY-STEP WORKED EXAMPLE",
            "Calculating Gradient, Directional Derivatives, and Magnitude"
        )
        watermark = get_watermark()
        self.play(FadeIn(header), FadeIn(watermark), run_time=1.2)
        
        # --- LEFT PANEL: Mathematical Steps ---
        # Card 1: Setup & Gradient Vector (0 - 32s)
        card1 = get_info_card(width=6.8, height=5.4, stroke_color=ACCENT_BLUE).to_edge(LEFT, buff=0.6).shift(DOWN*0.3)
        
        step1_title = Text("Step 1: Function & Partial Derivatives", font_size=17, color=ACCENT_CYAN, weight=BOLD)
        step1_f = Text("f(x,y) = x² + y²", font_size=19, color=TEXT_COLOR, weight=BOLD)
        step1_fx = Text("∂f / ∂x = 2x", font_size=17, color=ACCENT_GOLD)
        step1_fy = Text("∂f / ∂y = 2y", font_size=17, color=ACCENT_GREEN)
        step1_grad = Text("∇f(x,y) = ( ∂f/∂x, ∂f/∂y ) = (2x, 2y)", font_size=16, color=TEXT_COLOR)
        
        div1 = Line(LEFT*2.8, RIGHT*2.8, color=ACCENT_BLUE, stroke_width=1)
        
        step2_title = Text("Step 2: Evaluation at Point P(1,1)", font_size=17, color=ACCENT_CYAN, weight=BOLD)
        step2_fval = Text("f(1,1) = 1² + 1² = 2", font_size=16, color=TEXT_COLOR)
        step2_gval = Text("∇f(1,1) = ( 2(1), 2(1) ) = (2, 2)", font_size=19, color=ACCENT_GOLD, weight=BOLD)
        step2_mag = Text("|∇f(1,1)| = √(2² + 2²) = √8 = 2√2 ≈ 2.828", font_size=16, color=ACCENT_CYAN, weight=BOLD)
        
        panel1 = VGroup(
            step1_title, step1_f, VGroup(step1_fx, step1_fy).arrange(RIGHT, buff=0.8),
            step1_grad, div1,
            step2_title, step2_fval, step2_gval, step2_mag
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(card1.get_center())
        
        # --- RIGHT PANEL: Geometric Visualization ---
        plane = NumberPlane(
            x_range=[-0.5, 3.2, 1],
            y_range=[-0.5, 3.2, 1],
            x_length=5.0,
            y_length=5.0,
            background_line_style={"stroke_color": "#1E293B", "stroke_width": 1.0},
            axis_config={"color": AXES_COLOR, "stroke_width": 2}
        ).shift(RIGHT*3.6 + DOWN*0.3)
        x_lbl = Text("x", font_size=15, color=AXES_COLOR).next_to(plane.x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = Text("y", font_size=15, color=AXES_COLOR).next_to(plane.y_axis.get_end(), UP, buff=0.1)
        plane_labels = VGroup(x_lbl, y_lbl)
        
        # Contour arc through (1,1) -> radius = sqrt(2) approx 1.414
        r = np.sqrt(2)
        arc = Arc(
            radius=r * (plane.x_length / 3.7),
            start_angle=0,
            angle=PI/2,
            color="#06B6D4",
            stroke_width=2.5,
            arc_center=plane.c2p(0, 0)
        )
        arc_label = Text("Contour c=2", font_size=13, color="#06B6D4").next_to(arc.point_from_proportion(0.8), UR, buff=0.08)
        
        p_pt = plane.c2p(1, 1)
        p_dot = Dot(p_pt, color=ACCENT_GOLD, radius=0.08)
        p_lbl = Text("P(1,1)", font_size=15, color=ACCENT_GOLD).next_to(p_dot, DL, buff=0.08)
        
        # Gradient arrow (2,2)
        grad_dest = plane.c2p(1 + 1.2, 1 + 1.2)
        grad_arrow = Arrow(p_pt, grad_dest, buff=0, color=ACCENT_GOLD, stroke_width=4.5)
        grad_lbl = Text("∇f = (2,2)", font_size=15, color=ACCENT_GOLD, weight=BOLD).next_to(grad_dest, UR, buff=0.08)
        
        self.play(FadeIn(card1), FadeIn(panel1), run_time=2.0)
        self.play(Create(plane), Write(plane_labels), Create(arc), Write(arc_label), run_time=2.5)
        self.play(FadeIn(p_dot), Write(p_lbl), GrowArrow(grad_arrow), Write(grad_lbl), run_time=2.0)
        self.wait(20.0)
        
        # --- PHASE 2: Directional Derivatives along u1 and u2 (32 - 87s) ---
        card2 = get_info_card(width=6.8, height=5.4, stroke_color=ACCENT_GREEN).to_edge(LEFT, buff=0.6).shift(DOWN*0.3)
        
        step3_title = Text("Step 3: Directional Derivative along Gradient u₁", font_size=16, color=ACCENT_GREEN, weight=BOLD)
        step3_u1 = Text("u₁ = ∇f / |∇f| = ( 1/√2, 1/√2 )", font_size=16, color=ACCENT_GREEN)
        step3_d1_formula = Text("Dᵤ₁ f = ∇f · u₁", font_size=17, color=TEXT_COLOR, weight=BOLD)
        step3_d1_calc = Text("= (2, 2) · ( 1/√2, 1/√2 )", font_size=16, color=TEXT_COLOR)
        step3_d1_eval = Text("= 2/√2 + 2/√2 = 4/√2 = 2√2 ≈ 2.828", font_size=16, color=ACCENT_GREEN, weight=BOLD)
        step3_res = Text("➔ Maximum Instantaneous Increase!", font_size=15, color=ACCENT_GOLD, weight=BOLD)
        
        div2 = Line(LEFT*2.8, RIGHT*2.8, color=ACCENT_BLUE, stroke_width=1)
        
        step4_title = Text("Step 4: Perpendicular Direction u₂ (along contour)", font_size=16, color=ACCENT_RED, weight=BOLD)
        step4_u2 = Text("u₂ = ( 1/√2, -1/√2 )   [ u₁ · u₂ = 0 ]", font_size=15, color=ACCENT_RED)
        step4_d2_calc = Text("Dᵤ₂ f = (2, 2) · ( 1/√2, -1/√2 ) = 2/√2 - 2/√2 = 0", font_size=15, color=ACCENT_RED, weight=BOLD)
        step4_res = Text("➔ Zero Instantaneous Change along Contour!", font_size=15, color=ACCENT_CYAN, weight=BOLD)
        
        panel2 = VGroup(
            step3_title, step3_u1, step3_d1_formula, step3_d1_calc, step3_d1_eval, step3_res,
            div2,
            step4_title, step4_u2, step4_d2_calc, step4_res
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(card2.get_center())
        
        # Unit arrows on plane
        # u1 arrow (length = 0.6 in direction of (1,1))
        u1_dest = plane.c2p(1 + 0.6/np.sqrt(2), 1 + 0.6/np.sqrt(2))
        u1_arrow = Arrow(p_pt, u1_dest, buff=0, color=ACCENT_GREEN, stroke_width=4.0)
        u1_lbl = Text("u₁ (Gradient dir)", font_size=14, color=ACCENT_GREEN, weight=BOLD).next_to(u1_dest, UP, buff=0.08)
        
        # u2 arrow (length = 0.6 in direction of (1, -1))
        u2_dest = plane.c2p(1 + 0.6/np.sqrt(2), 1 - 0.6/np.sqrt(2))
        u2_arrow = Arrow(p_pt, u2_dest, buff=0, color=ACCENT_RED, stroke_width=4.0)
        u2_lbl = Text("u₂ (⟂ Contour)", font_size=14, color=ACCENT_RED, weight=BOLD).next_to(u2_dest, RIGHT, buff=0.08)
        
        right_ang2 = RightAngle(
            Line(p_pt, u1_dest), Line(p_pt, u2_dest),
            length=0.2, color=TEXT_COLOR
        )
        
        self.play(FadeOut(card1), FadeOut(panel1), FadeIn(card2), FadeIn(panel2), run_time=2.0)
        self.play(GrowArrow(u1_arrow), Write(u1_lbl), run_time=2.0)
        self.play(GrowArrow(u2_arrow), Write(u2_lbl), Create(right_ang2), run_time=2.0)
        
        self.wait(53.0)
        
        # Fade out
        self.play(
            FadeOut(plane), FadeOut(plane_labels), FadeOut(arc), FadeOut(arc_label),
            FadeOut(p_dot), FadeOut(p_lbl), FadeOut(grad_arrow), FadeOut(grad_lbl),
            FadeOut(u1_arrow), FadeOut(u1_lbl), FadeOut(u2_arrow), FadeOut(u2_lbl), FadeOut(right_ang2),
            FadeOut(card2), FadeOut(panel2), FadeOut(header), FadeOut(watermark),
            run_time=1.5
        )
