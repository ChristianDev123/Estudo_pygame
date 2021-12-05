import sys
import pygame as pg
pg.init()

dimensoesTela = [960,540]
corBranca = (255,255,255)
corVermelhoEscuro = (139, 0, 0)
posicaoCirculo = [350, 350]
raioCirculo = 50

tela = pg.display.set_mode(dimensoesTela)
tela.fill(corBranca)
pg.draw.circle(tela,(139,0,0),(350,350),50)
pg.display.flip()

while True:
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            sys.exit()