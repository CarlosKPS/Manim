from manimlib.imports import *
import decimal

class IntroductionToSeriesPart1(Scene):
    def construct(self):
        # Text and Equations
        text_1 = TextMobject("Séries")
        text_1.scale(3)
        text_1.set_color_by_gradient(RED_C, PURPLE_B)
        text_2 = TextMobject("Sequência")
        text_2.scale(3)
        text_2.set_color_by_gradient(PURPLE, BLUE)
        text_3 = TextMobject("Definição: ", "Uma lista de números escritos em uma ordem definida.")
        text_3[1].next_to(text_3, DOWN)
        text_3[0].set_color(BLUE_B)
        text_3[0].scale(1.6)
        text_3[0].center()
        text_3[1].set_color_by_gradient(PURPLE, BLUE)
        text_3[1].scale(1.1)
        term_list = []
        color_list = [BLUE, DARK_BLUE, PURPLE]

        definitions_1 = TexMobject("\\{a_{1}, a_{2}, a_{3}, ... \\}", "\\{a_{n}\\}", "\\{a_{n}\\}_{n}^{\\infty}" )
        definitions_1.scale(3)
        definitions_1.set_color_by_gradient(BLUE, PURPLE)
        
        # Fibonacci function
        fibonacci_list = ["0, ", "1,"]
        n_1 = 1
        n_2 = 0
        for i in np.arange(0, 10, 1):
            n = n_1 + n_2
            fibonacci_list.append(str(n)+", ")
            n_2 = n_1
            n_1 = n
        fibonacci_list.append("...")
        fibonacci = TexMobject(*fibonacci_list)
        fibonacci_term = TexMobject("a_{n-2}", "+", "a_{n-1}", "=", "a_{n}")
        fibonacci_term.scale(2.4)
        fibonacci_term.move_to(DOWN)
        fibonacci_term.set_color_by_gradient(BLUE, GREEN, PURPLE)

        # Sequence Term
        for color, term in zip(color_list, definitions_1):
            term.center()
            term.set_color(color)
            
        for i in range(5):
            term_list.append("a_{"+str(i+1)+"}, ")
        term_list.append("..., ")
        term_list.append("a_{n}, ")
        term_list.append("...")
        
        equation = TexMobject(*term_list)
        equation.scale(1.5)

        circle_1 = Circle(color = PURPLE)
        circle_2 = Circle(color = YELLOW)
        circle_3 = Circle(color = RED)
        circle_group = VGroup(circle_1, circle_2, circle_3)

        # Animation
        
        self.play(ShowCreation(text_1))
        self.wait(4)
        self.play(FadeOutAndShift(text_1, 3.7*UP), run_time = 2)
        self.wait()
        self.play(FadeInFrom(text_2, 3*DOWN))
        self.wait()
        self.play(ApplyMethod(text_2.shift, 3*UP))
        self.wait()
        self.play(Write(text_3[0]))
        self.play(Write(text_3[1]), run_time=3)
        self.wait()
        self.play(FadeOutAndShift(text_3[0], 6*LEFT), FadeOutAndShift(text_3[1], 6*RIGHT), run_time=2)
        self.wait()
        self.play(FadeIn(equation), run_time=2)
        self.wait()
        
        # Sequence literal
        for i in range(len(equation)):
            self.play(ApplyMethod(equation[i].set_color, BLUE))
            self.play(ApplyMethod(equation[i].set_color, WHITE))

        self.play(FadeOutAndShift(equation, 4*DOWN))
        self.wait()

        # Sequence definition
        self.play(ShowCreation(definitions_1[0]))
        self.wait()
        self.play(ReplacementTransform(definitions_1[0], definitions_1[1]), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(definitions_1[1], definitions_1[2]), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShift(definitions_1[2], 3*DOWN), run_time=1)
        self.wait(4)
        
        # Fibonacci sequence
        fibonacci.set_color_by_gradient(BLUE, PURPLE)
        fibonacci.scale(1.6)
        self.play(Write(fibonacci), run_time=2)
        self.wait()
        self.play(ApplyMethod(fibonacci.shift, 1.5*UP), run_time=1)
        self.wait()
        self.play(Write(fibonacci_term))
        self.wait(2)
        circle_1.surround(fibonacci_term[0])
        circle_2.surround(fibonacci_term[2])
        circle_3.surround(fibonacci_term[4])
        self.play(ShowCreation(circle_1), run_time=2)
        self.play(ShowCreation(circle_2), run_time=2)
        self.play(ShowCreation(circle_3), run_time=2)
        self.wait(2)
        self.play(Uncreate(circle_1), Uncreate(circle_2), Uncreate(circle_3))
        self.wait(4)
        
        n_1 = 1
        n_2 = 1
        aux_arc_1 = 0
        aux_arc_2 = 0
        aux_arc_3 = 0
        
        aux_circ_1 = 0
        aux_circ_2 = 0
        aux_circ_3 = 0

        for i in range(len(fibonacci)-4):
            circle_1.surround(fibonacci[i+1])
            circle_2.surround(fibonacci[i+2])
            circle_3.surround(fibonacci[i+3])
            
            
            n = n_1 + n_2
            text_list = [str(n_2), "+", str(n_1), "=", str(n)]
            text = TexMobject(*text_list).scale(2.4)
            text.move_to(DOWN)
            text[0].set_color(PURPLE)
            text[2].set_color(YELLOW)
            text[4].set_color(RED)

            arc_1 = Arrow(circle_1.get_bottom(), text[0].get_top(), color = PURPLE)
            arc_2 = Arrow(circle_2.get_bottom(), text[2].get_top(), color = YELLOW)
            arc_3 = Arrow(circle_3.get_bottom(), text[4].get_top(), color = RED)
            

            
            if i == 0:
                aux_arc_1 = arc_1
                aux_arc_2 = arc_2
                aux_arc_3 = arc_3
                aux_circ_1 = circle_1
                aux_circ_2 = circle_2
                aux_circ_3 = circle_3
        
                self.play()
                self.play(ShowCreation(circle_1), ShowCreation(circle_2), 
                            ShowCreation(circle_3), ShowCreation(arc_1), 
                            ShowCreation(arc_2), ShowCreation(arc_3),
                            ReplacementTransform(fibonacci_term, text))
                
            else:
                self.play(ReplacementTransform(aux_circ_1, circle_1), ReplacementTransform(aux_circ_2, circle_2),
                            ReplacementTransform(aux_circ_3, circle_3), ReplacementTransform(aux_arc_1, arc_1), 
                            ReplacementTransform(aux_arc_2, arc_2), ReplacementTransform(aux_arc_3, arc_3),
                            ReplacementTransform(fibonacci_term, text))

            aux_arc_1 = arc_1
            aux_arc_2 = arc_2
            aux_arc_3 = arc_3
            
            fibonacci_term = text
            n_2 = n_1
            n_1 = n
        
        self.play(Uncreate(circle_1), Uncreate(circle_2), 
                Uncreate(circle_3), Uncreate(arc_1), 
                Uncreate(arc_2), Uncreate(arc_3),
                Uncreate(text), Uncreate(fibonacci))
        self.play(FadeOutAndShift(text_2, 4*DOWN))
        self.wait(3)
                
