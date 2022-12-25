import pygame
from user_input_pygame import user_input
from Constants_Hangman import *
from Funktions_Hangman import *

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
pygame_icon = pygame.image.load("hangman.png")
pygame.display.set_icon(pygame_icon)

clock = pygame.time.Clock()

# Load the hangman images
hangman_images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    hangman_images.append(image)

def start_game():
    global menu
    menu = None

def quit_game():
    global running
    running = False 

# Class for the game
class Game:
    def __init__(self):
        self.hangman_index = 0
        
        self.lifes = 3
        self.score = -1
        self.name = user_input().capitalize()
        self.high_name, self.high_score = read_score()
        self.cursor_pos = 0
        self.input_string = ""
        self.font = pygame.font.Font(FONT, SIZE)

    def reset(self):
        self.hangman_index = 0
        if easy == True:
            self.word = word_pick_easy()
        else:
            self.word = word_pick_noteasy()
        self.word_letters = [letter for letter in self.word]
        self.guessed_letters = []
        self.word_guessed = ["_" for letter in self.word_letters]
        self.score = self.score +1
        if self.score > self.high_score:
            self.high_score = max(self.score, self.high_score)
            write_score(self.name, self.high_score)
        
        self.high_name, self.high_score = read_score()

    def reset_quit(self):
        self.hangman_index = 0
        if easy == True:
            self.word = word_pick_easy()
        else:
            self.word = word_pick_noteasy()
        self.word_letters = [letter for letter in self.word]
        self.guessed_letters = []
        self.word_guessed = ["_" for letter in self.word_letters]
        self.score = -1
        if self.score > self.high_score:
            self.high_score = max(self.score, self.high_score)
            write_score(self.name, self.high_score)
        
        self.high_name, self.high_score = read_score()

    def draw(self):
        # Draw the current hangman image
        screen.blit(hangman_images[self.hangman_index], (100, 100))
        
        # Draw the word
        word_text = " ".join(self.word_guessed)
        font = pygame.font.Font(FONT, SIZE)
        text = font.render(word_text, True, BLACK)
        screen.blit(text, (300, 300))

        # Draw the letters that have been guessed
        guessed_text = " ".join(self.guessed_letters)
        font = pygame.font.Font(FONT, SIZE)
        text = font.render(guessed_text, True, BLACK)
        screen.blit(text, (300, 350))

        # Draw the score
        score_text = f"Score: {self.score}"
        font = pygame.font.Font(FONT, SIZE)
        text = font.render(score_text, True, BLACK)
        screen.blit(text, (300, 50))

        # Draw the lifes
        score_text = f"Lifes: {self.lifes}"
        font = pygame.font.Font(FONT, SIZE)
        text = font.render(score_text, True, BLACK)
        screen.blit(text, (300, 10))

        # Draw the high score
        high_score_text = f"High Scorer: {self.high_name} Points: {self.high_score}  "
        font = pygame.font.Font(FONT, SIZE)
        text = font.render(high_score_text, True, BLACK)
        screen.blit(text, (300, 100))

    def show_game_over_screen(self):
        font = pygame.font.Font(FONT, SIZE)
        text = font.render("Game Over", True, BLACK)
        text1= font.render(f"Word: {self.word.upper()}", True, BLACK)
        screen.blit(text, (300, 400))
        screen.blit(text1, (300, 450))

    def loose_life_screen(self):
        font = pygame.font.Font(FONT, SIZE)
        text = font.render("YOU LOST A LIFE!", True, BLACK)
        text1= font.render(f"Word: {self.word.upper()}", True, BLACK)
        screen.blit(text, (300, 400))
        screen.blit(text1, (300, 450))
        self.score -= 1


    
    def show_you_win_screen(self):
        font = self.font
        text = font.render("You Win!", True, BLACK)
        screen.blit(text, (300, 400))
        if self.score > self.high_score:
            self.high_score = self.score
        
# Class for the menu
class Menu:
    def __init__(self):
        self.menu_items = ["Easy", "Not so Easy", "Quit"]
        self.selected_index = 0

    def draw(self):
        # Draw the menu items
        for i, item in enumerate(self.menu_items):
            font = pygame.font.Font(FONT, SIZE)
            text = font.render(item, True, BLACK)
            x = 250
            y = 200 + i * 50
            screen.blit(text, (x, y))

            # Draw a highlight around the selected item
            if i == self.selected_index:
                pygame.draw.rect(screen, BLACK, (x - 10, y - 10, text.get_width() + 20, text.get_height() + 20), 3)
   
# Main game loop
def main():
    global menu, game, running, easy
    game = Game()
    menu = Menu()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if menu is not None:
                    
                    if event.key == pygame.K_UP:
                        menu.selected_index = (menu.selected_index - 1) % len(menu.menu_items)
                    elif event.key == pygame.K_DOWN:
                        menu.selected_index = (menu.selected_index + 1) % len(menu.menu_items)
                    elif event.key == pygame.K_RETURN:
                        if menu.selected_index == 0:
                            easy = True
                            start_game()
                            game.reset()
                        elif menu.selected_index == 1:
                            easy = False
                            start_game()
                            game.reset()
                        elif menu.selected_index == 2:
                            quit_game()
                else:
                    # Check if the letter has already been guessed
                    if event.unicode in game.guessed_letters or event.unicode in game.word_guessed:
                        continue
                    elif event.unicode in game.word_letters:
                        # Update the word_guessed and guessed_letters lists
                        for i in range(len(game.word_letters)):
                            if game.word_letters[i] == event.unicode:
                                game.word_guessed[i] = event.unicode
                        game.guessed_letters.append(event.unicode)
                    
                        # Increment the score for each letter
                        #game.score += 1

                        # Check if the player has won
                        if "_" not in game.word_guessed:
                            game.draw()
                            pygame.display.update()
                            game.show_you_win_screen()
                            pygame.display.update()
                            pygame.time.delay(2000)
                            #game.reset()
                            menu = Menu()
                            
                            
                    else:
                        # Incorrect guess
                        game.hangman_index += 1
                        game.draw()
                        game.guessed_letters.append(event.unicode)

                        #print(game.hangman_index)

                        # Check if the player has lost
                        if game.hangman_index == 6:
                            game.lifes -= 1                            
                            if game.lifes >= 0:
                                game.draw()
                                pygame.display.update()
                                game.loose_life_screen()
                                pygame.display.update()
                                pygame.time.delay(4000)
                                menu = Menu()
                            elif game.lifes < 0:
                                game.show_game_over_screen()
                                pygame.display.update()
                                pygame.time.delay(6000)
                                game.lifes = 3
                                game.score = -1                          
                                menu = Menu()
                            
                                

                            

        # Clear the screen
        screen.fill(WHITE)
        # Draw the menu or game
        if menu is not None:
            menu.draw()
        else:
            game.draw()
        
        
        # Update the display
        pygame.display.update()

    pygame.quit()
main()