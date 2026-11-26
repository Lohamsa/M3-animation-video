"""
Scene 6: Summary and Closing Credits
Student Name: Lohamsa Vallika
Student ID: e25b070627
Newton School of Technology
"""

from manim import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers import *

class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # --- PHASE 1: Key Takeaways Card (0 - 20s) ---
        header = get_scene_header(
            "SUMMARY: KEY TAKEAWAYS",
            "The Three Fundamental Principles of the Gradient"
        )
        watermark = get_watermark()
        self.play(FadeIn(header), FadeIn(watermark), run_time=1.2)
        
        card = get_info_card(width=10.5, height=4.8, stroke_color=ACCENT_CYAN).shift(DOWN*0.3)
        
        t1_num = Text("1.", font_size=20, color=ACCENT_GOLD, weight=BOLD)
        t1_txt = Text("Vector of Partial Derivatives: ∇f = ( ∂f/∂x, ∂f/∂y )\nEncapsulates all directional rates of change into a single vector.", font_size=16, color=TEXT_COLOR, line_spacing=1.2)
        row1 = VGroup(t1_num, t1_txt).arrange(RIGHT, aligned_edge=UP, buff=0.3)
        
        t2_num = Text("2.", font_size=20, color=ACCENT_GREEN, weight=BOLD)
        t2_txt = Text("Direction of Steepest Ascent: Always points ⟂ to contour lines.\nBecause Dᵤf = |∇f| cos θ, the rate is maximized when θ = 0°.", font_size=16, color=TEXT_COLOR, line_spacing=1.2)
        row2 = VGroup(t2_num, t2_txt).arrange(RIGHT, aligned_edge=UP, buff=0.3)
        
        t3_num = Text("3.", font_size=20, color=ACCENT_CYAN, weight=BOLD)
        t3_txt = Text("Magnitude Equals Maximum Slope: |∇f| = √( (∂f/∂x)² + (∂f/∂y)² )\nAt (1,1), maximum rate of increase is exactly 2√2 ≈ 2.828.", font_size=16, color=TEXT_COLOR, line_spacing=1.2)
        row3 = VGroup(t3_num, t3_txt).arrange(RIGHT, aligned_edge=UP, buff=0.3)
        
        formula_box = VGroup(
            Text("MASTER FORMULA:", font_size=14, color=ACCENT_GOLD, weight=BOLD),
            Text("∇f(x,y) = ( ∂f/∂x, ∂f/∂y )    |    Dᵤf = ∇f · u = |∇f| cos θ", font_size=17, color=ACCENT_CYAN, weight=BOLD)
        ).arrange(DOWN, buff=0.1)
        
        content = VGroup(row1, row2, row3, Line(LEFT*4.5, RIGHT*4.5, color=ACCENT_BLUE, stroke_width=1), formula_box).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(card.get_center())
        
        self.play(FadeIn(card), run_time=1.0)
        self.play(FadeIn(row1, shift=RIGHT*0.2), run_time=2.0)
        self.play(FadeIn(row2, shift=RIGHT*0.2), run_time=2.0)
        self.play(FadeIn(row3, shift=RIGHT*0.2), run_time=2.0)
        self.play(FadeIn(formula_box), run_time=1.5)
        
        self.wait(10.0)
        
        # --- PHASE 2: Official Closing Credits & AI Disclosure (20 - 41s) ---
        self.play(FadeOut(card), FadeOut(content), FadeOut(header), run_time=1.5)
        
        cred_card = get_info_card(width=10.0, height=5.2, stroke_color=ACCENT_GOLD)
        
        proj_title = Text("M3 INTERNAL ASSESSMENT — ANIMATION VIDEO PROJECT", font_size=21, color=ACCENT_GOLD, weight=BOLD)
        topic_title = Text("Topic: The Gradient — Why Does It Point in the Direction of Steepest Increase?", font_size=16, color=ACCENT_CYAN)
        
        c_div1 = Line(LEFT*4.2, RIGHT*4.2, color=ACCENT_BLUE, stroke_width=1)
        
        details = VGroup(
            Text("Created By       : Lohamsa Vallika", font_size=18, color=TEXT_COLOR, weight=BOLD),
            Text("Student ID       : e25b070627", font_size=18, color=ACCENT_GOLD, weight=BOLD),
            Text("Institution      : Newton School of Technology", font_size=17, color=TEXT_COLOR),
            Text("Degree / Branch  : B.Tech Computer Science & Engineering (AI / ML)", font_size=17, color=MUTED_TEXT),
            Text("Course           : Linear Algebra & Calculus (M3) — Assessment Weightage: 10%", font_size=16, color=ACCENT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        
        c_div2 = Line(LEFT*4.2, RIGHT*4.2, color=ACCENT_BLUE, stroke_width=1)
        
        disclosure = Text(
            "AI Disclosure & Tools: Python, Manim Community v0.22, FFmpeg, ReportLab, Edge-TTS.\nConceptual architecture and mathematical verification reviewed and validated.",
            font_size=12, color=MUTED_TEXT, line_spacing=1.2
        )
        
        closing_content = VGroup(proj_title, topic_title, c_div1, details, c_div2, disclosure).arrange(DOWN, buff=0.18).move_to(cred_card.get_center())
        
        self.play(FadeIn(cred_card), FadeIn(closing_content), run_time=2.0)
        self.wait(17.5)
        
        self.play(FadeOut(cred_card), FadeOut(closing_content), FadeOut(watermark), run_time=1.5)
