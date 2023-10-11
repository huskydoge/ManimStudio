from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class SyntaxMatrix(VoiceoverScene):
    icon = SVGMobject('favicon').scale(0.5)

    def opening_animation(self):
        # opening animation
        self.add_sound("media/audio/mixkit-air-woosh-1489.wav", time_offset=1)
        self.play(FadeIn(self.icon))
        self.play(self.icon.animate.shift(1.5 * UP))
        self.wait(0.5)
        course = Tex("Husky  ","Course Time")
        course[1].set_color(BLUE)
        self.play(Write(course[0], run_time=.7), Write(course[1], run_time=.7))
        self.add_sound("media/audio/mixkit-dog-barking-twice-1.wav", gain=1)
        self.wait(0.5)
        u = Underline(course[1], color=WHITE)  # underline
        self.play(Create(u, run_time=.7))
        self.wait(0.5)
        self.play(FadeOut(self.icon, *course,u))
        self.wait(0.5)

    def chapter(self):
        # ###  Chapter 1
        chapt = Text("Chapter 1")
        name = Text("Syntax Analysis: Basics", gradient=(RED, BLUE, GREEN))
        with self.voiceover(text="Welcome to Husky's Channel! Today, let's talk about basic concept about Syntax Analysis"):
            self.play(Write(chapt))
            self.wait(0.3)
            self.play(chapt.animate.shift(3 * LEFT))
            name.next_to(chapt, RIGHT, buff=.5)
            self.play(Write(name, run_time=.6))
            self.wait(.3)
        self.play(FadeOut(chapt, name))

    def part1_lexical(self):

        # part 1
        with self.voiceover(text="Firstly, let's get familar with Lexical Analysis."):

            t = Text("Part 1: Lexical Analysis", gradient=(RED, BLUE, GREEN), font_size=140,
                     disable_ligatures=True).scale(0.2)
            t.to_edge(LEFT + UP, buff=.5)
            self.icon.to_edge(RIGHT + UP, buff=0.5)
            self.play(Create(t), Rotate(self.icon, 2 * PI))

        with self.voiceover(text="There are two symbol strings:"):

            e1 = MathTex("1", "+", "x", "*", "y")
            e2 = MathTex("(", "1", "+", "x", ")", "*", "y")
            #
            lsts = VGroup(e1, e2).arrange(RIGHT, buff=1)
            self.play(Create(lsts))

        with self.voiceover(text="What Lexical Analysis does is to tokenize the string as demonstrated here"):

            self.play(lsts[0].animate.shift(LEFT, UP), lsts[1].animate.shift(RIGHT, UP))

            self.wait(.5)
            lstsContent1 = ["NAT(1)", "PLUS", "IDENT(x)", "MUL", "IDENT(y)"]
            lstsContent2 = ["LEFT_PAREN", "NAT(1)", "PLUS", "IDENT(x)", "RIGHT_PAREN", "MUL",
                            "IDENT(y)"]

        ## lexer animation
        tokenGrp1 = []
        tokenGrp2 = []

        for i in range(len(lsts[0])):
            framebox1 = SurroundingRectangle(lsts[0][i], buff=.1)
            self.play(Create(framebox1, run_time=0.2))
            text = Text(lstsContent1[i])
            # self.play(ReplacementTransform(framebox1, text))
            # self.wait(.2)

            if i == 0:
                tokenGrp1.append(text.copy().scale(.3))
                tokenGrp1[-1].shift(3.5 * LEFT, 1 * DOWN)
            elif i < 3:
                tokenGrp1.append(text.copy().scale(.3).next_to(tokenGrp1[-1], RIGHT))
            elif i == 3:
                tokenGrp1.append(text.copy().scale(.3).next_to(tokenGrp1[0], 2 * DOWN))
            else:
                tokenGrp1.append(text.copy().scale(.3).next_to(tokenGrp1[-1], RIGHT))

            text_ = ""
            if i == 0:
                text_ = "The first symbol is one, which is tokenized as a natural number"
            elif i == 1:
                text_ = "The second symbol is tokenized as a plus sign"
            elif i == 2:
                text_ = "Then followed by Ident x."
            elif i == 3:
                text_ = "Then times sign"
            else:
                text_ = "and finally ends with another ident y"
            with self.voiceover(text=text_):
                self.play(ReplacementTransform(framebox1, tokenGrp1[-1]))
            self.wait(.1)

        with self.voiceover("Similarly, here is another example. Let's quickly go through it"):
            self.play(Circumscribe(e2))
        for i in range(len(lsts[1])):
            framebox2 = SurroundingRectangle(lsts[1][i], buff=.1)
            self.play(Create(framebox2, run_time=0.1))
            # self.wait(.2)
            text = Text(lstsContent2[i])
            # self.wait(.2)

            if i == 0:
                tokenGrp2.append(text.copy().scale(.3))
                tokenGrp2[-1].shift(RIGHT * 2, 1 * DOWN)
            elif i < 3:
                tokenGrp2.append(text.copy().scale(.3).next_to(tokenGrp2[-1], RIGHT))
            elif i == 3:
                tokenGrp2.append(text.copy().scale(.3).next_to(tokenGrp2[0], 2 * DOWN + LEFT))
            else:
                tokenGrp2.append(text.copy().scale(.3).next_to(tokenGrp2[-1], RIGHT))

            self.play(ReplacementTransform(framebox2, tokenGrp2[-1]))

        self.play(FadeOut(t, e1, e2, *tokenGrp1, *tokenGrp2, self.icon))

    def part2_syntax(self):
        ## Syntax
        title = Text("Part 2: Context-free Syntax ", gradient=(RED, BLUE, GREEN), font_size=140,
                     disable_ligatures=True).scale(0.2)
        title.to_edge(LEFT + UP, buff=0.5)
        self.icon.to_edge(RIGHT + UP, buff=0.5)
        with self.voiceover(text="Now, let's move to contex-free Syntax"):
            self.play(Create(title), Rotate(self.icon, 2 * PI))

        # Syntax table
        t = Table([
            ["S -> S ; S", "S -> ID := E", "S -> PRINT ( L )"],
            ["E -> ID", "E -> NAT", "E -> E + E"],
            ["E -> ( E )", "L -> E", "L -> L , E"]
        ], line_config={"stroke_color": BLUE, "stroke_width": 1}).scale(.5)

        with self.voiceover(text="Here is a Syntax rule table. The symbols in the table corresponds to the tokens we got from the previous step."):
            self.play(
                t.create()
            )

        tracker = self.add_voiceover_text(
            "A set of contex-free Syntax contains these aspects:"
        )

        self.wait(tracker.get_remaining_duration(buff=.1))

        with self.voiceover(text="An initial symbol, which is S in this case"):
            l = [t.get_entries((1, 1)), t.get_entries((1, 2)), t.get_entries((1, 3))]

            self.play(Circumscribe(l[0][0][0]), Circumscribe(l[0][0][3]), Circumscribe(l[0][0][5]),
                      Circumscribe(l[1][0][0]),
                      Circumscribe(l[2][0][0]))
            initial = Tex(r"Initial Symbol $S$", font_size=25, color=WHITE).next_to(t, 0.5 * LEFT + UP)
            self.play(Write(initial))

        with self.voiceover(text="A set of terminal symbols."):
            l = [t.get_entries((1, 2)), t.get_entries((1, 3)), t.get_entries((2, 1)), t.get_entries((2, 2)),
                 t.get_entries((2, 3)), t.get_entries((3, 1)), t.get_entries((3, 3)), t.get_entries((1, 1))]
            self.play(Indicate(l[0][0][3:5]), Indicate(l[0][0][4:7]), Indicate(l[1][0][3:8]), Indicate(l[1][0][8]),
                      Indicate(l[2][0][3:]), Indicate(l[3][0][3:]), Indicate(l[4][0][4]),
                      Indicate(l[5][0][3]), Indicate(l[5][0][5]), Indicate(l[6][0][-2]), Indicate(l[7][0][4]))
            terminal = Tex(r"Terminal Symbols", font_size=25, color=WHITE).next_to(t, 2 * RIGHT)
            terminal_set = Tex(r" $ID \ \ NAT \ \ , \ \ ; \ \ ( \ \ ) \ \ + \ \ :=$", font_size=20,
                               color=WHITE).next_to(terminal,
                                                    DOWN)
            self.play(Write(terminal, run_time=0.1), Write(terminal_set))
        with self.voiceover(text="A set of non-terminal symbols."):
            l = [t.get_entries((1, 1)), t.get_entries((1, 2)), t.get_entries((1, 3)),
                 t.get_entries((2, 1)), t.get_entries((2, 2)), t.get_entries((2, 3)),
                 t.get_entries((3, 1)), t.get_entries((3, 2)), t.get_entries((3, 3))]
            self.play(Indicate(l[0][0][0]), Indicate(l[0][0][-1]), Indicate(l[1][0][0]), Indicate(l[1][0][-1]),
                      Indicate(l[2][0][0]), Indicate(l[2][0][-2]), Indicate(l[3][0][0]),
                      Indicate(l[4][0][0]), Indicate(l[5][0][0]), Indicate(l[5][0][3]),
                      Indicate(l[5][0][5]), Indicate(l[6][0][0]), Indicate(l[6][0][-2]),
                      Indicate(l[7][0][0]), Indicate(l[7][0][-1]), Indicate(l[8][0][0])
                      , Indicate(l[8][0][5]))

            nonterminal = Tex(r"Non-terminal Symbols", font_size=25, color=WHITE).next_to(t, 0.5 * LEFT + DOWN)
            nonterminal_set = Tex(r"$S \ E \ L$", font_size=20, color=WHITE).next_to(nonterminal, DOWN)
            self.play(Write(nonterminal, run_time=0.4), Write(nonterminal_set))

        with self.voiceover(text="And all the expression in the tables are called production."):
            self.play(Circumscribe(t))
            production_text = Tex("Productions", color=BLUE).to_edge(DOWN, buff=0.5)
            self.play(FadeIn(production_text))

        production = Tex(r'Left Side', r'$->$', r'Right Side').arrange(buff=1)
        with self.voiceover(text="The left side of each production is a non-terminal,"):
            self.play(ReplacementTransform(production_text, production[0].to_edge(DOWN, buff=1).set_color(RED)))
            arrow_1 = Arrow(nonterminal_set.get_bottom(), production[0].get_left(), stroke_width=1, tip_length=0.1,
                            buff=0.3)
            self.play(Create(arrow_1))

        self.wait(0.2)
        self.play(Write(production[1].to_edge(DOWN, buff=1)))

        with self.voiceover(
                text="and the right side of each production is a list of terminators or non-terminators, which could be empty"):
            self.play(Write(production[2].to_edge(DOWN, buff=0.9).set_color(BLUE)))
            arrow_2 = Arrow(nonterminal_set.get_bottom(), production[2].get_top() + 0.1 * UP, buff=0.5, stroke_width=1,
                            tip_length=0.1)
            arrow_3 = Arrow(terminal_set.get_left(), production[2].get_top(), stroke_width=1, tip_length=0.1)
            self.play(Create(arrow_2), Create(arrow_3))
        t.line_config = {"stroke_color": BLUE, "stroke_width": 1}
        self.play(t.animate.shift(UP * 2).scale(0.8),
                  FadeOut(terminal_set, terminal, nonterminal_set, nonterminal, *production, arrow_3, arrow_2, arrow_1,
                          initial))

        ######################## derivation
        with self.voiceover(text="then, let's introduce the concept of derivation."):
            derivation = Tex("Derivation", color=BLUE)
            self.play(Write(derivation))

        with self.voiceover(
                text="The process of expanding the initial symbol, according to the production, to obtain a sequence of terminals is called derivation."):
            self.play(Circumscribe(t))
            self.play(ApplyWave(derivation, run_time=1.5,amplitude=1))
            definition = Tex(r"Initial Symbol $\stackrel{production}{\longrightarrow}$ Sequence of Terminals ",font_size=20)
            definition.next_to(derivation,2 * DOWN)
            self.play(Write(definition))
            self.wait(1)

        text1 = Tex("S", r' $\Rightarrow$ ', "S", " ; ", "S", font_size=28).shift(1.5 * UP + RIGHT * 2)
        with self.voiceover("For example, let's start with the initial symbol S."):
            self.play(t.animate.shift(LEFT * 3 + 2 * DOWN), ReplacementTransform(derivation, text1[0]),FadeOut(definition))
        with self.voiceover("According to the production table, we can derive S to S semicol S."):
            self.play(Circumscribe(t.get_entries((1, 1))))
            self.play(Write(text1[1]))
            self.play(Write(text1[2:]))

        with self.voiceover("we then derive S to 'ID be defined as E',"):
            text2 = Tex(r' $\Rightarrow$ ', "ID := ", "E", " ; ", "S", font_size=28)

            text2_group = VGroup(text2[0], text2[1], text2[2], text2[3], text2[4])
            text2_group.next_to(text1[1], DOWN, aligned_edge=LEFT)
            t_ = text1[2].copy()
            self.play(Write(text2[0]))
            self.play(Circumscribe(t.get_entries((1, 2))))
            replace_grp = VGroup(text2[1], text2[2])
            self.play(ReplacementTransform(t_, replace_grp))
            self.play(Write(text2[3:]))

        with self.voiceover("Then E to E plus E"):
            text3 = Tex(r' $\Rightarrow$ ', "ID := ", "E ", "+", " E", " ; ", "S", font_size=28)
            text3_group = VGroup(text3[0], text3[1], text3[2], text3[3], text3[4], text3[5], text3[6])
            text3_group.next_to(text2[0], DOWN, aligned_edge=LEFT)
            t_ = text2[2].copy()
            self.play(Write(text3[0]))
            replace_grp = VGroup(*text3[2:5])
            self.play(Write(*text3[1:2]))
            self.play(Circumscribe(t.get_entries((2, 3))))
            self.play(ReplacementTransform(t_, replace_grp))
            self.play(Write(text3[5:]))

        with self.voiceover("Then E to ID"):
            text4 = Tex(r' $\Rightarrow$ ', "ID := ", "ID ", "+", " E", " ; ", "S", font_size=28)
            text4_group = VGroup(text4[0], text4[1], text4[2], text4[3], text4[4], text4[5], text4[6])
            text4_group.next_to(text3[0], DOWN, aligned_edge=LEFT)
            t_ = text3[2].copy()
            self.play(Write(text4[0:2]))
            replace_grp = VGroup(*text4[2])
            # self.play(Write(*text4[1:2]))
            self.play(Circumscribe(t.get_entries((2, 1))))
            self.play(ReplacementTransform(t_, replace_grp))
            self.play(Write(text4[3:]))

        with self.voiceover(
                "By continuously applying production rules till no operation available, we can get the final derivation"):
            text5 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; S", font_size=28)
            text5.next_to(text4[0], DOWN, aligned_edge=LEFT)
            text6 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; PRINT(L)", font_size=28)
            text6.next_to(text5[0], DOWN, aligned_edge=LEFT)
            text7 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; PRINT(L, E)", font_size=28)
            text7.next_to(text6[0], DOWN, aligned_edge=LEFT)
            text8 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; PRINT(E, E)", font_size=28)
            text8.next_to(text7[0], DOWN, aligned_edge=LEFT)
            text9 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; PRINT(ID, E)", font_size=28)
            text9.next_to(text8[0], DOWN, aligned_edge=LEFT)
            text10 = Tex(r' $\Rightarrow$ ', "ID := ID + NAT; PRINT(ID, ID)", font_size=28)
            text10.next_to(text9[0], DOWN, aligned_edge=LEFT)

            self.play(Write(text5[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((2, 2))), run_time=0.4)
            self.play(Write(text5[1:]), run_time=0.4)

            self.play(Write(text6[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((1, 3))), run_time=0.4)
            self.play(Write(text6[1:]), run_time=0.4)

            self.play(Write(text7[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((3, 3))), run_time=0.4)
            self.play(Write(text7[1:]), run_time=0.4)

            self.play(Write(text8[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((3, 2))), run_time=0.4)
            self.play(Write(text8[1:]), run_time=0.4)

            self.play(Write(text9[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((2, 1))), run_time=0.4)
            self.play(Write(text9[1:]), run_time=0.4)

            self.play(Write(text10[0]), run_time=0.4)
            self.play(Circumscribe(t.get_entries((2, 1))), run_time=0.4)
            self.play(Write(text10[1:]), run_time=0.4)

            self.wait(0.5)
            self.play(FadeOut(t, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, run_time=2))
            self.wait(0.8)

            ######################## parsing tree
            with self.voiceover("Now, after getting familiar with derivation, let's move to parsing tree."):
                parsing_tree = Tex("Parsing Tree", color=BLUE)
                self.play(Write(parsing_tree))
                self.wait(1)
            with self.voiceover(
                    "By following the process of derivation step by step, we can get its corresponding parsing tree."):
                rule = Tex(
                    r"E $\rightarrow$ ID  \quad  E $\rightarrow$ E + E \quad   E $\rightarrow$ E * E \quad   E $\rightarrow$ ( E )",
                    font_size=32, color=GREEN).to_edge(UP, buff=1.5)
                tree1 = Tex('E', font_size=30)  # 0
                d1 = Tex('E', font_size=30)
                parsing_tree_ = parsing_tree.copy().scale(0.8)
                derivation_ = Tex("Derivation",color=BLUE).scale(0.8)
                self.play(ReplacementTransform(parsing_tree, rule))
                tree1.shift(LEFT * 2.6 + 0.5 * UP),
                d1.shift(RIGHT * 2.4 + 0.5 * UP)
                parsing_tree_.next_to(tree1, UP)
                derivation_.next_to(d1, UP, buff=0.3)
                self.play(Create(parsing_tree_), Create(derivation_))
                self.play(Write(tree1[0]), Write(d1[0]))

                self.wait(1)
                d2 = Tex(r"$\Rightarrow$ E * E", font_size=30).next_to(d1, DOWN, aligned_edge=LEFT)
                d3 = Tex(r"$\Rightarrow$ E + E * E", font_size=30).next_to(d2, DOWN, aligned_edge=LEFT)
                d4 = Tex(r"$\Rightarrow$ ID + E * E", font_size=30).next_to(d3, DOWN, aligned_edge=LEFT)
                d5 = Tex(r"$\Rightarrow$ ID + ID * E", font_size=30).next_to(d4, DOWN, aligned_edge=LEFT)
                d6 = Tex(r"$\Rightarrow$ ID + ID * ID", font_size=30).next_to(d5, DOWN, aligned_edge=LEFT)

                d = VGroup(d1, d2, d3, d4, d5, d6)

                tree2 = Text(" / | \ ", font_size=30).next_to(tree1, DOWN)  # 1
                tree3 = Tex(r'E \quad', ' * ', r'\quad E', font_size=30).next_to(tree2, DOWN)  # 2
                tree4_1 = Text(" / | \ ", font_size=30).next_to(tree3[0], DOWN)  # 3
                tree4_2 = Text("|", font_size=30).next_to(tree3[-1], DOWN)  # 4
                tree5_1 = Tex("E", " + ", "E", font_size=30).next_to(tree4_1, DOWN)  # 5
                tree5_2 = Tex("ID", font_size=30).next_to(tree4_2, DOWN)  # 6
                tree6_1 = Text(" | ", font_size=30).next_to(tree5_1[0], DOWN)  # 7
                tree6_2 = Text(" | ", font_size=30).next_to(tree5_1[2], DOWN)  # 8
                tree7_1 = Tex("ID", font_size=30).next_to(tree6_1, DOWN)  # 9
                tree7_2 = Tex("ID", font_size=30).next_to(tree6_2, DOWN)  # 10

                tree = VGroup(tree1, tree2, tree3, tree4_1, tree4_2, tree5_1, tree5_2, tree6_1, tree6_2, tree7_1,
                              tree7_2)

                internal = VGroup(tree3, tree4_1, tree5_1)
                leafs = VGroup(tree5_2, tree7_1, tree7_2)

                self.play(Write(tree[1]), Write(tree[2]), Write(d[1]))  # line 2
                self.play(Write(tree[3]), Write(tree[5]), Write(d[2]))  # line 3
                self.play(Write(tree[7]), Write(tree[9]), Write(d[3]))  # line 4
                self.play(Write(tree[8]), Write(tree[10]), Write(d[4]))  # line 5
                self.play(Write(tree[4]), Write(tree[6]), Write(d[5]))  # line 6

            tracker = self.add_voiceover_text("Parsing Tree has following properties")
            self.wait(tracker.get_remaining_duration(buff=0.05))
            with self.voiceover("First, The root node is the initial symbol of the context-free syntax"):
                arrow1 = Arrow(tree[0].get_right(), tree[0].get_right() + RIGHT)
                initial = Tex("1. Root : Initial Symbol", font_size=30).next_to(arrow1, RIGHT)
                self.play(Create(arrow1), Circumscribe(tree[0]))
                self.play(Write(initial))
            self.wait(0.5)
            with self.voiceover("Second, Each internal node is a non-terminal symbol"):
                arrow2 = Arrow(internal[1].get_left(), internal[1].get_left() + LEFT)
                self.play(Indicate(internal), Create(arrow2))
                nonterminal = Tex(r"2. Internal Node : ", "Non-Terminals", font_size=25).arrange(DOWN).next_to(arrow2,
                                                                                                               LEFT).next_to(
                    arrow2.get_end(), LEFT)
                self.play(Write(nonterminal))
            self.wait(0.5)
            with self.voiceover("Third, each leaf node is a terminal symbol"):
                arrow3 = Arrow(leafs[-1].get_right(), leafs[-1].get_right() + 0.5 * RIGHT + DOWN)
                self.play(Indicate(leafs), Create(arrow3))
                terminal = Tex("3. Leaf Node : Terminals", font_size=30).next_to(arrow3.get_end(), RIGHT)
                self.play(Write(terminal))
            self.wait(0.5)
            with self.voiceover("Lastly, Each parent node and its children form a production in a context-free syntax"):
                pgrp = VGroup(tree3[2], tree4_2, tree5_2[0])

                arrow4 = Arrow(tree4_2.get_right(), tree4_2.get_right() + RIGHT)
                ptext = Tex("4. Production Rule", font_size=30).next_to(arrow4.get_end(), RIGHT)
                self.play(Circumscribe(pgrp))
                rt = SurroundingRectangle(pgrp, color=RED)
                self.play(Create(rt))
                self.play(Create(arrow4))
                self.wait(0.5)
                self.play(Write(ptext))

            self.wait(0.5)
            self.play(
                FadeOut(title, *tree, *d, arrow1, arrow2, arrow3, arrow4, terminal, nonterminal, initial, rule, rt,
                        ptext, derivation_, parsing_tree_))

            ## Grammar ambiguity
            with self.voiceover("But, you may notice that there is something strange."):
                self.play(self.icon.animate.move_to(ORIGIN + UP))
                problem = Tex("Is there something STRANGE?",color=RED).next_to(self.icon, 2 * DOWN)
                self.play(Create(problem))
            self.wait(2)
            d.move_to(ORIGIN)
            tree[2].set_color(RED)

            ## another parsing tree
            tree1_ = Tex('E', font_size=30)  # 0
            tree2_ = Text(" / | \ ", font_size=30).next_to(tree1_, DOWN)  # 1
            tree3_ = Tex(r'E \quad', ' + ', r'\quad E', font_size=30, color=RED).next_to(tree2_, DOWN)  # 2
            tree4_1_ = Text("|", font_size=30).next_to(tree3_[0], DOWN)  # 3
            tree4_2_ = Text(" / | \ ", font_size=30).next_to(tree3_[-1], DOWN)  # 4
            tree5_1_ = Tex("ID", font_size=30).next_to(tree4_1_, DOWN)  # 5
            tree5_2_ = Tex("E", " * ", "E", font_size=30).next_to(tree4_2_, DOWN)  # 6
            tree6_1_ = Text(" | ", font_size=30).next_to(tree5_2_[0], DOWN)  # 7
            tree6_2_ = Text(" | ", font_size=30).next_to(tree5_2_[2], DOWN)  # 8
            tree7_1_ = Tex("ID", font_size=30).next_to(tree6_1_, DOWN)  # 9
            tree7_2_ = Tex("ID", font_size=30).next_to(tree6_2_, DOWN)  # 10

            tree_ = VGroup(tree1_, tree2_, tree3_, tree4_1_, tree4_2_, tree5_1_, tree5_2_, tree6_1_, tree6_2_, tree7_1_,
                           tree7_2_)

            d[1].set_color(RED)
            d2 = d.copy()
            d2[1] = Tex(r"$\Rightarrow$ E + E", font_size=30).next_to(d2[0], DOWN, aligned_edge=LEFT)
            d.scale(1.3)
            d2.scale(1.3)
            self.wait(0.5)
            with self.voiceover("Why should derivation process be this:"):
                self.play(ReplacementTransform(problem, d), FadeOut(self.icon))
            self.play(d.animate.shift(4 * LEFT))

            d2.shift(4 * RIGHT)
            d2[1].set_color(RED)
            arrow = Arrow(d.get_right(), d2.get_left(), buff=0.5, stroke_width=3, tip_length=0.3)
            self.wait(0.5)
            with self.voiceover("Rather than, this?!"):
                self.play(Create(arrow))
                self.play(Create(d2))
            self.wait(1.5)

            with self.voiceover("Yes, this weird thing is called syntax ambiguity!"):
                am = Tex("Syntax Ambiguity", color=PURPLE).next_to(arrow, UP)
                self.play(Write(am))
            self.wait(0.5)
            with self.voiceover(
                    "More precisely, syntax ambiguity means we could get two different parsing tree from one symbol string."):
                self.play(d.animate.to_edge(UP).scale(0.8), d2.animate.to_edge(UP).scale(0.8))
                self.play(Create(tree.next_to(d, DOWN, buff=0.5)), Create(tree_.next_to(d2, DOWN, buff=0.5)))
                self.wait(1)
            with self.voiceover(
                    "And to remove ambiguity here, We have to modified the syntax rule."):
                self.play(FadeIn(rule.to_edge(UP, buff=0.2).scale(0.8), run_time=2))
                self.play(Circumscribe(rule))
            self.wait(1)
            with self.voiceover(
                    "For example, if we change the rule in this way, by simply adding a new non-terminal symbol F"):
                self.play(FadeOut(arrow, am, d, d2, tree, tree_))
                self.play(rule.animate.move_to(ORIGIN + UP).scale(1.5))

                rule_ = Tex(
                    r"E $\rightarrow$ F  \quad  E $\rightarrow$ E + E \quad   F $\rightarrow$ F * F",
                    r"F $\rightarrow$ ( E ) \quad F $\rightarrow$ ID", font_size=32, color=YELLOW).arrange(DOWN).scale(
                    0.8).scale(1.5)

                arrow = Arrow(rule.get_bottom(), rule.get_bottom() + DOWN, stroke_width=2, tip_length=0.3)
                rule_.next_to(arrow.get_end(), DOWN)
                self.play(Create(arrow))
                self.play(Write(rule_))

        new_tree1_ = Tex('E', font_size=30)  # 0
        new_tree2_ = Text(" / | \ ", font_size=30).next_to(new_tree1_, DOWN)  # 1
        new_tree3_ = Tex(r'E \quad', ' + ', r'\quad E', font_size=30).next_to(new_tree2_, DOWN)  # 2
        new_tree4_1_ = Text("|", font_size=30).next_to(new_tree3_[0], DOWN)  # 3
        new_tree4_2_ = Text("|", font_size=30).next_to(new_tree3_[-1], DOWN)  # 4
        new_tree5_1_ = Tex("F", font_size=30).next_to(new_tree4_1_, DOWN)  # 5
        new_tree5_2_ = Tex("F", font_size=30).next_to(new_tree4_2_, DOWN)  # 6
        new_tree6_1_ = Text(" | ", font_size=30).next_to(new_tree5_1_[0], DOWN)  # 7
        new_tree6_2_ = Text(" / | \ ", font_size=30).next_to(new_tree5_2_, DOWN)  # 8
        new_tree7_1_ = Tex("ID", font_size=30).next_to(new_tree6_1_, DOWN)  # 9
        new_tree7_2_ = Tex("F", " * ", "F", font_size=30).next_to(new_tree6_2_, DOWN)  # 10
        new_tree8_1_ = Text(" | ", font_size=30).next_to(new_tree7_2_[0], DOWN)  # 11
        new_tree8_2_ = Text(" | ", font_size=30).next_to(new_tree7_2_[2], DOWN)  # 12
        new_tree9_1_ = Tex("ID", font_size=30).next_to(new_tree8_1_, DOWN)  # 13
        new_tree9_2_ = Tex("ID", font_size=30).next_to(new_tree8_2_, DOWN)  # 14
        new_Tree = VGroup(new_tree1_, new_tree2_, new_tree3_, new_tree4_1_, new_tree4_2_, new_tree5_1_, new_tree5_2_,
                          new_tree6_1_, new_tree6_2_, new_tree7_1_, new_tree7_2_, new_tree8_1_, new_tree8_2_,
                          new_tree9_1_, new_tree9_2_).scale(1.2)

        new_d1 = Tex('E', font_size=30)
        new_d2 = Tex(r"$\Rightarrow$ E + E", font_size=30).next_to(new_d1, DOWN, aligned_edge=LEFT)
        new_d3 = Tex(r"$\Rightarrow$ E + F", font_size=30).next_to(new_d2, DOWN, aligned_edge=LEFT)
        new_d4 = Tex(r"$\Rightarrow$ E + F * F", font_size=30).next_to(new_d3, DOWN, aligned_edge=LEFT)
        new_d5 = Tex(r"$\Rightarrow$ E + F * ID", font_size=30).next_to(new_d4, DOWN, aligned_edge=LEFT)
        new_d6 = Tex(r"$\Rightarrow$ E + ID * ID", font_size=30).next_to(new_d5, DOWN, aligned_edge=LEFT)
        new_d7 = Tex(r"$\Rightarrow$ F + ID * ID", font_size=30).next_to(new_d6, DOWN, aligned_edge=LEFT)
        new_d8 = Tex(r"$\Rightarrow$ ID + ID * ID", font_size=30).next_to(new_d7, DOWN, aligned_edge=LEFT)

        new_d = VGroup(new_d1, new_d2, new_d3, new_d4, new_d5, new_d6, new_d7, new_d8).scale(1.2)

        with self.voiceover("Then we could solve this problem as shown below. There is only one possible parsing tree left. I recommend you to pause the video to figure out why."):
            self.play(Circumscribe(rule_))
            self.wait(1)
            self.play(FadeOut(rule, arrow))
            self.play(rule_.animate.to_edge(UP).set_color(GREEN))
            new_Tree.shift(3 * LEFT + UP)
            new_d.shift(3 * RIGHT + UP)
            self.play(Create(new_Tree), Create(new_d))
            self.wait(1)

        another_d1 = Tex('E', font_size=30)
        another_d2 = Tex(r"$\Rightarrow$ E + E", font_size=30).next_to(another_d1, DOWN, aligned_edge=LEFT)
        another_d3 = Tex(r"$\Rightarrow$ F + E", font_size=30).next_to(another_d2, DOWN, aligned_edge=LEFT)
        another_d4 = Tex(r"$\Rightarrow$ ID + E", font_size=30).next_to(another_d3, DOWN, aligned_edge=LEFT)
        another_d5 = Tex(r"$\Rightarrow$ ID + F", font_size=30).next_to(another_d4, DOWN, aligned_edge=LEFT)
        another_d6 = Tex(r"$\Rightarrow$ E + F * F", font_size=30).next_to(another_d5, DOWN, aligned_edge=LEFT)
        another_d7 = Tex(r"$\Rightarrow$ F + ID * F", font_size=30).next_to(another_d6, DOWN, aligned_edge=LEFT)
        another_d8 = Tex(r"$\Rightarrow$ ID + ID * ID", font_size=30).next_to(another_d7, DOWN, aligned_edge=LEFT)

        another_d = VGroup(another_d1, another_d2, another_d3, another_d4, another_d5, another_d6, another_d7,
                           another_d8).scale(1.2).scale(0.8)
        self.wait(3)
        with self.voiceover(
                "Well, again, you may smartly notice that this derivation is not the only choice."):
            self.play(new_Tree.animate.scale(0.8).set_color(BLUE))
            self.play(new_Tree.animate.move_to(ORIGIN))
            self.play(new_d.animate.scale(0.8))
            self.play(new_d.animate.move_to(new_Tree.get_right() + 3 * RIGHT))
            another_d.move_to(new_Tree.get_left() + 3 * LEFT)
            self.play(Create(another_d))
        self.wait(1)
        with self.voiceover("Actually, these two derivations are all valid, because their corresponding parsing tree is the same."):
            self.wait(2)
            self.play(Indicate(new_Tree))
        self.wait(0.5)
        with self.voiceover("The one on the left hand side is called left-most derivation, because every time it expands the leftmost non-terminal"):
            self.play(Circumscribe(another_d))
            arrow_left = Arrow(another_d.get_left(), another_d.get_right(), buff=0.5, stroke_width=2,tip_length=0.2).next_to(another_d, DOWN)
            left = Tex("Left-most Derivation",font_size=28).next_to(arrow_left,DOWN)
            self.play(Create(arrow_left),Write(left))
        self.wait(0.5)
        with self.voiceover("While the other one on the right hand side is called right-most derivation, for the similar reason."):
            self.play(Circumscribe(new_d))
            arrow_right = Arrow(new_d.get_right(), new_d.get_left(), buff=0.5, stroke_width=2,tip_length=0.2).next_to(new_d, DOWN)
            right = Tex("Right-most Derivation",font_size=28).next_to(arrow_right,DOWN)
            self.play(Create(arrow_right),Write(right))
        self.wait(1)
        self.play(FadeOut(new_Tree,another_d,new_d,arrow_left,arrow_right,left,right,rule_))
        with self.voiceover("However, we still have to ask ourselves, are all problems solved?"):
            self.icon = SVGMobject('favicon').scale(0.5).shift(UP)
            self.play(FadeIn(self.icon))
            self.play(Rotate(self.icon, PI * 2))
            problem = Tex("All Problem Solved? ",color=RED).next_to(self.icon, DOWN,buff=1)
            self.play(GrowFromCenter(problem))
            self.play(FocusOn(problem))
            self.wait(1)
        with self.voiceover("For example, does this symbol string have a unique parsing tree under this syntax rule? Please think about it."):
            example = Tex("ID + ID + ID ?",font_size=50).next_to(self.icon, 2 * DOWN)
            self.wait(2)
            self.play(ReplacementTransform(problem,example))
            self.wait(1)
        with self.voiceover("Ok, then, today's video is over. Next time we will introduce more challenging part: Shift-Reduce Analysis."):
            self.wait(2.5)
            next = Text("Next Chapter: Shift-Reduce Analysis", gradient=(RED, BLUE, GREEN)).next_to(self.icon, DOWN,buff=1)
            self.play(ReplacementTransform(example, next))
        self.wait(0.3)
        self.play(FadeOut(next))
        with self.voiceover("Looking forward to our next meeting. SEE YOU SOON!!"):
            soon = Text("SEE YOU SOON", gradient=(RED, BLUE, GREEN)).next_to(self.icon, DOWN,buff=1)
            self.play(Write(soon,run_time=2))
            self.wait(1)
            self.play(FadeOut(soon))

    def ending(self):
        self.play(self.icon.animate.to_edge(UP, buff=1))
        listing = Code(
            "husky.py",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style=Code.styles_list[15],
            background="window",
            font_size=20,
            language="python",
        )
        self.add_sound("media/audio/mixkit-dog-barking-twice-1.wav", gain=1)
        self.play(Write(listing,run_time=5))
        self.wait(4)
        self.play(FadeOut(listing,self.icon))
        self.wait(1)

    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-GuyNeural", style="chat",
                g1obalspeed=1.15)
        )

        self.opening_animation()
        # self.chapter()
        # self.part1_lexical()
        # self.part2_syntax()
        # self.ending()
