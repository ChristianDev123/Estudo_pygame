import sys
import pygame as pg
pg.init()

dimensoesTela = [960,540]
corBranca = (255,255,255)

tela = pg.display.set_mode(dimensoesTela)
tela.fill(corBranca)
pg.display.flip()
while True:
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            sys.exit()