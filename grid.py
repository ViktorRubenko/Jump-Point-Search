import numpy, pygame

white = (255, 255, 255)
lightgrey = (205, 205, 205)
startcolor = (80, 240, 104)
goalcolor = (238, 68, 0)
bordercolor = (128, 128, 128)
astarcolor = (255, 255, 0)
jpscolor = (230, 0, 230)


class Grid:
    def __init__(self, size_screen, size_node):
        self.size = size_screen
        self.size_node = size_node
        self.matrix = numpy.zeros(1)
        self.start, self.goal = (0, 0), (0, 0)
        self.flagstart = False
        self.flaggoal = False

        self.SGB = pygame.Surface(size_screen)
        self.PathA = pygame.Surface(size_screen)
        self.PathJ = pygame.Surface(size_screen)
        self.SGB.set_colorkey(white)
        self.PathA.set_colorkey(white)
        self.PathJ.set_colorkey(white)

    def refresh(self, layer):
        self.start, self.goal = (0, 0), (0, 0)
        self.flagstart = False
        self.flaggoal = False
        self.matrix = numpy.zeros(
            (self.size[1] // self.size_node, self.size[0] // self.size_node)
        )

        layer.fill(white)
        self.SGB.fill(white)
        self.PathA.fill(white)
        self.PathJ.fill(white)
        for x in range(0, self.size[0], self.size_node):
            pygame.draw.line(layer, lightgrey, (x, 0), (x, self.size[1]))
        for y in range(0, self.size[1], self.size_node):
            pygame.draw.line(layer, lightgrey, (0, y), (self.size[0], y))

    def lightrefresh(self, layer):
        layer.fill(white)
        self.PathA.fill(white)
        self.PathJ.fill(white)
        for x in range(0, self.size[0], self.size_node):
            pygame.draw.line(layer, lightgrey, (x, 0), (x, self.size[1]))
        for y in range(0, self.size[1], self.size_node):
            pygame.draw.line(layer, lightgrey, (0, y), (self.size[0], y))
        layer.blit(self.SGB, (0, 0))

    def drawrect(self, layer, color, pos):
        pygame.draw.rect(
            layer,
            color,
            (
                pos[0] // self.size_node * self.size_node + 1,
                pos[1] // self.size_node * self.size_node + 1,
                self.size_node - 1,
                self.size_node - 1,
            ),
        )

    def drawpath(self, path, main_layer, flag):
        nowayfont = pygame.font.Font("myriadpro.otf", 25)
        nowayfont1 = pygame.font.Font("myriadpro.otf", 25)
        if flag == 1:
            time = nowayfont.render("A*:" + str(path[1]), True, (34, 177, 86))
            time1 = nowayfont1.render(
                "A*:" + str(path[1]), True, (255, 255, 255)
            )
            main_layer.blit(time1, (16, 11))
            main_layer.blit(time, (15, 10))
        else:
            time = nowayfont.render("JPS:" + str(path[1]), True, (34, 177, 86))
            time1 = nowayfont1.render(
                "JPS:" + str(path[1]), True, (255, 255, 255)
            )
            main_layer.blit(time1, (6, 36))
            main_layer.blit(time, (5, 35))

        if path[0] == 0:
            noway = nowayfont.render("Путь не найден", True, (34, 177, 86))
            noway1 = nowayfont1.render("Путь не найден", True, (255, 255, 255))
            main_layer.blit(noway1, (6, 56))
            main_layer.blit(noway, (5, 55))
            return

        if flag == 1:
            i = 0
            while i < len(path[0]) - 1:
                pygame.draw.line(
                    self.PathA,
                    astarcolor,
                    (
                        path[0][i][1] * self.size_node + self.size_node // 2,
                        path[0][i][0] * self.size_node + self.size_node // 2,
                    ),
                    (
                        path[0][i + 1][1] * self.size_node
                        + self.size_node // 2,
                        path[0][i + 1][0] * self.size_node
                        + self.size_node // 2,
                    ),
                    self.size_node // 2,
                )
                i += 1
            main_layer.blit(self.PathA, (0, 0))
        else:
            i = 0
            while i < len(path[0]) - 1:
                pygame.draw.line(
                    self.PathJ,
                    jpscolor,
                    (
                        path[0][i][1] * self.size_node + self.size_node // 2,
                        path[0][i][0] * self.size_node + self.size_node // 2,
                    ),
                    (
                        path[0][i + 1][1] * self.size_node
                        + self.size_node // 2,
                        path[0][i + 1][0] * self.size_node
                        + self.size_node // 2,
                    ),
                    self.size_node // 2,
                )
                i += 1
            main_layer.blit(self.PathJ, (0, 0))

    def mark_border(self, pos, main_layer):
        if (
            (pos[1] // self.size_node, pos[0] // self.size_node) != self.start
            and (pos[1] // self.size_node, pos[0] // self.size_node)
            != self.goal
        ):
            if (
                self.matrix[pos[1] // self.size_node][pos[0] // self.size_node]
                == 0
            ):
                self.matrix[pos[1] // self.size_node][
                    pos[0] // self.size_node
                ] = 1
                self.drawrect(self.SGB, bordercolor, pos)
                main_layer.blit(self.SGB, (0, 0))

    def clear_border(self, pos, main_layer):
        if (
            (pos[1] // self.size_node, pos[0] // self.size_node) != self.start
            and (pos[1] // self.size_node, pos[0] // self.size_node)
            != self.goal
        ):
            if (
                self.matrix[pos[1] // self.size_node][pos[0] // self.size_node]
                == 1
            ):
                self.matrix[pos[1] // self.size_node][
                    pos[0] // self.size_node
                ] = 0
                self.drawrect(self.SGB, (254, 254, 254), pos)
                main_layer.blit(self.SGB, (0, 0))

    def mark_node(self, pos, main_layer):
        if not self.flagstart:
            self.start = (pos[1] // self.size_node, pos[0] // self.size_node)
            self.drawrect(self.SGB, startcolor, pos)
            self.flagstart = True
            main_layer.blit(self.SGB, (0, 0))
            return

        if (
            not self.flaggoal
            and (pos[1] // self.size_node, pos[0] // self.size_node)
            != self.start
        ):
            self.goal = (pos[1] // self.size_node, pos[0] // self.size_node)
            self.drawrect(self.SGB, goalcolor, pos)
            self.flaggoal = True
            main_layer.blit(self.SGB, (0, 0))
            return
