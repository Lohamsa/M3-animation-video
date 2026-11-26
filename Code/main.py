"""
Main execution script for M3 Animation Video Project:
The Gradient — Why Does It Point in the Direction of Steepest Increase?
Student Name: Lohamsa Vallika
Student ID: e25b070627
Newton School of Technology
"""

import os
import sys
import subprocess
import argparse

SCENES = [
    ("Scene1Intro", "scenes/scene1_intro.py"),
    ("Scene2Function", "scenes/scene2_function.py"),
    ("Scene3VisualIntuition", "scenes/scene3_visual_intuition.py"),
    ("Scene4WorkedExample", "scenes/scene4_worked_example.py"),
    ("Scene5SteepestDirection", "scenes/scene5_steepest_direction.py"),
    ("Scene6Summary", "scenes/scene6_summary.py"),
]

def render_scene(scene_name, script_path, quality="h"):
    """
    Renders a single scene using Manim.
    quality: 'l' (480p), 'm' (720p), 'h' (1080p), 'k' (4K)
    """
    print(f"\n==========================================")
    print(f"Rendering {scene_name} from {script_path} (Quality: {quality})")
    print(f"==========================================")
    
    cmd = [
        sys.executable, "-m", "manim",
        f"-q{quality}",
        script_path,
        scene_name
    ]
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(description="Render M3 Gradient Animation Scenes")
    parser.add_argument("--quality", choices=["l", "m", "h"], default="h", help="Render quality (l=480p, m=720p, h=1080p)")
    parser.add_argument("--scene", type=int, choices=[1, 2, 3, 4, 5, 6], default=None, help="Render specific scene number (1-6)")
    args = parser.parse_args()
    
    if args.scene:
        scene_name, script_path = SCENES[args.scene - 1]
        render_scene(scene_name, script_path, args.quality)
    else:
        for scene_name, script_path in SCENES:
            render_scene(scene_name, script_path, args.quality)

if __name__ == "__main__":
    main()
