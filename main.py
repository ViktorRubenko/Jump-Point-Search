import pygame, grid, astar, jps, os, datetime

def main():

    print('Эвристика Манхэттена:\n1 - вызов алгоритма A*'+
          '\n2 - вызов алгоритма JPS\n3 - вызов обоих методов\n'+
          '\nЭвристика Евклида:\n5 - вызов алгоритма A*'+
          '\n6 - вызов алгоритма JPS\n7 - вызов обоих методов\n'+
          '\nF5 - очистить сетку\n')

    while True:
        try:
            size1 = int(input('Размер окна:\nШирина: '))
            size2 = int(input('Высота: '))
            size_node = int(input('Размер узла: '))
            if size1 % size_node !=0 or size2 % size_node !=0:
                print('Высота и ширина должны быть кратны размеру узла\n')
            else: break
        except:
            size1,size2 = 800,640
            size_node = 16
            break
            
    size = (size1,size2)

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
                    if Grid.matrix[pos[1]//size_node][pos[0]//size_node] == 0:
                        mark_border = True
                    else:
                        clear_border = True
                elif event.button == 3:
                    Grid.mark_node(pygame.mouse.get_pos(),background)
            if (event.type == pygame.MOUSEBUTTONUP and
                event.button == 1):
                mark_border = False
                clear_border = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    Grid.refresh(background)
                if event.key == pygame.K_1:
                    Grid.lightrefresh(background)
                    Grid.drawpath(astar.method(Grid.matrix,Grid.start,Grid.goal,1),
                                  background,1)
                if event.key == pygame.K_2:
                    Grid.lightrefresh(background)
                    Grid.drawpath(jps.method(Grid.matrix,Grid.start,Grid.goal,1),
                                  background,2)
                if event.key == pygame.K_3:
                    Grid.lightrefresh(background)
                    Grid.drawpath(astar.method(Grid.matrix,Grid.start,Grid.goal,1),
                                  background,1)
                    Grid.drawpath(jps.method(Grid.matrix,Grid.start,Grid.goal,1),
                                  background,2)
                if event.key == pygame.K_5:
                    Grid.lightrefresh(background)
                    Grid.drawpath(astar.method(Grid.matrix,Grid.start,Grid.goal,2),
                                  background,1)
                if event.key == pygame.K_6:
                    Grid.lightrefresh(background)
                    Grid.drawpath(jps.method(Grid.matrix,Grid.start,Grid.goal,2),
                                  background,2)
                if event.key == pygame.K_7:
                    Grid.lightrefresh(background)
                    Grid.drawpath(astar.method(Grid.matrix,Grid.start,Grid.goal,2),
                                  background,1)
                    Grid.drawpath(jps.method(Grid.matrix,Grid.start,Grid.goal,2),
                                  background,2)
        screen.blit(background,(0,0))
        pygame.display.update()

        if mark_border:
            Grid.mark_border(pygame.mouse.get_pos(),background)
        if clear_border:
            Grid.clear_border(pygame.mouse.get_pos(),background)
                
    pygame.quit()

if __name__=='__main__': main()
