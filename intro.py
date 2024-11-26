# manim -pql intro.py Intro 

from manim import *



import MotionClouds as mc


class Intro(Scene):
    def construct(self):
        run_time = 1

        #--------------------------------
        title = Title(f"Orientation discrimination experiment")
        text1 = Tex('Welcome to this psychophysics experiment !').shift(2*UP)
        text2 = Tex('It studies the perception of the orientation of contours').shift(UP)
        text3 = Tex('in images with different levels of difficulty.') 
        text4 = Tex('Your input to understand percption is important,').shift(DOWN)
        text5 = Tex('many thanks for participating !').shift(2*DOWN)

        self.add(title)
        self.wait(run_time)
        self.add(text1)
        self.wait(run_time)
        self.add(text2)
        self.wait(run_time)
        self.add(text3)
        self.wait(run_time)
        self.add(text4)
        self.wait(run_time)
        self.add(text5)
        self.wait(run_time)
        self.wait(run_time)
        self.remove(title, text1, text2, text3, text4, text5)
        #--------------------------------

        run_time = 2
        # my_object = MathTex(r"\Updownarrow").scale(8)
        my_object = Rectangle(width=1.0, height=4.0)
        # square = Square()  # create a square
        
        title = Text("Consider a visual object like this rectangle...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        # self.wait(run_time)
        self.play(Create(my_object), run_time=run_time) 
        self.remove(title)
        title = Text("...we may want to estimate its orientation...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(
            my_object.animate.set_fill(PINK, opacity=0.5)
        )  # color the text on screen
        self.wait(run_time)
        self.remove(title)

        title = Text("...if it is tilted in one direction...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(my_object.animate.rotate(PI / 5), run_time=run_time/2)  
        self.remove(title)

        title = Text("...or rather in the other...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)
        self.remove(title)

        vertical = DashedLine(config.top, config.bottom, dash_length=2.0, color=RED)

        # self.add(vertical) 
        title = Text("Here we choose the vertical as a reference...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(Create(vertical), run_time=run_time) 
        self.remove(title)

        title = Text("...to judge if it is tilted counter-clockwise...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(my_object.animate.rotate(PI / 2.5), run_time=run_time)
        self.remove(title)

        title = Text("..or rather clockwise.", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)
        self.remove(title)
        self.remove(vertical)

        self.play(Unwrite(my_object)) 

        #--------------------------------
        im_height = 6
        
        image = ImageMobject('img_pilot/83.png')

        line = Line(ORIGIN, LEFT)        
        image.height = im_height
        self.add(image)
        title = Text("You will be presented textures with a main orientation of contours...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.wait(run_time)
        self.remove(title)

        title = Text("...here it is counter-clockwise relative to the vertical...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(Create(vertical), run_time=run_time) 
        self.remove(title)
        self.remove(vertical)

        title = Text("...so click or swipe left.", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear)
        self.wait(run_time)
        self.remove(title)

        self.remove(image)

        #--------------------------------
        
        image = ImageMobject('img_pilot/113.png')
        line = Line(ORIGIN, RIGHT)        
        image.height = im_height
        self.add(image)
        self.wait(run_time)
        title = Text("That one is clockwise relative to the vertical...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(Create(vertical), run_time=run_time) 
        self.remove(title)

        title = Text("...so click or swipe right.", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear, run_time=run_time)
        self.remove(title)
        self.remove(image)
        self.remove(vertical)

        # #--------------------------------
        
        run_time = 2
        image = ImageMobject('img_pilot/139.png')
        line = Line(ORIGIN, LEFT)        
        image.height = im_height
        self.add(image)
        self.wait(run_time)
        title = Text("Some orientations are closer to the vertical...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear, run_time=run_time)
        self.remove(title)
        self.remove(image)

        #--------------------------------
        
        image = ImageMobject('img_pilot/161.png')
        line = Line(ORIGIN, LEFT)        
        image.height = im_height
        self.add(image)
        self.wait(run_time)
        title = Text("Some are harder to detect...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear, run_time=run_time)
        self.remove(title)
        self.remove(image)

        #--------------------------------
        
        image = ImageMobject('img_pilot/153.png')
        line = Line(ORIGIN, RIGHT)        
        image.height = im_height
        self.add(image)
        self.wait(run_time)
        title = Text("... however, always answer left or right!", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear, run_time=run_time)
        self.remove(title)
        self.remove(image)

        #--------------------------------
        run_time = 1

        title = Title(f"Orientation discrimination experiment")
        text1 = Tex('One experiment lasts about 4 minutes for 216 images.').shift(2*UP)
        text2 = Tex('Total time depends on your speed to judge orientation...').shift(UP)
        text3 = Tex('...so relax and do no hesitate to respond as fast as possible.') 
        text4 = Tex('Your overall score will be shared at the end of the experiment,').shift(DOWN)
        text5 = Tex('many thanks for participating !').shift(2*DOWN)

        self.add(title)
        self.wait(run_time)
        self.add(text1)
        self.wait(run_time)
        self.add(text2)
        self.wait(run_time)
        self.add(text3)
        self.wait(run_time)
        self.add(text4)
        self.wait(run_time)
        self.add(text5)
        self.wait(run_time)
        self.wait(run_time)
        self.remove(title, text1, text2, text3, text4, text5)
        #--------------------------------