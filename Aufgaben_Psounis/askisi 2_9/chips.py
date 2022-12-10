







def updateChips():
    global playerChips
    pygame.draw.rect(screen, (0,128,0), (39, 585, 200, 40), 0)
    label = smallFont.render('Chips: ' + str(playerChips), 1, (255,255,255))
    screen.blit(label, (10, 585))