from codecs import BufferedIncrementalEncoder
from mimetypes import init
import play
import pygame
pygame.init()
pygame.mixer.init()

play.set_backdrop((255, 130, 240))

text1= play.new_text(words="це класне піаніно для гри", x=0, y=200)
text2 = play.new_text(words="створити свою милодію натискаючи ці клавіші", x=0, y=150)

keys = []
sounds = []

for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color="white", width=40, height=120, x=key_x, y=0, border_width=3, border_color="black") 
    keys.append(key)
    sound = pygame.mixer.Sound(str(i + 1) + ".ogg")
    sounds.append(sound)

@play.when_program_starts
def start():
    pass

@play.repeat_forever
async def play_piano():
    for j in range(8):
        if keys[j].is_clicked:
            sounds[j].play()
            keys[j].color = "light green"
            await play.timer(0.3)
            keys[j].color = "white"

play.start_program()