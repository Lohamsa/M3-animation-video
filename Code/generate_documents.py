"""
PDF Generation Script for M3 Animation Video Project
Generates:
1. Documents/Storyboard.pdf
2. Documents/Narration_Script.pdf
3. Documents/Mathematical_Verification.pdf

Author: Lohamsa Vallika (Student ID: e25b070627)
Institution: Newton School of Technology
Course: Linear Algebra & Calculus (M3)
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

STUDENT_NAME = "Lohamsa Vallika"
STUDENT_ID = "e25b070627"
COLLEGE = "Newton School of Technology"
BRANCH = "B.Tech Computer Science & Engineering (AI/ML)"
SUBJECT = "Linear Algebra and Calculus (M3)"
PROJECT_TITLE = "The Gradient — Why Does It Point in the Direction of Steepest Increase?"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, f"M3 Assessment: {PROJECT_TITLE}")
            self.drawRightString(612 - 54, 750, f"{STUDENT_NAME} ({STUDENT_ID})")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 744, 612 - 54, 744)
            
        # Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 50, 612 - 54, 50)
        self.drawString(54, 38, f"{COLLEGE} | {BRANCH}")
        self.drawRightString(612 - 54, 38, f"Page {self._pageNumber} of {total_pages}")
        self.restoreState()

def get_base_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0284C7"),
        spaceAfter=14
    )
    
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155"),
        spaceAfter=6
    )
    
    bold_style = ParagraphStyle(
        'DocBold',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor("#0F172A")
    )
    
    code_style = ParagraphStyle(
        'DocCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#0369A1"),
        spaceAfter=4
    )
    
    return {
        "title": title_style,
        "subtitle": subtitle_style,
        "h2": h2_style,
        "body": body_style,
        "bold": bold_style,
        "code": code_style
    }

def create_metadata_card(doc_type_title):
    st = get_base_styles()
    data = [
        [Paragraph(f"<b>Document:</b> {doc_type_title}", st['body']), Paragraph(f"<b>Course:</b> {SUBJECT}", st['body'])],
        [Paragraph(f"<b>Student Name:</b> {STUDENT_NAME}", st['body']), Paragraph(f"<b>Student ID:</b> {STUDENT_ID}", st['body'])],
        [Paragraph(f"<b>Institution:</b> {COLLEGE}", st['body']), Paragraph(f"<b>Program:</b> {BRANCH}", st['body'])],
        [Paragraph(f"<b>Topic:</b> The Gradient & Steepest Increase", st['body']), Paragraph(f"<b>Target Function:</b> f(x,y) = x² + y²", st['body'])]
    ]
    t = Table(data, colWidths=[245, 255])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

# ==============================================================================
# 1. STORYBOARD PDF
# ==============================================================================
def generate_storyboard_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    st = get_base_styles()
    elements = []
    
    elements.append(Paragraph("PROJECT STORYBOARD", st['title']))
    elements.append(Paragraph(f"Official Six-Scene Pedagogical Specification | {PROJECT_TITLE}", st['subtitle']))
    elements.append(create_metadata_card("Official Animation Storyboard (6 Scenes)"))
    elements.append(Spacer(1, 14))
    
    scenes_data = [
        {
            "num": 1,
            "title": "Hook & Introduction",
            "time": "00:00 - 00:35 (~35 sec)",
            "obj": "Engage viewer with intuitive mountain ascent query and establish formal student identification.",
            "visual": "Dark navy 3D space with a wireframe paraboloid mountain. Smooth ambient camera rotation around the summit. A glowing gold climber point at (0.9, 0.9) with 3D directional vectors pointing in 8 compass directions. Smooth transition to formal project title card.",
            "anim": "Camera tracks 3D surface; vectors grow from climber dot; golden arrow pulses pointing up the peak. Camera resets to 2D; title and student details fade in with blue border card.",
            "math": "z = f(x,y); candidate directions: Δr = (cos θ, sin θ)",
            "narration": "Presents mountain climber analogy: which way to step for the fastest climb? Introduces the gradient and formal student presentation."
        },
        {
            "num": 2,
            "title": "Understanding Two-Variable Functions & Partial Derivatives",
            "time": "00:35 - 01:34 (~59 sec)",
            "obj": "Explain geometric meaning of multivariable surface z = f(x,y) and coordinate partial derivatives.",
            "visual": "3D paraboloid bowl surface z = x² + y² over xy-axes. Left glassmorphic card displays input/output mappings and critical evaluation points (0,0)->0, (1,1)->2, (2,0)->4. 3D parabolic cross-sections slice through surface along coordinate planes.",
            "anim": "Surface creates smoothly; coordinate axes scale; evaluation dots pop up; 3D golden and emerald slice curves trace through the surface with tangent slope lines.",
            "math": "f(x,y) = x² + y²; ∂f/∂x = 2x (y constant); ∂f/∂y = 2y (x constant)",
            "narration": "Explains how inputs (x,y) generate vertical elevation z. Differentiates single vs multivariable calculus. Explains partial derivatives as rates of change along pure axes."
        },
        {
            "num": 3,
            "title": "Visual Intuition: Contour Lines & Gradient Field",
            "time": "01:34 - 02:33 (~59 sec)",
            "obj": "Connect 3D height to 2D level curves and visualize the gradient vector orthogonal to contours.",
            "visual": "2D NumberPlane displaying concentric contour circles f(x,y) = c for c in {0.5, 1, 2, 4, 6, 8}. Target point P(1,1) on contour c=2. Gradient vector arrow (2,2) in bright gold with dashed x-component (2) and y-component (2). Red contour tangent line showing right angle.",
            "anim": "Concentric contour rings ripple outward with color spectrum; point P appears; component lines form a right triangle; gradient vector shoots outward perpendicular to the contour circle.",
            "math": "Contour: x² + y² = c; ∇f(1,1) = (2,2); ∇f ⟂ Tangent (-1,1)",
            "narration": "Introduces contour lines where elevation is constant. Walking along a contour yields zero change. Introduces gradient vector combining partial derivatives, highlighting orthogonality."
        },
        {
            "num": 4,
            "title": "Complete Worked Example with Intermediate Steps",
            "time": "02:33 - 04:00 (~87 sec)",
            "obj": "Step-by-step rigorous calculation of gradient, magnitude, and directional derivatives along gradient and tangent.",
            "visual": "Split-panel layout. Left: Glassmorphic cards revealing algebraic derivation step by step without skips. Right: Interactive 2D coordinate plane showing point P(1,1), contour arc c=2, gradient arrow, unit vector u₁ in emerald green, and perpendicular unit vector u₂ in crimson red.",
            "anim": "Equations write sequentially; intermediate evaluations highlighted; vector arrows u₁ and u₂ grow from P(1,1); right angle indicator highlights perpendicularity.",
            "math": "∇f(1,1) = (2,2); |∇f| = 2√2; u₁ = (1/√2, 1/√2); D_{u₁}f = ∇f · u₁ = 2√2; u₂ = (1/√2, -1/√2); D_{u₂}f = 0",
            "narration": "Walks through every step of calculation: partial derivatives, evaluation at (1,1), gradient magnitude (2√2), unit gradient direction, dot product yielding 2√2, and perpendicular dot product yielding 0."
        },
        {
            "num": 5,
            "title": "Why is the Gradient the Steepest Direction?",
            "time": "04:00 - 05:04 (~64 sec)",
            "obj": "Mathematical and geometric proof of why θ = 0° maximizes directional derivative via the dot product.",
            "visual": "Left panel: Analytical proof based on dot product formula D_u f = |∇f| cos θ. Right panel: Interactive unit circle wheel with fixed gradient vector ∇f at 45° and rotating unit vector u(θ). Live value display tracking angle θ, cos θ, and D_u f.",
            "anim": "Vector u smoothly sweeps from 0° -> 90° (perpendicular, D_u f = 0) -> 180° (opposite, D_u f = -2.83) -> 0° (aligned, D_u f = +2.83). Real-time numerical display updates continuously.",
            "math": "D_u f = ∇f · u = |∇f||u| cos θ = |∇f| cos θ; Max when cos θ = 1 ⟺ θ = 0°",
            "narration": "Explains the dot product cosine definition. Proves that cos θ is bounded in [-1, 1] and reaches its absolute maximum at θ = 0°. Concludes that pointing along the gradient guarantees steepest ascent."
        },
        {
            "num": 6,
            "title": "Summary Takeaways & Official Credits",
            "time": "05:04 - 05:45 (~41 sec)",
            "obj": "Summarize the three core mathematical takeaways and present official course assessment credits.",
            "visual": "Card 1: Three highlighted takeaways with master formula. Card 2: Full assessment submission details: Student Name, Student ID, Program, Institution, Assessment Weightage, and AI Disclosure.",
            "anim": "Takeaway rows fade in one by one with glowing bullet points; master formula emphasizes key result; transitions to clean credit card.",
            "math": "Master Result: ∇f = (∂f/∂x, ∂f/∂y); Max Rate = |∇f| in direction u = ∇f / |∇f|",
            "narration": "Recaps the three pillars: gradient definition, steepest increase direction, and magnitude as maximum rate. Concludes internal assessment video with formal credits."
        }
    ]
    
    for sc in scenes_data:
        scene_table_data = [
            [Paragraph(f"<b>SCENE {sc['num']}: {sc['title'].upper()}</b>", st['bold']), Paragraph(f"<b>Timing:</b> {sc['time']}", st['body'])],
            [Paragraph(f"<b>Learning Objective:</b> {sc['obj']}", st['body']), ""],
            [Paragraph(f"<b>Visual Description:</b> {sc['visual']}", st['body']), ""],
            [Paragraph(f"<b>Animation Details:</b> {sc['anim']}", st['body']), ""],
            [Paragraph(f"<b>Key Formulas:</b> <font color='#0369A1'><b>{sc['math']}</b></font>", st['body']), ""],
            [Paragraph(f"<b>Narration Summary:</b> {sc['narration']}", st['body']), ""]
        ]
        t_scene = Table(scene_table_data, colWidths=[380, 120])
        t_scene.setStyle(TableStyle([
            ('SPAN', (0,1), (1,1)),
            ('SPAN', (0,2), (1,2)),
            ('SPAN', (0,3), (1,3)),
            ('SPAN', (0,4), (1,4)),
            ('SPAN', (0,5), (1,5)),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E0F2FE")),
            ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor("#0284C7")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        elements.append(t_scene)
        elements.append(Spacer(1, 10))
        
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Generated: {output_path}")

# ==============================================================================
# 2. NARRATION SCRIPT PDF
# ==============================================================================
def generate_narration_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    st = get_base_styles()
    elements = []
    
    elements.append(Paragraph("VOICE-OVER NARRATION SCRIPT", st['title']))
    elements.append(Paragraph(f"Complete Scene-by-Scene Audio Script & Sync Guide | {PROJECT_TITLE}", st['subtitle']))
    elements.append(create_metadata_card("Complete Narration Script & Sync Guide"))
    elements.append(Spacer(1, 14))
    
    script_data = [
        {
            "num": 1,
            "title": "Hook and Introduction",
            "time": "00:00 - 00:35",
            "dur": "34.56 sec",
            "text": "Imagine you are standing on a misty mathematical mountain, looking up at the summit. If you want to climb as quickly as possible, which direction should you take your next step? Welcome to this exploration of one of multivariable calculus's most elegant concepts: The Gradient. We will uncover why the gradient always points in the direction of steepest increase. My name is Lohamsa Vallika, student ID e25b070627, from Newton School of Technology. Let us begin our ascent.",
            "notes": "Synchronize mountain intro with 3D camera rotation and multi-directional arrows; synchronize student name and ID with formal title card reveal."
        },
        {
            "num": 2,
            "title": "Understanding the Function & Partial Derivatives",
            "time": "00:35 - 01:34",
            "dur": "59.42 sec",
            "text": "To understand the gradient, let us explore a multivariable function: z equals f of x and y, defined as x squared plus y squared. In single-variable calculus, an input x gives an output y. Here, every input pair (x,y) on the horizontal plane produces a vertical height, z. When we plot every point, we create a smooth, three-dimensional paraboloid bowl. Notice that at the origin, the height is zero. As we step outward, the height increases quadratically. To see how the function changes, we examine partial derivatives. The partial derivative with respect to x is 2x, measuring the rate of change when moving purely along x while holding y constant. Similarly, the partial derivative with respect to y is 2y, measuring change purely along y. These are our fundamental coordinate slopes.",
            "notes": "Align 3D bowl creation with 'paraboloid bowl'; point out (0,0) and (1,1) when mentioned; trigger 3D cross-sectional slice curves and tangent lines exactly when discussing partial derivatives."
        },
        {
            "num": 3,
            "title": "Visual Intuition: Contour Lines & Gradient Field",
            "time": "01:34 - 02:33",
            "dur": "58.46 sec",
            "text": "Now, let us slice our 3D bowl with horizontal planes. Each slice produces a level curve, known as a contour line, where f of x and y equals a constant c. For our paraboloid, these are concentric circles. Every point on a single contour line shares the exact same height. If you walk along a contour, your elevation does not change at all. But what if you step across contour lines? That is where the gradient vector enters. The gradient of f combines both partial derivatives into a vector: 2x in the x direction and 2y in the y direction. At the point P, (1, 1), the gradient is the vector (2, 2). Notice two remarkable geometric facts: first, the gradient vector points perpendicularly outward from the contour line. Second, it points directly toward higher contour values.",
            "notes": "Display concentric contour rings during level curves explanation; show point P(1,1); draw dashed component lines (2,2) on 'combines both partial derivatives'; highlight right angle at 'perpendicularly outward'."
        },
        {
            "num": 4,
            "title": "Complete Worked Example with Intermediate Steps",
            "time": "02:33 - 04:00",
            "dur": "86.74 sec",
            "text": "Let us verify this mathematically with a complete worked example. Our function is f of x, y equals x squared plus y squared. First, we compute the partial derivatives: d f by d x is 2x, and d f by d y is 2y. Therefore, the gradient vector field is (2x, 2y). Evaluating at the point P, (1, 1), we find the gradient vector is (2, 2). The magnitude of this gradient is the square root of 2 squared plus 2 squared, which equals the square root of 8, or 2 root 2. Next, let us normalize the gradient to obtain a unit direction vector, u-one: (1 over root 2, 1 over root 2). The directional derivative along u-one is the dot product of the gradient and u-one. That gives (2, 2) dot (1 over root 2, 1 over root 2), which simplifies to 2 root 2, approximately 2.83. Now, consider a perpendicular unit direction vector, u-two: (1 over root 2, minus 1 over root 2). The directional derivative along u-two is 2 over root 2 minus 2 over root 2, which equals zero. Moving along the gradient produces the maximum instantaneous increase, while moving perpendicular yields zero change.",
            "notes": "Reveal algebraic equations sequentially in sync with speech; animate u₁ in emerald green when discussing gradient direction; animate u₂ in crimson red along the contour tangent when discussing zero directional derivative."
        },
        {
            "num": 5,
            "title": "Why the Gradient is the Steepest Direction",
            "time": "04:00 - 05:04",
            "dur": "64.46 sec",
            "text": "Why is the gradient direction guaranteed to be the steepest? The answer lies in the geometric definition of the dot product. The directional derivative in any unit direction u is given by the dot product of the gradient and u. By definition, this equals the magnitude of the gradient, times the magnitude of u, times the cosine of theta, where theta is the angle between the gradient and the direction vector. Because u is a unit vector, its magnitude is 1. Thus, the directional derivative simplifies to the magnitude of the gradient times cosine of theta. Now recall that cosine of theta is bounded between minus 1 and 1. Its absolute maximum is 1, which occurs if and only if theta equals zero degrees. When theta is zero, your direction vector u points in the exact same direction as the gradient vector! Therefore, the rate of increase is maximized precisely in the direction of the gradient, and the magnitude of the gradient gives that maximum rate: 2 root 2.",
            "notes": "Sync dot product formula reveal with narration; as narration discusses theta=90° and theta=180°, animate rotating vector u on the unit wheel tracker; hold at theta=0° for final maximum conclusion."
        },
        {
            "num": 6,
            "title": "Summary and Closing Credits",
            "time": "05:04 - 05:45",
            "dur": "40.87 sec",
            "text": "To summarize our journey: First, the gradient is a vector whose components are the partial derivatives of the function. Second, the gradient always points perpendicular to contour lines, in the direction of steepest increase. Third, its magnitude represents that maximum possible rate of increase. This concludes our M3 Internal Assessment animation project. Created by Lohamsa Vallika, Student ID e25b070627, B.Tech CSE AI and ML at Newton School of Technology. Thank you for watching, and keep exploring mathematics!",
            "notes": "Fade in three summary points consecutively; emphasize master formula; transition smoothly to formal closing credits card with full student details and AI disclosure."
        }
    ]
    
    for item in script_data:
        t_data = [
            [Paragraph(f"<b>SCENE {item['num']}: {item['title'].upper()}</b>", st['bold']), Paragraph(f"<b>Time:</b> {item['time']} ({item['dur']})", st['body'])],
            [Paragraph(f"<b>Spoken Narration:</b><br/>\"{item['text']}\"", st['body']), ""],
            [Paragraph(f"<b>Synchronization Notes:</b> {item['notes']}", st['body']), ""]
        ]
        t = Table(t_data, colWidths=[370, 130])
        t.setStyle(TableStyle([
            ('SPAN', (0,1), (1,1)),
            ('SPAN', (0,2), (1,2)),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F1F5F9")),
            ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor("#0284C7")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 7),
            ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 10))
        
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Generated: {output_path}")

# ==============================================================================
# 3. MATHEMATICAL VERIFICATION PDF
# ==============================================================================
def generate_math_verification_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    st = get_base_styles()
    elements = []
    
    elements.append(Paragraph("MATHEMATICAL VERIFICATION DOCUMENT", st['title']))
    elements.append(Paragraph(f"Step-by-Step Proofs & Formal Derivations | {PROJECT_TITLE}", st['subtitle']))
    elements.append(create_metadata_card("Formal Mathematical Verification & Derivations"))
    elements.append(Spacer(1, 14))
    
    sections = [
        ("1. Target Function Definition", [
            "We consider the two-variable scalar function f: R² -> R defined by:",
            "<b>f(x, y) = x² + y²</b>",
            "This defines a circular paraboloid bowl in three dimensions with a global minimum at the origin (0, 0) where f(0, 0) = 0."
        ]),
        ("2. Partial Derivatives", [
            "The first partial derivatives represent instantaneous rates of change along the coordinate axes:",
            "• With respect to x (holding y constant):<br/><b>∂f / ∂x = d/dx [x² + y²] = 2x + 0 = 2x</b>",
            "• With respect to y (holding x constant):<br/><b>∂f / ∂y = d/dy [x² + y²] = 0 + 2y = 2y</b>",
            "Both partial derivatives are continuous everywhere on R², confirming that f is continuously differentiable (C¹)."
        ]),
        ("3. The Gradient Vector Field", [
            "By definition, the gradient operator ∇ applied to a scalar field f(x,y) yields a vector field:",
            "<b>∇f(x, y) = ( ∂f/∂x, ∂f/∂y ) = ( 2x, 2y )</b>",
            "Evaluating at the representative test point <b>P = (1, 1)</b>:",
            "<b>f(1, 1) = 1² + 1² = 2</b>",
            "<b>∇f(1, 1) = ( 2(1), 2(1) ) = ( 2, 2 )</b>"
        ]),
        ("4. Gradient Magnitude (Norm)", [
            "The Euclidean norm (magnitude) of the gradient vector at P(1, 1) is:",
            "<b>|∇f(1, 1)| = √( (∂f/∂x)² + (∂f/∂y)² ) = √( 2² + 2² ) = √( 4 + 4 ) = √8 = 2√2 ≈ 2.8284</b>"
        ]),
        ("5. Unit Gradient Direction Vector (u₁)", [
            "Normalizing ∇f(1, 1) produces a unit direction vector u₁ pointing along the gradient:",
            "<b>u₁ = ∇f(1,1) / |∇f(1,1)| = ( 2 / (2√2), 2 / (2√2) ) = ( 1/√2, 1/√2 )</b>",
            "Verification of unit norm: |u₁| = √( (1/√2)² + (1/√2)² ) = √( 1/2 + 1/2 ) = √1 = 1. (Verified)"
        ]),
        ("6. Perpendicular Unit Direction Vector (u₂)", [
            "Let u₂ be a unit vector orthogonal to u₁ in the xy-plane:",
            "<b>u₂ = ( 1/√2, -1/√2 )</b>",
            "Orthogonality check via dot product:",
            "<b>u₁ · u₂ = (1/√2)(1/√2) + (1/√2)(-1/√2) = 1/2 - 1/2 = 0</b> (Strictly Orthogonal)",
            "Geometrically, u₂ is tangent to the circular level curve x² + y² = 2 at P(1, 1)."
        ]),
        ("7. Directional Derivatives Verification", [
            "The directional derivative of f in unit direction u = (a, b) is given by:",
            "<b>Dᵤ f(x, y) = ∇f(x, y) · u</b>",
            "<br/><b>Case A: Direction along the Gradient (u₁):</b>",
            "D_{u₁} f(1, 1) = (2, 2) · ( 1/√2, 1/√2 ) = 2(1/√2) + 2(1/√2) = 4/√2 = <b>2√2 ≈ 2.8284</b>",
            "Notice that D_{u₁} f(1, 1) = |∇f(1, 1)|.",
            "<br/><b>Case B: Direction along the Perpendicular Tangent (u₂):</b>",
            "D_{u₂} f(1, 1) = (2, 2) · ( 1/√2, -1/√2 ) = 2(1/√2) - 2(1/√2) = <b>0</b>",
            "This confirms that moving along the contour line produces zero instantaneous change."
        ]),
        ("8. Proof: Why the Gradient Points in the Direction of Steepest Increase", [
            "<b>Theorem:</b> Let f: R² -> R be differentiable at point P. The directional derivative Dᵤ f(P) is maximized when the unit direction vector u points in the exact direction of ∇f(P), and the maximum value is |∇f(P)|.",
            "<br/><b>Proof:</b>",
            "By definition of the Euclidean inner product (dot product):",
            "<b>Dᵤ f = ∇f · u = |∇f| |u| cos θ</b>",
            "where θ is the angle between the vectors ∇f and u.",
            "Because u is a unit vector, |u| = 1. Therefore:",
            "<b>Dᵤ f = |∇f| cos θ</b>",
            "The scalar magnitude |∇f| is non-negative (|∇f| ≥ 0). The value of cos θ is bounded on the real domain:",
            "<b>-1 ≤ cos θ ≤ +1</b>",
            "The maximum possible value of cos θ is +1. In the interval [0, 2π), cos θ = 1 occurs if and only if:",
            "<b>θ = 0° (or 0 radians)</b>",
            "When θ = 0°, the direction vector u is collinear and codirectional with ∇f:",
            "<b>u = ∇f / |∇f|</b>",
            "Under this condition, the directional derivative reaches its absolute maximum:",
            "<b>max(Dᵤ f) = |∇f| (1) = |∇f|</b>",
            "Conversely, the minimum possible value occurs when cos θ = -1 (θ = 180°), producing the direction of steepest descent:",
            "<b>min(Dᵤ f) = -|∇f|</b>",
            "And when θ = 90° (orthogonal to gradient), cos(90°) = 0, meaning directional derivative is zero along contour lines.",
            "<b>Q.E.D. (Quod Erat Demonstrandum)</b>"
        ]),
        ("9. Summary Table of Directional Derivatives at P(1,1)", [
            "Below is a tabular summary verifying key angles and rates:"
        ])
    ]
    
    for sec_title, lines in sections:
        elements.append(Paragraph(sec_title, st['h2']))
        for line in lines:
            elements.append(Paragraph(line, st['body']))
        elements.append(Spacer(1, 6))
        
    # Table of angles
    table_data = [
        ["Direction", "Vector u", "Angle θ", "cos θ", "Directional Derivative Dᵤf", "Geometric Meaning"],
        ["Gradient (u₁)", "(1/√2, 1/√2)", "0°", "+1.0", "2√2 ≈ +2.828", "Steepest Ascent (Maximum)"],
        ["Intermediate", "(1, 0)", "45°", "+0.707", "2.000", "Partial derivative ∂f/∂x"],
        ["Intermediate", "(0, 1)", "-45°", "+0.707", "2.000", "Partial derivative ∂f/∂y"],
        ["Contour Tangent (u₂)", "(1/√2, -1/√2)", "90°", "0.0", "0.000", "Along Level Curve (Zero Change)"],
        ["Opposite Contour", "(-1/√2, 1/√2)", "-90°", "0.0", "0.000", "Along Level Curve (Zero Change)"],
        ["Steepest Descent (-u₁)", "(-1/√2, -1/√2)", "180°", "-1.0", "-2√2 ≈ -2.828", "Steepest Descent (Minimum)"]
    ]
    t_summary = Table(table_data, colWidths=[90, 80, 50, 45, 110, 125])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0284C7")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#DCFCE7")), # Green for max
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#F1F5F9")),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#F1F5F9")),
        ('BACKGROUND', (0,6), (-1,6), colors.HexColor("#FEE2E2")), # Red for min
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('ALIGN', (2,0), (4,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-1), 4),
    ]))
    elements.append(t_summary)
    elements.append(Spacer(1, 14))
    
    # Sign-off verification
    signoff_text = (
        f"<b>Prepared & Verified by:</b> {STUDENT_NAME} (Student ID: {STUDENT_ID})<br/>"
        f"<b>Institution:</b> {COLLEGE} | <b>Branch:</b> {BRANCH}<br/>"
        f"<b>Assessment:</b> Linear Algebra & Calculus (M3) Internal Assessment"
    )
    elements.append(Paragraph(signoff_text, st['body']))
    
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Generated: {output_path}")

def main():
    docs_dir = "M3_AnimationVideo_Gradient_e25b070627/Documents"
    os.makedirs(docs_dir, exist_ok=True)
    
    generate_storyboard_pdf(f"{docs_dir}/Storyboard.pdf")
    generate_narration_pdf(f"{docs_dir}/Narration_Script.pdf")
    generate_math_verification_pdf(f"{docs_dir}/Mathematical_Verification.pdf")
    print("\nAll 3 PDF Documents Generated Successfully!")

if __name__ == "__main__":
    main()
