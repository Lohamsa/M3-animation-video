"""
Scene 1: Hook and Introduction
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

class Scene1Intro(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # --- PHASE 1: Hook & 3D Mountain Surface (0 - 16s) ---
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 8, 2],
            x_length=5.5,
            y_length=5.5,
            z_length=3.5,
            axis_config={"color": AXES_COLOR, "stroke_width": 2}
        )
        
        # Paraboloid surface f(x,y) = x^2 + y^2
        surface = Surface(
            lambda u, v: axes.c2p(u, v, (u**2 + v**2)),
            u_range=[-1.8, 1.8],
            v_range=[-1.8, 1.8],
            resolution=(20, 20),
            fill_color="#2563EB",
            fill_opacity=0.75,
            checkerboard_colors=["#1E3A8A", "#2563EB"],
            stroke_color="#60A5FA",
            stroke_width=0.8
        )
        
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES, zoom=0.95)
        
        hook_text = Text(
            "Imagine standing on a mountain...\nWhich direction takes you up the fastest?",
            font_size=24,
            color=TEXT_COLOR,
            line_spacing=1.2
        )
        self.add_fixed_in_frame_mobjects(hook_text)
        hook_text.to_edge(UP, buff=0.6)
        
        self.play(FadeIn(hook_text, shift=DOWN*0.3), run_time=1.5)
        self.play(Create(axes), Create(surface), run_time=3.5)
        
        # A climber point at (0.8, 0.8)
        px, py = 0.9, 0.9
        pz = px**2 + py**2
        p_coords = axes.c2p(px, py, pz)
        climber_dot = Sphere(center=p_coords, radius=0.12, color=ACCENT_GOLD)
        climber_label = Text("You are here", font_size=16, color=ACCENT_GOLD)
        self.add_fixed_in_frame_mobjects(climber_label)
        climber_label.to_corner(UL, buff=1.2)
        
        # 3D Arrows from the point indicating candidate directions
        arrows = VGroup()
        angles = [0, PI/4, PI/2, 3*PI/4, PI, 5*PI/4, 3*PI/2, 7*PI/4]
        for ang in angles:
            dx = 0.5 * np.cos(ang)
            dy = 0.5 * np.sin(ang)
            new_z = (px + dx)**2 + (py + dy)**2
            dest = axes.c2p(px + dx, py + dy, new_z)
            is_steepest = (ang == PI/4) # Points outward along gradient (1,1)
            col = ACCENT_GOLD if is_steepest else ACCENT_CYAN
            sw = 4 if is_steepest else 2
            arr = Line(p_coords, dest, color=col, stroke_width=sw).add_tip(tip_length=0.15)
            arrows.add(arr)
            
        self.play(FadeIn(climber_dot), FadeIn(climber_label), run_time=1.5)
        self.play(Create(arrows), run_time=2.0)
        
        # Smooth camera rotation to feel the 3D geometry
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5.0)
        self.stop_ambient_camera_rotation()
        
        # Fade out 3D elements for formal Title Card
        self.play(
            FadeOut(axes), FadeOut(surface), FadeOut(climber_dot),
            FadeOut(arrows), FadeOut(hook_text), FadeOut(climber_label),
            run_time=1.5
        )
        
        # Reset camera to 2D
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)
        
        # --- PHASE 2: Formal Title Card & Student Details (16 - 35s) ---
        title = Text("THE GRADIENT", font_size=46, weight=BOLD, color=ACCENT_GOLD)
        subtitle = Text("Why does it point in the direction of steepest increase?", font_size=23, color=ACCENT_CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.25).to_edge(UP, buff=0.9)
        
        divider = Line(LEFT*4.5, RIGHT*4.5, color=ACCENT_BLUE, stroke_width=2).next_to(title_group, DOWN, buff=0.3)
        
        card = get_info_card(width=9.5, height=3.2, stroke_color=ACCENT_BLUE).next_to(divider, DOWN, buff=0.35)
        
        student_info = VGroup(
            Text("Student Name : Lohamsa Vallika", font_size=20, color=TEXT_COLOR, weight=BOLD),
            Text("Student ID   : e25b070627", font_size=20, color=ACCENT_CYAN, weight=BOLD),
            Text("Institution  : Newton School of Technology", font_size=19, color=TEXT_COLOR),
            Text("Degree & Program : B.Tech CSE (AI & ML)", font_size=19, color=MUTED_TEXT),
            Text("Course       : Linear Algebra & Calculus (M3) — Internal Assessment", font_size=18, color=ACCENT_GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(card.get_center())
        
        watermark = get_watermark()
        
        self.play(FadeIn(title_group, shift=UP*0.2), Create(divider), run_time=1.5)
        self.play(FadeIn(card), FadeIn(student_info), FadeIn(watermark), run_time=2.0)
        
        self.wait(15.5)
        self.play(FadeOut(title_group), FadeOut(divider), FadeOut(card), FadeOut(student_info), FadeOut(watermark), run_time=1.0)
