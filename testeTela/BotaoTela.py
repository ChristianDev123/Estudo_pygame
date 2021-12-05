import pygame as pg
import sys

pg.init()

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

dimensao = (720,720)
tela = pg.display.set_mode(dimensao)
tela.fill(coresEmRGB["branco"])
pg.display.flip()

larguraTela = tela.get_width()
alturaTela = tela.get_height()
fonteTexto = pg.font.SysFont("Times",35)
texto = fonteTexto.render("Saída", True, coresEmRGB["azulEscuro"])
mouse = pg.mouse.get_pos()

while True:
    for evento in pg.event.get():
        if(evento.type == pg.QUIT):
            sys.exit()
        if(evento.type == pg.MOUSEBUTTONDOWN):
             if (larguraTela/2 <= mouse[0] <= larguraTela/2+140 and alturaTela/2 <= mouse[1] <= alturaTela/2+40):
                 pg.QUIT

if(larguraTela/2 <= mouse[0] <= larguraTela/2+140 and alturaTela/2 <= mouse[1] <= alturaTela/2+40): 
        pg.draw.rect(tela,coresEmRGB["vermelho"],[larguraTela/2,alturaTela/2,140,40])   
else: 
    pg.draw.rect(tela,coresEmRGB["branco"],[larguraTela/2,alturaTela/2,140,40]) 
tela.blit(texto,(larguraTela/2+50,alturaTela/2)) 
          
pg.display.update() 