# A sample executable to verify the feasibility of recording a pygame program to video file.
# Reference to:
# https://zhuanlan.zhihu.com/p/150205805
# https://blog.csdn.net/m0_50944918/article/details/111299881
# https://nerdparadise.com/programming/pygame/part3

import pygame
import cv2
from PIL import Image
import numpy
import gtts
#from playsound import playsound
import os


os.system("mkdir ../output")

# video generation
#file_path = r"../output/sample_video.mp4v"
#fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
video_fps = 30
size = (1080, 720)
video0 = cv2.VideoWriter("../output/sample_video_0.avi", fourcc, video_fps, size)

pygame.init()
pygame.display.set_caption("Sample Video Recorder")
pygame_fps = 30
display_surf = pygame.display.set_mode(size)
fps_clock = pygame.time.Clock()

t = 0
while t < 60:
    t += 1
    pygame.draw.rect(display_surf, (0, 0, 128), (540 - t*2, 360 - t, t*4, t*2))
    pygame.display.update()
    image_string = pygame.image.tostring(display_surf.subsurface(0, 0, 1080, 720), "RGB")
    pil_image = Image.frombytes("RGB", (1080, 720), image_string)
    img = cv2.cvtColor(numpy.asarray(pil_image), cv2.COLOR_RGB2BGR)
    video0.write(img)
    fps_clock.tick(pygame_fps)

video0.release()
#gst-launch-1.0 filesrc location=sample_video.avi ! decodebin ! queue ! videoconvert ! videoscale ! video/x-raw, width=800, height=600 ! ximagesink

# audio generation
tts = gtts.gTTS("Hello world")
tts.save("../output/sample_audio.mp3")
#print(gtts.lang.tts_langs())
#playsound("hello.mp3")

# merge video and audio
os.system("ffmpeg -i ../output/sample_video_0.avi -i ../output/sample_audio.mp3 ../output/sample_video_1.avi -y")
