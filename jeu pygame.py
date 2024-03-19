import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Geometry Dash")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables du joueur
player_width = 50
player_height = 50
player_x = 50
player_y = WINDOW_HEIGHT // 2 - player_height // 2
player_velocity = 10

# Variables des obstacles
obstacle_width = 50
obstacle_height = random.randint(50, 300)
obstacle_x = WINDOW_WIDTH
obstacle_y = WINDOW_HEIGHT - obstacle_height
obstacle_velocity = 10
obstacle_gap = 200

# Score
score = 0
font = pygame.font.Font(None, 36)

# Compteur de collisions
collision_counter = 0

# Fonction pour afficher le score
def display_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    WINDOW.blit(score_text, (10, 10))

# Boucle principale du jeu
clock = pygame.time.Clock()
running = True
while running:
    WINDOW.fill(WHITE)
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_y -= player_velocity
    else:
        player_y += player_velocity

    # Mouvement de l'obstacle
    obstacle_x -= obstacle_velocity

    # Gestion des collisions
    if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width:
        if player_y < obstacle_height or player_y + player_height > obstacle_height + obstacle_gap:
            # Collision détectée
            collision_counter += 1
            if collision_counter >= 3:
                running = False  # Le joueur meurt après 3 collisions
            else:
                obstacle_x = WINDOW_WIDTH
                obstacle_height = random.randint(50, 300)
                score += 1

    # Affichage du joueur
    pygame.draw.rect(WINDOW, BLACK, (player_x, player_y, player_width, player_height))

    # Affichage de l'obstacle
    pygame.draw.rect(WINDOW, BLACK, (obstacle_x, 0, obstacle_width, obstacle_height))
    pygame.draw.rect(WINDOW, BLACK, (obstacle_x, obstacle_height + obstacle_gap, obstacle_width, WINDOW_HEIGHT - obstacle_height - obstacle_gap))

    # Réinitialisation de l'obstacle lorsqu'il sort de l'écran
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WINDOW_WIDTH
        obstacle_height = random.randint(50, 300)
        score += 1

    # Affichage du score
    display_score()

    pygame.display.update()
    clock.tick(30)

# Fermeture de Pygame
pygame.quit()

   

 