###################################################
#             def user_input() with Pygame        #
#   At a Black Screen it will ask for User Input. #
#   Input will show up as typing.                 #
#   Input will saved to Var: name and be returned.#
###################################################

import pygame


# Constants for the game
WIDTH = 600
HEIGHT = 600
FPS = 60
X = 10 #  x input
Y = 10 # y input
X1 = 10 # x prompt
Y1= 10 # y prompt

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (125, 125, 0)
LGREEN = (26, 82, 118)

# Font
FONT = "comic.ttf"
SIZE = 25

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

clock = pygame.time.Clock()

def user_input():
    
    def text_print(word1,x,y):
        global name
        font = pygame.font.Font(FONT, SIZE)
        name = ""
        for letter in word1:
            name = name + str(letter)
        text = font.render("{}".format(name), True, WHITE)
        screen.fill(LGREEN)
        screen.blit(text,(x,y))
        
        pygame.display.update()

    
    name_user = []
    ask = "Please enter your name or alias: "
    text_print(ask,X1,Y1) 
    
    #pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                   
                if event.key == pygame.K_BACKSPACE:
                    name_user.pop(-1)
                    text_print(name_user,X,Y)
                      
                       
            
                if event.key == pygame.K_b:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                   
                if event.key == pygame.K_c:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                   
                if event.key == pygame.K_d:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_e:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_f:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_g:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_h:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_s:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_j:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_k:
                   name_user.append(chr(event.key))
                   text_print(name_user,X,Y)
                if event.key == pygame.K_l:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_y:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_x:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_v:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_n:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                   
                if event.key == pygame.K_m:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                   
                if event.key == pygame.K_q:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_w:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_r:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_t:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_z:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_u:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_i:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_o:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_p:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_MINUS:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)
                if event.key == pygame.K_SPACE:
                    
                    name_user.append(chr(pygame.K_UNDERSCORE))
                    text_print(name_user,X,Y)   
                if event.key == pygame.K_UNDERSCORE:
                    name_user.append(chr(event.key))
                    text_print(name_user,X,Y)          
                if event.key == pygame.K_RETURN:
                    done=False
                # add more events if needed...

    
    return name

