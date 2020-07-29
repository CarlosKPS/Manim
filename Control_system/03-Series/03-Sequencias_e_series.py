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
        self.wait(4)
        self.play(ReplacementTransform(definitions_1[0], definitions_1[1]), run_time=3)
        self.wait(4)
        self.play(ReplacementTransform(definitions_1[1], definitions_1[2]), run_time=3)
        self.wait(4)
        self.play(FadeOutAndShift(definitions_1[2], 3*DOWN), run_time=2)
        self.wait(4)
        
        # Fibonacci sequence
        fibonacci.set_color_by_gradient(BLUE, PURPLE)
        fibonacci.scale(1.6)
        self.play(Write(fibonacci[1:]), run_time=2)
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
        self.wait(4)
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
        
                self.play(ShowCreation(circle_1), ShowCreation(circle_2), 
                            ShowCreation(circle_3), ShowCreation(arc_1), 
                            ShowCreation(arc_2), ShowCreation(arc_3),
                            ReplacementTransform(fibonacci_term, text))
                self.wait()
                
            else:
                self.play(ReplacementTransform(aux_circ_1, circle_1), ReplacementTransform(aux_circ_2, circle_2),
                            ReplacementTransform(aux_circ_3, circle_3), ReplacementTransform(aux_arc_1, arc_1), 
                            ReplacementTransform(aux_arc_2, arc_2), ReplacementTransform(aux_arc_3, arc_3),
                            ReplacementTransform(fibonacci_term, text))
                self.wait()

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
        self.play(FadeOutAndShift(text_2, 6*DOWN))
        self.wait(3)
  
                
class IntroductionToSeriesPart2(Scene):
    def construct(self):
        n_term = TexMobject("\\{\\frac{n}{n+1}\\}_{n=1}^{\\infty}").scale(2)
        n_term.set_color_by_gradient(BLUE_D, PURPLE_D)
        n = TexMobject("n = ", "\\, ").scale(1.5)
        n.center()
        n.set_color_by_gradient(PURPLE, BLUE)


        self.play(Write(n_term), run_time=2)
        self.wait(4)
        self.play(ApplyMethod(n_term.shift, 2.5*UP), run_time=2)
        self.wait(5)

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
            new_n.set_color(BLUE)
            if k == 0:
                self.play(Transform(n[1], new_n))
                self.play(ShowCreation(frac[1]))
            else:  
                self.play(Transform(n[1], new_n)) 
                self.play(ReplacementTransform(n_term.copy(), frac[k+1:k+2]))
                self.wait(1)

        self.play(Write(frac[-1]), run_time=2)
        self.wait(6)

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
            brace_1.set_color_by_gradient(PURPLE, BLUE)
            
            
            a = float(num_list[i+1])/float(div_list[i+1])
            b = float(num_list[i+2])/float(div_list[i+2])
            c = b -a

            sub = TexMobject(*[str("{0:.3f}".format(b)), "-", str("{0:.3f}".format(a)), "=", str("{0:.3f}".format(c))]).scale(1.4)
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
        plane = NumberPlane()
        line = NumberLine(number_scale_val = 0.6, unity_size=6 , tick_size= 0.2, numbers_with_elongated_ticks = [0, 1], longer_tick_multipler = 3, color=BLUE)
        unit_line = UnitInterval(color= BLUE_C)

        # Create ticks in line and two ticks in unit line
        for i in np.arange(-10, 10, 1):
            line.add_numbers(i)
            if i == 0 or i ==1:
                unit_line.add_numbers(i)
        
        # Two groups of points. 
        dot_group = VGroup()
        dot_group_2 = VGroup()
        for i in range(18):
            val = 1.0*(i+1)/(i+2)
            dot_group.add(Dot(np.array([val, 0, 0]), color=RED_A))
            dot_group_2.add(Dot(unit_line.number_to_point(val), color=RED_A))

        # Create a line in screen
        self.play(ShowCreation(line), run_time=2)

        # Create a n count in latex
        n_term = TexMobject("n = ", "\\, ").scale(2)
        n_term.move_to(3*UP)
        n_term.set_color_by_gradient(PURPLE, BLUE)
        self.play(ShowCreation(n_term))

        # Place in the dots in the long line
        for i,dot in enumerate(dot_group):
            n_number = TexMobject(str("{0:.4f}".format(1*(i+1)/(i+2)))).set_color(BLUE).scale(2)
            n_number.next_to(n_term[0])
            self.play(Transform(n_term[1], n_number), ShowCreation(dot))
            #self.play()
        self.wait(4)

        # Uncreate everythig but n 
        self.play(Uncreate(line), Uncreate(dot_group), FadeOut(n_term[1]))
        self.wait(4)
        self.play(ShowCreation(unit_line))
        self.wait(4)
        
        # Place the dots in the short line
        for i,dot in enumerate(dot_group_2):
            n_number = TexMobject(str("{0:.4f}".format(1*(i+1)/(i+2)))).set_color(BLUE).scale(2)
            n_number.next_to(n_term[0])
            self.play(Transform(n_term[1], n_number), ShowCreation(dot))
            #self.play()
        self.wait(4)
        
        # Uncreate everything
        self.play(Uncreate(dot_group_2), Uncreate(unit_line), run_time=3)
        self.play(FadeOutAndShift(n_term, 5*DOWN))
        self.wait(4)

        # Show Fraction
        frac = TexMobject("\\frac{n}{n+1}").scale(2)
        frac.set_color_by_gradient(BLUE, PURPLE)
        self.play(ShowCreation(frac))
        self.wait(5)
        for i in [100, 500, 1000, 10000, 100000]:
            if i==100000:
                new_frac = TexMobject("\\frac{"+str(i)+"}{"+str(i)+"+1}"+ "=" "\\frac{"+str(i)+"}{"+str(i+1)+"}"+"="+"0.99999").scale(1.5)
            else:    
                new_frac = TexMobject("\\frac{"+str(i)+"}{"+str(i)+"+1}"+ "=" "\\frac{"+str(i)+"}{"+str(i+1)+"}"+"="+str("{0:.4f}".format(1.*(i)/(i+1)))).scale(1.5)
            new_frac.set_color_by_gradient(BLUE, PURPLE)
            self.play(Transform(frac, new_frac), run_time=3)
            self.wait(2)
            
        new_frac = TexMobject("\\lim_{n \\to \\infty} \\frac{n}{n + 1} = 1").scale(1.5)
        new_frac.set_color_by_gradient(BLUE, PURPLE)
        self.play(ReplacementTransform(frac, new_frac), run_time=3)
        self.wait(4)
        frac = TexMobject("\\frac{n}{n+1}").scale(2).set_color_by_gradient(PURPLE, BLUE)
        frac_1 = TexMobject("\\frac{x}{x+1}").scale(2).set_color_by_gradient(PURPLE, BLUE)
        self.play(ReplacementTransform(new_frac, frac), run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(frac, frac_1 ), run_time=2)
        self.wait(3)
        self.play(Uncreate(frac_1), run_time=2)
        self.wait(4)


