import pygame, time
pygame.init()
fenetre_taille= (800, 600)
red=(255, 0, 0)
i=0
black=(0, 0, 0)


pygame.display.set_caption("titre de la fenètre")
surface_fenetre= pygame.display.set_mode(fenetre_taille)


def afficher_couleur(couleur3):
    for i in range(1,250):
        for g in range(1,250):
            pygame.draw.line(surface_fenetre,(0+i, 0+g, couleur3), [10+i,10+g], [10+i,10+g], 10)	

lancer = True
while lancer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lancer=False

    surface_fenetre.fill(black)
    afficher_couleur(255)
    
    pygame.display.flip()