import sys
import time
import pygame as game

game.init()
dimensaoTela = (720,720)
tela = game.display.set_mode(dimensaoTela)
x=0

coresEmRGB = {
    "branco":(255,255,255),
    "preto":(0,0,0),
    "vermelho":(255,0,0),
    "azul":(0,0,255),
    "verde":(0,255,0),
    "vermeloEscuro":(139,0,0),
    "cinza":(128, 128, 128),
    "prata":(192, 192, 192),
    "azulEscuro":(0,0,128),
    "amarelo":(255,255,0),
    "aqua":(0,255,255),
    "magenta":(255,0,255),
    "marrom":(128,0,0),
}

while True:
    for event in game.event.get():
        if(event.type == game.QUIT):
            sys.exit()
    if(x == 0):
        tela.fill(coresEmRGB["preto"])
        x=1
    else:
        tela.fill(coresEmRGB["vermelho"])
        x=0
    time.sleep(1)
    game.display.flip()