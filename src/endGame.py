import pygame
from pygame.locals import *


class EndGame:
    def __init__(self):
        pygame.init()

    def show_winning_screen(self, winner):
        print(f"{winner} wins!")
        screen = pygame.display.set_mode((640, 640))
        
        pygame.display.set_caption('Game Over')

        color = (255,255,255)
        color_light = (170,170,170)
        color_dark = (100,100,100)

        width = screen.get_width()
        height = screen.get_height()

        smallfont = pygame.font.SysFont('Corbel',35)

        button_quit_size = (120, 40)
        button_quit_pos = (width/2-60, 550)

        button_play_again_size = (200, 40)
        button_play_again_pos = (width/2-100, 450)

        text_quit = smallfont.render('quit' , True , color)
        text_quit_rect = text_quit.get_rect(center=(width/2, button_quit_pos[1]+18))

        text_play_again = smallfont.render('play again' , True , color)
        text_play_again_rect = text_play_again.get_rect(center=(width/2, button_play_again_pos[1]+18))

        font = pygame.font.Font(None, 74)
        text = font.render(f"{winner} wins!", True, (10, 10, 10))
        text_rect = text.get_rect(center=(width/2, height/2))

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                
                    if button_quit_pos[0] <= mouse[0] <= button_quit_pos[0]+button_quit_size[0] and button_quit_pos[1] <= mouse[1] <= button_quit_pos[1]+button_quit_size[1]:
                        pygame.quit()
                        return False

                    if button_play_again_pos[0] <= mouse[0] <= button_play_again_pos[0]+button_play_again_size[0] and button_play_again_pos[1] <= mouse[1] <= button_play_again_pos[1]+button_play_again_size[1]:
                        return True


            screen.fill((250, 250, 250))

            mouse = pygame.mouse.get_pos()

            if button_quit_pos[0] <= mouse[0] <= button_quit_pos[0]+button_quit_size[0] and button_quit_pos[1] <= mouse[1] <= button_quit_pos[1]+button_quit_size[1]:
                pygame.draw.rect(screen,color_light,[button_quit_pos[0],button_quit_pos[1], button_quit_size[0],button_quit_size[1]])
            else:
                pygame.draw.rect(screen,color_dark,[button_quit_pos[0] ,button_quit_pos[1], button_quit_size[0],button_quit_size[1]])

            if button_play_again_pos[0] <= mouse[0] <= button_play_again_pos[0]+button_play_again_size[0] and button_play_again_pos[1] <= mouse[1] <= button_play_again_pos[1]+button_play_again_size[1]:
                pygame.draw.rect(screen,color_light,[button_play_again_pos[0],button_play_again_pos[1], button_play_again_size[0],button_play_again_size[1]])
            else:
                pygame.draw.rect(screen,color_dark,[button_play_again_pos[0] ,button_play_again_pos[1], button_play_again_size[0],button_play_again_size[1]])

            screen.blit(text_quit , text_quit_rect)
            screen.blit(text_play_again , text_play_again_rect)
            screen.blit(text, text_rect)

            pygame.display.update()
