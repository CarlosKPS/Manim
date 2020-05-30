from manimlib.imports import *


class FirstSignal(Scene):
    def construct(self):
        text_1 = TextMobject("Sinais")
        text_2 = TextMobject("O Que é um sinal???")
        text_def = TextMobject("Definições:")
        text_3 = [["""Comum:""", """Qualquer manifestação que permite conhecer, reconhecer\\\\ ou prever alguma coisa""" ],
            ["""Eletricidade:""", """impulso elétrico que entra num circuitou ou sai dele"""],
            ["""Informática:""","""Impulso eletrônico que corresponde a uma \\\\unidade mínima de informação."""],
            ["""Física/Radio Técnica""" ,"""variação de feixe de ondas eletromagnéticas."""]
        ]
        
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


        