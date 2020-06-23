from manimlib.imports import *

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
        graph_label = self.get_graph_label(graph_1, direction=UP+RIGHT)
        
        number_of_n = []
        color_list = [BLUE_D, PINK, PURPLE,  GREEN, YELLOW, ORANGE, RED_C]
        dots_for_each_graph = []
        for i,j in enumerate([20, 50, 100, 150, 200, 500, 1000]):
            dots_for_each_graph.append(self.get_points_from_graphic(self.func_1, j, point_radius=0.05, dot_color=color_list[i]))
            number_of_n.append(TextMobject("N = "+str(j)))

        text_1.move_to(3.5*UP)
        self.add(text_1)
        self.play(ShowCreation(graph_1), Write(graph_label))
        self.wait(2)

        for k in range(len(dots_for_each_graph)-1):
            if k==0:
                number_of_n[k].set_color(color=color_list[k])
                number_of_n[k].move_to(3*UP+3*RIGHT)
                self.play(FadeIn(number_of_n[k]))
                self.play(FadeIn(dots_for_each_graph[k]))

            self.wait()
            self.play(FadeOut(graph_1))
            self.wait(2)
            self.play(FadeIn(graph_1))
            self.wait()
            number_of_n[k+1].set_color(color=color_list[k+1])
            number_of_n[k+1].move_to(3*UP+3*RIGHT)
            self.play(ReplacementTransform(dots_for_each_graph[k], dots_for_each_graph[k+1]),
                    ReplacementTransform(number_of_n[k], number_of_n[k+1]),
                    ApplyMethod(number_of_n[k].remove))
            
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

    def func_1(self, x):
        return np.cos(x)