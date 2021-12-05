import sys
import pygame as pg
pg.init()

dimensoesTela = [960,540]
corBranca = (255,255,255)
corAzul = (0,0,255)
corVermelha = (255,0,0)
posPixel = [350,350]

tela = pg.display.set_mode(dimensoesTela)
tela.fill(corBranca)
for linha1 in range(50):
    posPixel[0] = posPixel[0] + 1
    posPixel[1] = posPixel[1] + 1
    if (posPixel[1] > 399):
        break
    tela.set_at(posPixel,corAzul)
posPixel = [349,349]
for reforcoLinha1 in range(50):
    posPixel[0] = posPixel[0] + 1
    posPixel[1] = posPixel[1] + 1
    if (posPixel[1] > 401):
        break
    tela.set_at(posPixel,corAzul)

posPixel = [400,350]
for linha2 in range(50):
    posPixel[0] = posPixel[0] - 1
    posPixel[1] = posPixel[1] + 1
    if(posPixel[1]>399):
        break
    tela.set_at(posPixel,corVermelha)
posPixel = [401, 351]
for reforcoLinha2 in range(50):
    posPixel[0] = posPixel[0] - 1
    posPixel[1] = posPixel[1] + 1
    if(posPixel[1]>401):
        break
    tela.set_at(posPixel,corVermelha)


pg.display.flip()
while True:
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            sys.exit()