class IntroductionToSeriesPart4(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : 0,
        "x_max" : 20,
        "x_min" : 0,
        "y_tick_frequency" : 0.5, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "x_axis_label": None,
        "y_axis_label": None,
        "y_label_decimal":3,
        "graph_origin" : 3*DOWN+5*LEFT,
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph_1 = self.get_graph(self.func_to_graph,color = RED, x_min=0, x_max=20)
        label_1 = self.get_graph_label(graph_1, direction = 1.5*DOWN+RIGHT, label = "y = \\frac{x}{x+1}")
        label_11 = self.get_graph_label(graph_1, direction = 1.5*DOWN+RIGHT, label = "y = \\frac{n}{n+1}")
        graph_2 = self.get_graph(lambda x: 1,x_min =0, x_max=20, color=YELLOW)
        label_2 = self.get_graph_label(graph_2, direction = 1.5*UP+RIGHT, label = "y=1")

        lines = self.create_lines_between_two_graphs(graph_2, graph_1, n=20)

        x_axis_label = TexMobject("x").set_color(BLUE)
        x_axis_label.next_to(self.x_axis, RIGHT+UP)
        y_axis_label = TexMobject("y(x)").set_color(BLUE)
        y_axis_label.next_to(self.y_axis, UP)

        
        x_axis_label_2 = TexMobject("n").set_color(PURPLE)
        x_axis_label_2.next_to(self.x_axis, RIGHT+UP)
        y_axis_label_2 = TexMobject("y[n]").set_color(PURPLE)
        y_axis_label_2.next_to(self.y_axis, UP)

        #dot1 = Dot(self.coords_to_point(0,1), color=PURPLE, radius=0.05)
        dots = self.get_points_from_graphic(self.func_to_graph, 20, xmin=0, xmax=20, dot_color=RED, point_radius=0.07)
        dots_2 = self.get_points_from_graphic(lambda x: 1, 20, xmin=0, xmax=20, dot_color=YELLOW, point_radius=0.07)
        self.play(ShowCreation(x_axis_label), ShowCreation(y_axis_label))
        self.wait(3)
        self.play(ShowCreation(graph_2), run_time=3)
        self.play(Write(label_2))
        
        self.play(ShowCreation(graph_1), run_time=3)
        self.play(Write(label_1))
        self.wait(4)
        
        self.play(Transform(x_axis_label, x_axis_label_2), Transform(y_axis_label, y_axis_label_2))
        self.play(Transform(graph_1, dots), Transform(label_1, label_11), run_time=2)
        self.wait(4)
        self.play(ShowCreation(lines), run_time=3)
        self.wait(2)
        self.play(Transform(graph_2, dots_2))
        self.wait(3)
        self.play(Uncreate(label_1), Uncreate(label_2), run_time=3)
        self.wait(2)
        self.play(Uncreate(graph_1), Uncreate(graph_2), run_time=3)
        self.play(Uncreate(lines), run_time=2)
        self.play(Uncreate(self.x_axis), Uncreate(self.y_axis), Uncreate(x_axis_label), Uncreate(y_axis_label), run_time=2)
        self.wait(3)
 
    def create_lines_between_two_graphs(self, first_graph, second_graph, xmin=0, xmax=20, n = 20, line_color= GREEN):
        vert_lines_1 = self.get_vertical_lines_to_graph(first_graph, num_lines = n, x_min=xmin, x_max=xmax, color= line_color)
        vert_lines_2 = self.get_vertical_lines_to_graph(second_graph, num_lines = n, color= line_color)
        line_group = VGroup()
        for line1, line2 in zip(vert_lines_1, vert_lines_2):
            top = line1.get_top()
            bottom = line2.get_top()
            line = Line(start=bottom, end=top, color = line_color)
            line_group.add(line) 

        return line_group

    def func_to_graph(self, x):
        return x/(x+1)

    def get_points_from_graphic(self, graphic, number_of_lines, point_radius=0.04, xmin=-10, xmax=10, dot_color=BLUE):
        graph = self.get_graph(graphic, color=PURPLE, x_min=xmin,x_max=xmax)
        vert_lines = self.get_vertical_lines_to_graph(graph, x_min=xmin, x_max=xmax, num_lines=number_of_lines)
        point_list = list(vert_lines.get_all_points())
        dots_group = VGroup()
        n = 0

        for i, coords in enumerate(point_list):
            if n == 3:
                dots_group.add(Dot(coords, radius=point_radius, color=dot_color))
                n = 0
            else:
                n+=1

        return dots_group


class IntroductionToSeriesPart5(Scene):

    def construct(self):
        # Texts.
        text_1 = TextMobject("Séries")  # Intro text.
        text_1.scale(3)                 # Scale Intro Text.
        text_1.set_color_by_gradient(RED_C, PURPLE_B) # Set color of intro Text.

        # Pi number.
        # Create a TexMobject that contains the value of pi in string format.
        pi_text = TexMobject("\\pi", "=", str(PI),"...") # create a mobject.
        pi_text.set_color_by_gradient(RED, PURPLE) # set colot by a gradient from red to purple.

        # Pi number in decimal form.
        pi_dec = decimal.Decimal(format(PI, '.10f')) # create a decimal value with 10 decimals numbers
        pi_tuple = pi_dec.as_tuple()[1] # get the right element of a tuple that contais the pi number.

        pi_list = [] # create a auxiliar list to use in the down for loop.
        terms_of_pi_list = [] # create a group terms of pi

        # create a list of pi numer in fraction format.
        for i in range(10): # chosse only 10 terms.
            if i ==0:
                pi_list.append("\\frac{"+str(pi_tuple[i])+"}{10^{"+str(i)+"}} +") # append in auxiliar list each fraction terms of pi
                terms_of_pi_list.append(str(pi_tuple[i])+".")
            else:
                pi_list.append("\\frac{"+str(pi_tuple[i])+"}{10^{"+str(i)+"}} +") # append in auxiliar list each fraction terms of pi
                terms_of_pi_list.append(str(pi_tuple[i]))

        pi_list.append("...") # after for loop add ... at the end.
        pi_sum = TexMobject(*pi_list).scale(0.8) # transform all list into TexMobject. 
        pi_sum.next_to(pi_text[1], RIGHT) # put the sum pi in the right place. In this case on the right of equal signal.
        pi_sum.set_color_by_gradient(RED, PURPLE) # set color by gradient from red to purple.
        
        # Each terms of pi
        terms_of_pi_list.append("...")
        terms_of_pi = TexMobject(*terms_of_pi_list).scale(2)
        terms_of_pi.next_to(pi_text, 7*DOWN)
        terms_of_pi.set_color_by_gradient(YELLOW, RED)

        # generate all Braces
        braces_group = VGroup() # crate a brace group.
    
        # Animation
        self.play(FadeInFrom(text_1, 4*DOWN), run_time=2) # Show series text
        self.wait(2)
        self.play(FadeOutAndShift(text_1, 5*UP))
        self.wait()
        self.play(Write(pi_text[:])) # Write 
        self.wait(6)

        # transform pi_text into pi_sum wich is the fraction sum and remove the ...
        pi_group_aux = VGroup(pi_text[:2], pi_sum)
        #self.play(Transform(pi_text[2], pi_sum), FadeOut(pi_text[3]))
        self.play(Transform(pi_text, pi_group_aux))
        self.play(ApplyMethod(pi_text.shift, 3.5*LEFT), ApplyMethod(pi_sum.shift,3.5*LEFT))
        self.wait(2)
        self.play(FadeIn(terms_of_pi))
        self.wait(3)

        for i,term in enumerate(pi_sum):
            if i == len(pi_sum)-1:
                break
            # Create a brace above each term of pi_sum.
            brace = Brace(pi_sum[i], UP, buff = SMALL_BUFF)
            brace.set_color_by_gradient(RED, PURPLE) # set color by gradient

            a = float(pi_tuple[i]/(10**i)) # transform string into float
            b = "{0:."+str(i)+"f}" # auxiliar to format the a variable
            title = brace.get_text("$"+b.format(a)+"$").set_color_by_gradient(YELLOW, RED) # Set a title for each brace
            
            circle = Circle(color=BLUE)
            circle.surround(terms_of_pi[i])

            if i ==0:
                self.play(GrowFromCenter(brace), FadeIn(title), ShowCreation(circle))
                self.wait()
            else:
                self.play(ReplacementTransform(brace_1, brace), ReplacementTransform(title_1, title), ReplacementTransform(aux_circle, circle))
                self.wait()
            
            brace_1 = brace
            title_1 = title
            aux_circle = circle
        
        self.wait(4)
        self.play(Uncreate(circle), Uncreate(title), Uncreate(brace), run_time=2)
        self.wait()
        self.play(FadeOutAndShift(terms_of_pi, 3*DOWN),run_time=2)
        self.play(FadeOut(pi_group_aux, 3*UP))
        self.play(FadeOut(pi_text))
        self.wait(3)

        # ----- Second part -------
        text_sequence_and_sum = [TexMobject("\\{a_n\\}_{n=1}^\\infty").set_color_by_gradient(BLUE, PURPLE).scale(3),
                                TexMobject("a_1 + a_2 + a_3 + ... + a_n + ...").set_color_by_gradient(RED, PURPLE).scale(1.7)]

        sum_definition = [TexMobject("\\sum_{n=1}^{\\infty} a_n").set_color_by_gradient(RED, YELLOW).scale(3),
                        TexMobject("\\sum a_n").set_color_by_gradient(RED, YELLOW).scale(3)]

        infinity_sum = TexMobject("1 + 2 + 3 + 4 + 5 + ... + n +...").set_color(RED).scale(1.6)

        self.play(Write(text_sequence_and_sum[0]), run_time=3)
        self.wait(4)
        self.play(ReplacementTransform(text_sequence_and_sum[0], text_sequence_and_sum[1]), run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_sequence_and_sum[1], sum_definition[0]))
        self.wait(2)
        self.play(ReplacementTransform(sum_definition[0], sum_definition[1], run_time=2))
        self.wait(3)
        self.play(Uncreate(sum_definition[1]))
        self.wait(5)
        self.play(ShowCreation(infinity_sum), run_time=3)
        self.wait(8)
        self.play(Uncreate(infinity_sum), run_time=1)

        # Final scene is the same as initial
        text_1.scale(2)
        self.play(FadeIn(text_1), run_time=3)
        self.play(FadeOut(text_1), run_time=5)