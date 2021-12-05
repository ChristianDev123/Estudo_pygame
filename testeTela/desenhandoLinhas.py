import sys
import pygame as game

game.init()

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
dimensao = [720,720]
tela = game.display.set_mode(dimensao)
tela.fill(coresEmRGB["branco"])
alturaTela = tela.get_height()
larguraTela = tela.get_width()

linhasTela = {
    "horizontalC": {
        "posInicial":(0,alturaTela/3),
        "posFinal":(larguraTela,alturaTela/3),
    },
    "horizontalB":{
        "posInicial":(0,(alturaTela/3)*2),
        "posFinal":(larguraTela,(alturaTela/3)*2),
    },
    "verticalE":{
        "posInicial":(larguraTela/3,0),
        "posFinal":(larguraTela/3,alturaTela),
    },
    "verticalD":{
        "posInicial":((larguraTela/3)*2,0),
        "posFinal":((larguraTela/3)*2,alturaTela),
    }
}

game.draw.line(tela,coresEmRGB["vermelho"],linhasTela["horizontalC"]["posInicial"],linhasTela["horizontalC"]["posFinal"],7)
game.draw.line(tela,coresEmRGB["vermelho"],linhasTela["horizontalB"]["posInicial"],linhasTela["horizontalB"]["posFinal"],7)
game.draw.line(tela,coresEmRGB["azul"],linhasTela["verticalE"]["posInicial"],linhasTela["verticalE"]["posFinal"],7)
game.draw.line(tela,coresEmRGB["azul"],linhasTela["verticalD"]["posInicial"],linhasTela["verticalD"]["posFinal"],7)
game.display.flip()

while True:
    for event in game.event.get():
        if(event.type == game.QUIT):
            sys.exit()
