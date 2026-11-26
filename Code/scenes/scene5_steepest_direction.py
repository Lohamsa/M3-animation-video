"""
Scene 5: Why the Gradient is the Steepest Direction
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

class Scene5SteepestDirection(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # Header & Watermark
        header = get_scene_header(
            "PART 4: WHY IS THE GRADIENT THE STEEPEST DIRECTION?",
            "Geometric Proof via the Dot Product and Cosine Maximization"
        )
        watermark = get_watermark()
        self.play(FadeIn(header), FadeIn(watermark), run_time=1.2)
        
        # --- LEFT PANEL: Mathematical Proof Card ---
        card = get_info_card(width=6.6, height=5.5, stroke_color=ACCENT_GOLD).to_edge(LEFT, buff=0.6).shift(DOWN*0.3)
        
        title_proof = Text("The Dot Product Formula", font_size=19, color=ACCENT_GOLD, weight=BOLD)
        f1 = Text("Dᵤ f = ∇f · u = |∇f| |u| cos θ", font_size=19, color=TEXT_COLOR, weight=BOLD)
        f2 = Text("Since u is a unit vector (|u| = 1):", font_size=15, color=MUTED_TEXT)
        f3 = Text("Dᵤ f = |∇f| cos θ", font_size=22, color=ACCENT_CYAN, weight=BOLD)
        
        div = Line(LEFT*2.8, RIGHT*2.8, color=ACCENT_BLUE, stroke_width=1)
        
        c1 = Text("Properties of cos θ:", font_size=17, color=ACCENT_GREEN, weight=BOLD)
        c2 = Text("• Range: -1 ≤ cos θ ≤ +1", font_size=15, color=TEXT_COLOR)
        c3 = Text("• Maximum: cos θ = 1 strictly when θ = 0°", font_size=16, color=ACCENT_GOLD, weight=BOLD)
        c4 = Text("• When θ = 0°: u points in SAME direction as ∇f", font_size=14, color=TEXT_COLOR)
        c5 = Text("• Max Rate of Increase = |∇f| = 2√2 ≈ 2.828", font_size=16, color=ACCENT_GREEN, weight=BOLD)
        
        div2 = Line(LEFT*2.8, RIGHT*2.8, color=ACCENT_BLUE, stroke_width=1)
        
        cases = Text("θ = 90°  ➔ cos(90°) = 0   ➔ Dᵤf = 0 (Contour)\nθ = 180° ➔ cos(180°) = -1 ➔ Dᵤf = -2√2 (Steepest Descent)", font_size=13, color=MUTED_TEXT, line_spacing=1.3)
        
        proof_panel = VGroup(
            title_proof, f1, f2, f3, div,
            c1, c2, c3, c4, c5, div2, cases
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(card.get_center())
        
        # --- RIGHT PANEL: Interactive Vector Angle Wheel ---
        wheel_center = RIGHT*3.8 + DOWN*0.2
        circle = Circle(radius=1.8, color="#334155", stroke_width=2).move_to(wheel_center)
        c_dot = Dot(wheel_center, color=TEXT_COLOR, radius=0.06)
        
        # Fixed Gradient vector pointing at 45 degrees
        grad_len = 2.4
        grad_ang = PI/4
        grad_end = wheel_center + np.array([grad_len*np.cos(grad_ang), grad_len*np.sin(grad_ang), 0])
        grad_arrow = Arrow(wheel_center, grad_end, buff=0, color=ACCENT_GOLD, stroke_width=4.5)
        grad_label = Text("∇f (Fixed)", font_size=15, color=ACCENT_GOLD, weight=BOLD).next_to(grad_end, UR, buff=0.08)
        
        # Rotating direction vector u
        u_val = ValueTracker(PI/4) # Starts at theta = 0 (aligned with gradient)
        
        u_arrow = always_redraw(lambda: Arrow(
            wheel_center,
            wheel_center + np.array([1.8*np.cos(u_val.get_value()), 1.8*np.sin(u_val.get_value()), 0]),
            buff=0, color=ACCENT_GREEN, stroke_width=4.0
        ))
        
        u_label = always_redraw(lambda: Text(
            "u", font_size=15, color=ACCENT_GREEN, weight=BOLD
        ).next_to(
            wheel_center + np.array([1.8*np.cos(u_val.get_value()), 1.8*np.sin(u_val.get_value()), 0]),
            normalize(np.array([np.cos(u_val.get_value()), np.sin(u_val.get_value()), 0])),
            buff=0.12
        ))
        
        # Angle arc and tracker text below circle
        def get_diff_angle():
            diff = (u_val.get_value() - grad_ang) % (2*PI)
            if diff > PI:
                diff = 2*PI - diff
            return diff
            
        rate_tracker = always_redraw(lambda: VGroup(
            Text(f"Angle θ = {np.degrees(get_diff_angle()):.1f}°", font_size=15, color=TEXT_COLOR),
            Text(f"cos θ = {np.cos(get_diff_angle()):+.2f}", font_size=16, color=ACCENT_CYAN, weight=BOLD),
            Text(f"Dᵤf = {2.828 * np.cos(get_diff_angle()):+.2f}", font_size=18, color=ACCENT_GOLD if abs(get_diff_angle()) < 0.1 else (ACCENT_GREEN if np.cos(get_diff_angle()) > 0 else ACCENT_RED), weight=BOLD)
        ).arrange(DOWN, buff=0.12).next_to(circle, DOWN, buff=0.35))
        
        self.play(FadeIn(card), FadeIn(proof_panel), run_time=2.0)
        self.play(Create(circle), FadeIn(c_dot), GrowArrow(grad_arrow), Write(grad_label), run_time=2.0)
        self.play(Create(u_arrow), Write(u_label), FadeIn(rate_tracker), run_time=2.0)
        self.wait(10.0)
        
        # Animate u sweeping across different angles to visually demonstrate cosine scaling
        # Move to 90 degrees away (perpendicular)
        self.play(u_val.animate.set_value(grad_ang + PI/2), run_time=5.0, rate_func=linear)
        self.wait(4.0)
        
        # Move to 180 degrees away (opposite / steepest descent)
        self.play(u_val.animate.set_value(grad_ang + PI), run_time=6.0, rate_func=linear)
        self.wait(4.0)
        
        # Move back to 0 degrees (aligned / maximum steepest ascent!)
        self.play(u_val.animate.set_value(grad_ang), run_time=6.0, rate_func=linear)
        self.wait(22.0)
        
        # Fade out
        self.play(
            FadeOut(circle), FadeOut(c_dot), FadeOut(grad_arrow), FadeOut(grad_label),
            FadeOut(u_arrow), FadeOut(u_label), FadeOut(rate_tracker),
            FadeOut(card), FadeOut(proof_panel), FadeOut(header), FadeOut(watermark),
            run_time=1.5
        )
