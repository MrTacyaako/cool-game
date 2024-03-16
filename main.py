from pygame import *


window = display.set_mode((900, 500))
display.set_caption('Гориллы')

background = transform.scale(image.load('background.jpg'), (900, 500))
sprite1 = transform.scale(image.load('sprite1.jpg'), (100, 70))
sprite2 = transform.scale(image.load('sprite2.png'), (70, 50))

x1 = 100
y1 = 200 
x2 = 500
y2 = 200

clock = time.Clock()
FPS = 60


game = True
while game:

    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    

    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_UP]:
        y2 -= 10
    if key_pressed[K_DOWN]:
        y2 += 10
    if key_pressed[K_RIGHT]:
        x2 += 10
    if key_pressed[K_LEFT]:
        x2 -= 10

    key_pressed = key.get_pressed()
    if key_pressed[K_s]:
        y1 += 10
    if key_pressed[K_w]:
        y1 -= 10
    if key_pressed[K_a]:
        x1 -= 10
    if key_pressed[K_d]:
        x1 += 10



    display.update()
    clock.tick(FPS)