class IntroductionToSeriesPart2(Scene):
    def construct(self):
        n_term = TexMobject("\\{\\frac{n}{n+1}\\}_{n=1}^{\\infty}").scale(2)
        n_term.set_color_by_gradient(BLUE_D, PURPLE_D)
        n = TexMobject("N = ", "\\, ").scale(1.5)
        n.center()
        n.set_color_by_gradient(PURPLE, BLUE)


        self.add(n_term)
        self.wait(2)
        self.play(ApplyMethod(n_term.shift, 2.5*UP), run_time=2)
        self.wait(2)

        div_list, num_list = ["{"],["{"]
        for i in range(10):
            num_list.append(str(i+1))
            div_list.append(str(i+2))
        num_list.append("}")
        div_list.append("}")

        self.play(ShowCreation(n), run_time=2)
        self.wait(2)

        color_list = [BLUE_C, BLUE_B, PURPLE_B, PURPLE_A, PURPLE_C, YELLOW_A, GREEN_A, PINK, BLUE_A, GREEN_B, BLUE_D]
        
        frac_list = ["{ "]
        for i in range(len(num_list)-2):
            frac_list.append("\\frac{"+num_list[i+1]+"}{"+div_list[i+1]+"}"+",")
        frac_list.append("...}")
        frac = TexMobject(*frac_list).scale(2)
        frac.center()
        frac.move_to(2.5*DOWN)
        frac.set_color_by_gradient(PURPLE, BLUE)

        
        for k in range(len(num_list)-2):
            new_n = TexMobject(str(k+1)).scale(1.5)
            new_n.next_to(n[0], RIGHT)
            new_n.set_color(color_list[k])
                
            self.play(Transform(n[1], new_n)) 
            self.play(ReplacementTransform(n_term.copy(), frac[k+1:k+2]))
            self.wait(2)

        self.play(Write(frac[-1]), run_time=2)
        self.wait(4)

        brace_group = VGroup()
        for i in range(len(num_list)-2):
            brace = Brace(frac[i+1], UP, buff = SMALL_BUFF)
            brace.set_color_by_gradient(PURPLE, BLUE)
            title = brace.get_text("$"+str("{0:.3f}".format((float(num_list[i+1])/float(div_list[i+1]))))+"$").set_color(PURPLE)
            if i == 0:
                self.play(ShowCreation(brace), ShowCreation(title))
                self.wait(2)
            else:
                self.play(ReplacementTransform(brace_1, brace),
                        ReplacementTransform(title_1, title))
                self.wait(2)
            brace_1 = brace
            title_1 = title
        
        self.play(FadeOut(brace), FadeOut(title), FadeOut(n_term), FadeOut(n))
        self.play(ApplyMethod(frac.shift, 2*UP))


        for i in range(int(len(num_list))-3):
            brace = Brace(frac[i+1], UP, buff = SMALL_BUFF)
            brace.set_color_by_gradient(PURPLE, BLUE)
            
            brace_1 = Brace(frac[i+2], UP, buff = SMALL_BUFF)
            brace.set_color_by_gradient(PURPLE, BLUE)
            
            
            a = float(num_list[i+1])/float(div_list[i+1])
            b = float(num_list[i+2])/float(div_list[i+2])
            c = a - b

            sub = TexMobject(*[str("{0:.3f}".format(a)), "-", str("{0:.3f}".format(b)), "=", str("{0:.3f}".format(c))]).scale(1.4)
            sub.move_to(3*UP)
            sub.set_color_by_gradient(PURPLE_C, BLUE_C)

            title = brace.get_text("$"+str("{0:.3f}".format((float(num_list[i+1])/float(div_list[i+1]))))+"$").set_color_by_gradient(BLUE, PURPLE).scale(0.7)
            title_1 = brace_1.get_text("$"+str("{0:.3f}".format((float(num_list[i+2])/float(div_list[i+2]))))+"$").set_color_by_gradient(BLUE, PURPLE).scale(0.7)

            
            if i == 0:
                self.play(ShowCreation(brace), ShowCreation(brace_1), ShowCreation(title), ShowCreation(title_1))
                self.play(FadeInFrom(sub, 5*UP))
                self.wait(2)
            else:
                self.play(ReplacementTransform(aux_brace, brace),
                        ReplacementTransform(aux_title, title),
                        ReplacementTransform(aux_brace_1, brace_1),
                        ReplacementTransform(aux_title_1, title_1))
                self.play(ReplacementTransform(aux_sub, sub))
                self.wait(2)

            aux_brace = brace
            aux_brace_1 = brace_1
            aux_title = title
            aux_title_1 = title_1
            aux_sub = sub

