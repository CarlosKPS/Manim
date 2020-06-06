from manimlib.imports import *


class FirstSignal(Scene):
    def construct(self):
        text_1 = TextMobject("Sinais e Sistemas")
        text_2 = TextMobject("O Que é um sinal???")
        text_def = TextMobject("Definições.")
        text_3 = [["""Comum:""", """Qualquer manifestação que permite conhecer, reconhecer\\\\ ou prever alguma coisa.""" ],
            ["""Eletricidade:""", """Impulso elétrico que entra num circuitou ou sai dele."""],
            ["""Informática:""","""Impulso eletrônico que corresponde a uma \\\\unidade mínima de informação."""]
        ]
        text_4 = TextMobject("Sinais São representados\\\\ matematicamente por funções.")
        text_5 = [[r"f(x)", r"f(t)"], [r"x(t)", r"u(t)"]]


        text_1.scale(2)
        text_2.scale(2)
    
        self.play(GrowFromCenter(text_1))
        self.wait()
        self.play(ReplacementTransform(text_1.copy(), text_2), FadeOut(text_1))
        self.wait()
        self.play(FadeOut(text_2))
        self.wait()
        self.play(GrowFromCenter(text_def))
        self.play(ApplyMethod(text_def.shift, 3*UP))
        self.wait()
        for text in text_3:
            t1 = TextMobject(text[0])
            t2 = TextMobject(text[1])
            t1.move_to(UP)
            t2.next_to(t1, 2*DOWN)
            self.play(Write(t1), Write(t2))
            self.wait()
            self.play(FadeOut(t1), FadeOut(t2))
            self.wait()
        self.play(FadeOutAndShiftDown(text_def))
        self.wait()
        text_4.scale(2)
        self.play(Write(text_4))
        self.play(ApplyMethod(text_4.move_to, 2.5*UP))
        self.wait()
        for eq in text_5:
            t1 = TexMobject(eq[0])
            t2 = TexMobject(eq[1])
            t1.scale(2)
            t2.scale(2)
            self.play(FadeIn(t1))
            self.wait()
            self.play(Transform(t1,t2))
            self.wait()
            self.play(FadeOut(t1), FadeOut(t2))
            self.wait()
            
        self.play(FadeOut(text_4))
        self.wait(2)

class Continuo1(Scene):
    def construct(self):
        #Texts----------------------------------
        text_1 = TextMobject("Sinais contínuos.")
        text_1.scale(2)

        #Functions-----------------------------
        tfunc_1 = ["$x($","$t$","$)$"]
        definition = TextMobject("""$t \\in \\mathbb{R}$""")
        definition.scale(2)
        f1 = TextMobject(*tfunc_1)
        f1.scale(2)

        #Geometrics----------------------------
        circle = Circle(color=YELLOW)
        circle.surround(f1[1])
        #Animations
        self.play(FadeIn(text_1))
        self.wait()
        self.play(ApplyMethod(text_1.move_to, 3*UP))
        self.wait()        
        self.play(Write(f1))
        self.wait()
        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(FadeOut(circle))
        self.wait()
        self.play(ApplyMethod(f1.move_to, 1.5*UP))
        self.wait()
        self.play(Write(definition))
        self.wait(2)


class Continuo2(GraphScene):
    CONFIG = {
        "x_min": -4*PI,
        "x_max": 4*PI,
        "x_tick_frequency": PI/2,
        "y_max": 1.5,
        "y_min": -1.5,
        "y_tick_frequency": 0.5,
        "grid": True,
        "graph_origin": ORIGIN+0.5*DOWN,
        "x_axis_label": None,
        "y_axis_label": None, 
    }
    def construct(self):
        self.setup_axes()
        #Text ------------------------------------------------
        text_1 = TextMobject("Exemplo")
        #Graph -----------------------------------------------
        graph_1 = self.get_graph(self.func_1, color=GREEN, x_min=-4*PI,x_max=4*PI)
        graph_label_1 = self.get_graph_label(graph_1, direction=DOWN+RIGHT, label = "\\cos(\\theta)")
        
        text_1.move_to(3.7*UP)
        self.play(Write(text_1))
        self.wait()
        self.play(ShowCreation(graph_1), Write(graph_label_1), run_time=2)
        self.wait(2)
    
    #Setting some axis's prefferences 
    def setup_axes(self):
        #Always Start With this:
        GraphScene.setup_axes(self)

        #Width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)

        #Color of edges
        self.x_axis.set_color(BLUE)
        self.y_axis.set_color(BLUE)

        func = TexMobject("\\cos(\\theta)")
        var = TexMobject("\\theta")
        func.set_color(BLUE_E)
        var.set_color(BLUE_E)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)

        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1, 1])

        init_val_x = -4*PI
        step_x = PI/2
        end_val_x = 4*PI

        values_decimal_x= list(np.arange(init_val_x, end_val_x, step_x))

        list_x=TexMobject("-4\\pi",
                            "-7\\frac{\\pi}{2}",
                            "-3\\pi", 
                            "-5\\frac{\\pi}{2}",
                            "-2\\pi",
                            "-3\\frac{\\pi}{2}",
                            "-\\pi",
                            "-\\frac{\\pi}{2}", 
                            "0",                  
                            "\\frac{\\pi}{2}",
                            "\\pi",
                            "3\\frac{\\pi}{2}",
                            "2\\pi",
                            "5\\frac{\\pi}{2}",
                            "3\\pi",
                            "7\\frac{\\pi}{2}",
                            "4\\pi",
                          )
        #List of tuples (position, label)
        values_x =[ (i, j) for i,j in zip(values_decimal_x, list_x)]

        self.x_axis_labels = VGroup()

        for x_val, x_tex in values_x:
            x_tex.scale(0.4)
            x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            if x_val == 0:
                x_tex.scale(1.2)
                x_tex.next_to(self.coords_to_point(0, 0), 0)
            self.x_axis_labels.add(x_tex)

        

        self.play(
            *[Write(objeto) 
            for objeto in [
                self.x_axis,
                self.y_axis, 
                self.x_axis_labels, 
                func, var
                ]
            ], run_time = 2
        )

    def func_1(self, x):
        return np.cos(x)

