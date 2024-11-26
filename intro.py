# manim -pql intro.py Intro 

from manim import *



import MotionClouds as mc


class Intro(Scene):
    def construct(self):
        run_time = 1

        title = Title(f"Orientation discrimination experiment")
        text1 = Tex('The horse does not eat cucumber salad.').shift(2*UP)
        text2 = Tex('The horse does not eat 2 salad.').shift(UP)
        text3 = Tex('The horse does not eat 3 salad.') 
        text4 = Tex('The horse does not eat 4 salad.\\ dkjhkhfqkjf \\ lhdslfqhj ').shift(DOWN)

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
        self.remove(title, text1, text2, text3, text4)
        #--------------------------------

        # my_object = MathTex(r"\Updownarrow").scale(8)
        my_object = Rectangle(width=1.0, height=4.0)
        # square = Square()  # create a square
        self.play(Create(my_object), run_time=run_time) 
        self.play(
            my_object.animate.set_fill(PINK, opacity=0.5)
        )  # color the text on screen
        self.play(my_object.animate.rotate(PI / 5), run_time=run_time/2)  
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)

        vertical = DashedLine(config.top, config.bottom, dash_length=2.0, color=RED)

        # self.add(vertical) 
        self.play(Create(vertical), run_time=run_time) 
        

        self.play(my_object.animate.rotate(PI / 2.5), run_time=run_time)
        self.play(my_object.animate.rotate(-PI / 2.5), run_time=run_time)

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
        # self.wait(run_time)
        title = Text("That one is clockwise relative to the vertical...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(Create(vertical), run_time=run_time) 
        self.remove(title)

        title = Text("...so click or swipe right.", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear, run_time=run_time)
        self.remove(title)
        self.remove(image)

        # #--------------------------------
        
        image = ImageMobject('img_pilot/139.png')
        line = Line(ORIGIN, LEFT)        
        image.height = im_height
        self.add(image)
        # self.wait(run_time)
        title = Text("Some orientations are closer to the vertical...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear)
        self.remove(title)
        self.remove(image)

        #--------------------------------
        
        image = ImageMobject('img_pilot/161.png')
        line = Line(ORIGIN, RIGHT)        
        image.height = im_height
        self.add(image)
        # self.wait(run_time)
        title = Text("Some are harder to detect...", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear)
        self.remove(title)
        self.remove(image)

        #--------------------------------
        
        image = ImageMobject('img_pilot/153.png')
        line = Line(ORIGIN, RIGHT)        
        image.height = im_height
        self.add(image)
        # self.wait(run_time)
        title = Text("... however, always answer left or right!", color=WHITE).scale(0.75)
        self.add(title.to_edge(DOWN))
        self.play(MoveAlongPath(image, line), rate_func=linear)
        self.remove(title)
        self.remove(image)