class IntroductionToSeriesPart3(Scene):
    def construct(self):
        pass

class IntroductionToSeriesPart4(Scene):

    def construct(self):
        # Texts
        text_1 = TextMobject("Séries")
        text_1.scale(3)
        text_1.set_color_by_gradient(RED_C, PURPLE_B)
        # Pi number
        pi_text = TexMobject("\\pi", "=", str(PI),"...")
        pi_text.set_color_by_gradient(RED, PURPLE)
        pi_dec = decimal.Decimal(format(PI, '.10f'))
        pi_tuple = pi_dec.as_tuple()[1]

        pi_list = []
        for i in range(10):
            pi_list.append("\\frac{"+str(pi_tuple[i])+"}{10^{"+str(i)+"}} +")
        pi_list.append("...")
        pi_sum = TexMobject(*pi_list).scale(0.8)
        pi_sum.next_to(pi_text[1], RIGHT)
        pi_sum.set_color_by_gradient(RED, PURPLE)

        #Braces
        braces_group = VGroup()
        for i in pi_sum[:10]:
            braces = Brace(i, UP, buff = SMALL_BUFF)


        # Animation
        self.play(FadeInFrom(text_1, 4*DOWN), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShift(text_1, 5*UP))
        self.wait()
        self.play(Write(pi_text))
        self.wait()
        self.play(ReplacementTransform(pi_text[2], pi_sum))
        self.play(ApplyMethod(pi_text.shift, 3.5*LEFT), ApplyMethod(pi_sum.shift,3.5*LEFT))
        self.wait()
        for i,term in enumerate(pi_sum):
            if i == len(pi_sum)-1:
                break

            brace = Brace(pi_sum[i], UP, buff = SMALL_BUFF)
            brace.set_color_by_gradient(RED, PURPLE)
            #title = brace.get_text("$"+str(float(pi_tuple[i]/(10**i)))+"$")
            a = float(pi_tuple[i]/(10**i))
            b = "{0:."+str(i)+"f}"
            title = brace.get_text("$"+b.format(a)+"$").set_color_by_gradient(ORANGE, YELLOW)
            if i ==0:
                self.play(GrowFromCenter(brace), FadeIn(title))
                self.wait()
                brace_1 = brace
                title_1 = title
            else:
                self.play(ReplacementTransform(brace_1, brace), ReplacementTransform(title_1, title), run_time = 2)
                self.wait()
            
            brace_1 = brace
            title_1 = title
        self.wait(4)