from manim import *


import MotionClouds as mc


class Intro(Scene):
    def construct(self):



        # my_object = MathTex(r"\Updownarrow").scale(8)
        my_object = Rectangle(width=1.0, height=4.0)
        # square = Square()  # create a square
        run_time = 3
        self.play(Create(my_object), run_time=run_time)  # show the square on screen
        self.play(
            my_object.animate.set_fill(PINK, opacity=0.5)
        )  # color the text on screen
        self.play(my_object.animate.rotate(PI / 5), run_time=run_time/2)  # rotate the square
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)  # rotate the square

        vertical = DashedLine(config.top, config.bottom, dash_length=2.0, color=RED)

        self.add(vertical)  # show the square on screen
        

        self.play(my_object.animate.rotate(PI / 2.5), run_time=run_time)  # rotate the square
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)  # rotate the square
        