class ContinuoAndDiscrete(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_max": 1.5,
        "y_min": -1.5,
        "grid": True,
        "graph_origin": ORIGIN+DOWN,
        "x_labeled_num": np.arange(-10, 10, 1),
        "function_color": GREEN,
        "axes_color": YELLOW,
        "x_axis_label": "$t$",
        "y_axis_label": "$x(t)$" 
    }
    def construct(self):
        self.setup_axes(animate=True)
        #Text ------------------------------------------------
        text_1 = TextMobject("Exemplo")
        #Graph -----------------------------------------------
        graph_1 = self.get_graph(self.func_1, color=PURPLE, x_min=-10,x_max=10)
        graph_label_1 = self.get_graph_label(graph_1, direction=UP+RIGHT)
        vert_lines_1 = self.get_vertical_lines_to_graph(graph_1, x_min=-10, x_max=10, num_lines=20, color=BLUE)
        vert_lines_12 = self.get_vertical_lines_to_graph(graph_1, x_min=-10, x_max=10, num_lines=40, color=BLUE)
        vert_lines_13 = self.get_vertical_lines_to_graph(graph_1, x_min=-10, x_max=10, num_lines=80, color=BLUE)
        vert_lines_14 = self.get_vertical_lines_to_graph(graph_1, x_min=-10, x_max=10, num_lines=400, color=BLUE)
        
        text_1.move_to(3*UP)
        self.add(text_1)
        self.play(ShowCreation(graph_1))
        self.wait(2)
        self.play(ShowCreation(vert_lines_1))
        self.wait(2)
        self.play(FadeOut(graph_1))
        self.wait()
        self.play(Transform(vert_lines_1, vert_lines_12))
        self.wait()
        self.play(FadeIn(graph_1))
        self.wait(2)
        self.play(Transform(vert_lines_12, vert_lines_13))
        self.wait()
        self.play(FadeOut(graph_1))
        self.wait()
        self.play(Transform(vert_lines_13, vert_lines_14))
        self.wait()
        self.play(FadeIn(graph_1))
        self.wait()
        
    def func_1(self, x):
        return np.cos(x)


class ShiftInTime(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_max": 1.5,
        "y_min": -1.5,
        "grid": True,
        "graph_origin": ORIGIN,
        "x_labeled_num": np.arange(-10, 10, 1),
        "function_color": GREEN,
        "axes_color": GOLD,
        "x_axis_label": "$t$",
        "y_axis_label": "$y(t)$" 
    }

    def construct(self):
        self.setup_axes(animate=True)
        #Graph area -----------------------------------------------------------------------------------------------
        #Graph_1
        graph_1 = self.get_graph(self.func1, color = RED)
        vert_line_1 = self.get_vertical_line_to_graph(0, graph_1, color = PURPLE)
        graph_label_1 = self.get_graph_label(graph_1, label = "\\cos(t)")
        #Graph_2
        graph_2 = self.get_graph(self.func2, color = BLUE)
        vert_line_2 = self.get_vertical_line_to_graph(90*DEGREES, graph_2, color = PURPLE)
        graph_label_2 = self.get_graph_label(graph_2, label = "\\cos(t-\\frac{\\pi}{2})", x_val=-10, direction= 3*UP)

        #Geometrics-------------------------------------------------------------------------------------------------
        #Texts------------------------------------------------------------------------------------------------------
        text_1 = TextMobject("Desvio no tempo")
        text_2 = ["\\cos(t)", "\\cos(t-\\frac{\\pi}{2}"]
        text_3 = TextMobject("Diferença de $\\frac{\\pi}{2}$")
        text_3.scale(0.5)

        #groups, braces
        group_lines = VGroup(vert_line_1, vert_line_2)
        braces = Brace(group_lines, UP)
        text_3.next_to(braces, 0.2*UP+0.001*RIGHT)
        
        #Animation
        self.play(ShowCreation(graph_1), Write(graph_label_1))
        self.wait()
        self.play(ReplacementTransform(graph_1.copy(), graph_2), Write(graph_label_2))
        self.wait()
        self.play(ShowCreation(vert_line_1), ShowCreation(vert_line_2))
        self.wait()
        self.play(GrowFromCenter(braces), Write(text_3))
        self.wait()


    def func1(self, x):
        return np.cos(x)

    def func2(self, x):
        return np.cos(x-90*DEGREES)

class ShiftInTime2(Scene):
    def construct(self):
        #Texts
        eq_1 = ["cos","(", "t","-", "\\frac{\\pi}{2}",")"]
        eq = TexMobject(*eq_1)
        #Geometrics
        circle = Circle(color=YELLOW)
        #define initial transform
        eq.scale_in_place(2)
        circle.surround(eq[4])
        #Animation
        aux_eq = VGroup(eq[:3],eq[-1])
        self.play(Write(aux_eq))
        self.wait()
        self.play(Write(eq[3:5]))
        self.wait()
        self.play(ShowCreation(circle))
        self.wait()


class SignalReflection(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -1.5,
        "y_max": 1.5,
        "grid": True,
        "graph_origin": ORIGIN,
        "x_axis_label": "$t$",
        "y_axis_label": "$y(t)$"
    }
    def construct(self):
        graph_1 = self.get_graph(self.func_1, x_min=-10, x_max=10)

    def func_1(self,x ):
        return np.cos(-x)