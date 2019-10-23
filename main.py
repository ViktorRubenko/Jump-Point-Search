import pygame
import os
import datetime
import grid
import astar
import jps


def main():

    print(
        "Right click to set start node and end node"
        + "\nHold left button to draw obstacles"
        + "\nButtons for calling algorithms:"
        + "\nManhattan heuristic:\n1 - call A* algorithm"
        + "\n2 - call JPS algorithm\n3 - call both\n"
        + "\nEuclidean heuristic:\n5 - call A* algorithm"
        + "\n6 - call JPS algorithm\n7 - call both\n"
        + "\nF5 - clear grid\n"
    )

    while True:
        try:
            width, height, size_node = map(
                int,
                [
                    input(x)
                    for x in ("Window width: ", "Window height: ", "Node size: ")
                ],
            )
            if width % size_node != 0 or height % size_node != 0:
                print(
                    "Width and height should be fully divided by the size of the node\n"
                )
            else:
                break
        except:
            width, height = 800, 640
            size_node = 16
            break

    size = (width, height)

    pygame.init()
    screen = pygame.display.set_mode(size)
    running = True
    mark_border = False
    clear_border = False

    background = pygame.Surface(size)
    Grid = grid.Grid(size, size_node)
    Grid.refresh(background)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if (
                        Grid.matrix[pos[1] // size_node][pos[0] // size_node]
                        == 0
                    ):
                        mark_border = True
                    else:
                        clear_border = True
                elif event.button == 3:
                    Grid.mark_node(pygame.mouse.get_pos(), background)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mark_border = False
                clear_border = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    Grid.refresh(background)
                if event.key == pygame.K_1:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        astar.method(Grid.matrix, Grid.start, Grid.goal, 1),
                        background,
                        1,
                    )
                if event.key == pygame.K_2:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        jps.method(Grid.matrix, Grid.start, Grid.goal, 1),
                        background,
                        2,
                    )
                if event.key == pygame.K_3:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        astar.method(Grid.matrix, Grid.start, Grid.goal, 1),
                        background,
                        1,
                    )
                    Grid.drawpath(
                        jps.method(Grid.matrix, Grid.start, Grid.goal, 1),
                        background,
                        2,
                    )
                if event.key == pygame.K_5:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        astar.method(Grid.matrix, Grid.start, Grid.goal, 2),
                        background,
                        1,
                    )
                if event.key == pygame.K_6:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        jps.method(Grid.matrix, Grid.start, Grid.goal, 2),
                        background,
                        2,
                    )
                if event.key == pygame.K_7:
                    Grid.lightrefresh(background)
                    Grid.drawpath(
                        astar.method(Grid.matrix, Grid.start, Grid.goal, 2),
                        background,
                        1,
                    )
                    Grid.drawpath(
                        jps.method(Grid.matrix, Grid.start, Grid.goal, 2),
                        background,
                        2,
                    )
        screen.blit(background, (0, 0))
        pygame.display.update()

        if mark_border:
            Grid.mark_border(pygame.mouse.get_pos(), background)
        if clear_border:
            Grid.clear_border(pygame.mouse.get_pos(), background)

    pygame.quit()


if __name__ == "__main__":
    main()
