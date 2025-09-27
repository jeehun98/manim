# manim_quickstart.py
# -------------------------------------------------------------
# A compact set of Manim scenes you can render immediately.
# Tested with Manim Community v0.19.x on Windows with Python 3.10+
# -------------------------------------------------------------
# How to render (examples):
#   manim -pqh manim_quickstart.py HelloManim        # quick preview (low quality)
#   manim -p   manim_quickstart.py HelloManim        # default quality (1080p)
#   manim -p   manim_quickstart.py PlotSine          # render another scene
#   manim -p -r 2560,1440 manim_quickstart.py PlotSine    # custom resolution
#   manim -p -o hello.gif manim_quickstart.py HelloManim  # export as GIF
#   manim -p --format=png --save_last_frame manim_quickstart.py HelloManim
#
# Flags:
#   -p/--preview   : auto-open output after render
#   -qk/-ql/-qm/-qh: quality (k=4k, l=low, m=medium, h=high)
#   -r W,H         : custom resolution
#   -o NAME        : output file name
#   --format=mp4|gif|png  : output format
#   --fps N        : frames per second
# -------------------------------------------------------------

from manim import *

# 1) Minimal text write
class HelloManim(Scene):
    def construct(self):
        t = Tex(r"Hello, \\texttt{Manim}!")
        self.play(Write(t))
        self.wait(0.5)
        self.play(t.animate.set_color(YELLOW).scale(1.2))
        self.wait(0.5)

# 2) LaTeX math + transforms
class MathTransform(Scene):
    def construct(self):
        a = MathTex(r"e^{i\pi} + 1 = 0")
        b = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}")
        self.play(Write(a))
        self.wait(0.6)
        self.play(Transform(a, b))
        self.wait(0.6)

# 3) Axes + animated curve (ValueTracker)
class PlotSine(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 2*PI, PI/2], y_range=[-1.2, 1.2, 0.5],
                  x_length=8, y_length=3.5, tips=False)
        labels = ax.get_axis_labels(Tex("x"), Tex("y"))
        self.play(Create(ax), FadeIn(labels))

        amp = ValueTracker(1.0)

        def curve():
            return ax.plot(lambda x: amp.get_value()*np.sin(x), color=BLUE)

        g = always_redraw(curve)
        self.play(Create(g))
        self.wait(0.5)
        self.play(amp.animate.set_value(0.2), run_time=1.2)
        self.play(amp.animate.set_value(1.0), run_time=1.2)
        self.wait(0.3)

# 4) VGroup layout + basic animations
class GridAndShapes(Scene):
    def construct(self):
        sq = Square().set_fill(BLUE, 0.6)
        cr = Circle().set_fill(RED, 0.6)
        tr = Triangle().set_fill(GREEN, 0.6)
        grp = VGroup(sq, cr, tr).arrange(RIGHT, buff=1)
        self.play(FadeIn(grp, shift=DOWN))
        self.play(Rotate(grp, angle=PI/4))
        self.play(grp.animate.scale(1.2))
        self.play(grp.animate.set_opacity(0.4))
        self.wait(0.3)

# 5) Updaters + counters
class CounterDemo(Scene):
    def construct(self):
        val = ValueTracker(0)
        num = always_redraw(lambda: DecimalNumber(val.get_value(),
                                                  num_decimal_places=2).to_edge(UR))
        self.add(num)
        self.play(val.animate.set_value(10), run_time=2, rate_func=linear)
        self.wait(0.2)

# 6) Camera movement
class CameraPan(Scene):
    def construct(self):
        big = NumberPlane(x_range=[-6,6,1], y_range=[-4,4,1])
        dot = Dot([2,1,0], color=YELLOW)
        self.add(big, dot)
        self.play(self.camera.frame.animate.scale(0.7).move_to(dot))
        self.wait(0.3)

# 7) Save last frame (diagrams/thumbnail)
class Thumbnail(Scene):
    def construct(self):
        t = Tex("My Video Title").scale(1.3)
        box = RoundedRectangle(width=6.5, height=3.6, corner_radius=0.3)
        grp = VGroup(box, t).arrange(DOWN, buff=0.5)
        self.add(grp)
        # Render with: manim -p --format=png --save_last_frame manim_quickstart.py Thumbnail
