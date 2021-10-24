# A sample executable to verify the feasibility of recording a pygame program to video file.
# Reference to:
# https://zhuanlan.zhihu.com/p/150205805
# https://blog.csdn.net/m0_50944918/article/details/111299881

import pygame
import cv2
from PIL import Image
import numpy



file_path = r"../output/sample_video.mp4v"
fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
video_fps = 30
size = (1080, 720)
video = cv2.VideoWriter(file_path, fourcc, video_fps, size)

pygame.init()
pygame.display.set_caption("Sample Video Recorder")
pygame_fps = 30
display_surf = pygame.display.set_mode(size)
fps_clock = pygame.time.Clock()

t = 0
while t < 180:
    t += 1
    pygame.draw.rect(display_surf, (0, 0, 128), (540 - t*2, 360 - t, t*4, t*2))
    pygame.display.update()
    image_string = pygame.image.tostring(display_surf.subsurface(0, 0, 1080, 720), "RGB")
    pil_image = Image.frombytes("RGB", (1080, 720), image_string)
    img = cv2.cvtColor(numpy.asarray(pil_image), cv2.COLOR_RGB2BGR)
    video.write(img)
    fps_clock.tick(pygame_fps)

video.release()
