from manim import *

class Intro(Scene):
    def construct(self):
        self.play(
            Rotate(
                MathTex(r"\bot").scale(8),
                angle=20/180*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
        )
        self.play(
            Rotate(
                MathTex(r"\bot").scale(8),
                angle=-20/180*PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
        )
        

        