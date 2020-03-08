import time
import pygame

path = r""

#初始化
pygame.mixer.init()

#加载音乐

track = pygame.mixer.music.load(path)

#播放
pygame.mixer.music.play()

#
time.sleep(120)

#暂停
pygame.mixer.music.pause()

#停止
pygame.mixer.music.stop()