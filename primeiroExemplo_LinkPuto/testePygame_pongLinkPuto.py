import sys
import pygame as pg
pg.init()
velocidade = [1,1]
alturaTela = 1000
larguraTela = 1800
preto = 0,0,0
dimensaoTela = larguraTela,alturaTela # cria uma tupla com os valores da variável
tela = pg.display.set_mode(dimensaoTela) # cria uma tela
linkPuto = pg.image.load("linkPuto.gif")
linkRect = linkPuto.get_rect()
while 1:
    for evento in pg.event.get():
        if(evento.type == pg.QUIT):
            sys.exit()
    linkRect = linkRect.move(velocidade)
    if(linkRect.left < 0 or linkRect.right > larguraTela):
        velocidade[0] = - velocidade[0]
    if(linkRect.top < 0 or linkRect.bottom > alturaTela):
        velocidade[1] = - velocidade[1]
    tela.fill(preto)
    tela.blit(linkPuto, linkRect)
    pg.display.flip()

    