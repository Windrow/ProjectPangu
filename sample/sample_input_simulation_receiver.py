# A sample executable based on pygame to react the mouse and keyboard actions simulated by input simulator.

import pygame
from pygame.locals import *


size = (1080, 720)
pygame_fps = 30
color_blue = (0, 0, 128)
color_red = (128, 0, 0)
thickness = 4
mouse_up = True
mouse_pos = (-1, -1)
key_pos = (540, 360)

pygame.init()
pygame.display.set_caption("Sample Input Simulation")
display_surf = pygame.display.set_mode(size)
fps_clock = pygame.time.Clock()

pygame.draw.circle(display_surf, color_red, key_pos, thickness, 0)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEMOTION:
            if mouse_up == False:
                if mouse_pos[0] <= size[0] and mouse_pos[0] >= 0 and mouse_pos[1] <= size[1] and mouse_pos[1] >= 0:
                    # draw a line
                    pygame.draw.line(display_surf, color_blue, mouse_pos, event.pos, thickness)
            mouse_pos = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mouse_up = False
        elif event.type == MOUSEBUTTONUP:
            if mouse_up == False:
                # draw a spot
                pygame.draw.circle(display_surf, color_blue, event.pos, thickness, 0)
            mouse_up = True
        elif event.type == KEYDOWN:
            # About long press: cloud.tencent.com/developer/article/1490216
            if event.key == K_LEFT:
                key_pos = tuple((key_pos[0] - 16, key_pos[1]))
            elif event.key == K_RIGHT:
                key_pos = tuple((key_pos[0] + 16, key_pos[1]))
            elif event.key == K_UP:
                key_pos = tuple((key_pos[0], key_pos[1] - 16))
            elif event.key == K_DOWN:
                key_pos = tuple((key_pos[0], key_pos[1] - 16))
            pygame.draw.circle(display_surf, color_red, key_pos, thickness, 0)
    pygame.display.update()
    fps_clock.tick(pygame_fps)

pygame.quit()
