import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Geometry Dash")

# Chargement de l'image de l'arrière-plan
background_img = pygame.image.load("background.png").convert()  # Assurez-vous que le chemin d'accès à l'image est correct

# Chargement de l'image du joueur
player_img = pygame.image.load("player.png").convert_alpha()

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

# Fonction pour afficher le score
def display_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    WINDOW.blit(score_text, (10, 10))

# Création des rectangles de collision pour le joueur et les obstacles
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
obstacle_rect1 = pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_height)
obstacle_rect2 = pygame.Rect(obstacle_x, obstacle_height + obstacle_gap, obstacle_width, WINDOW_HEIGHT - obstacle_height - obstacle_gap)

# Boucle principale du jeu
clock = pygame.time.Clock()
running = True
obstacle_passed = False  # Variable pour suivre si le joueur a passé un obstacle
while running:
    WINDOW.blit(background_img, (0, 0))  # Dessiner l'arrière-plan

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

    # Vérification si le joueur touche le sol
    if player_y + player_height >= WINDOW_HEIGHT:
        running = False  # Le joueur meurt s'il touche le sol

    # Mouvement de l'obstacle
    obstacle_x -= obstacle_velocity

    # Mise à jour des rectangles de collision
    player_rect.y = player_y
    obstacle_rect1.x = obstacle_x
    obstacle_rect2.x = obstacle_x

    # Gestion des collisions
    if player_rect.colliderect(obstacle_rect1) or player_rect.colliderect(obstacle_rect2):
        running = False

    # Gestion du score
    if obstacle_x + obstacle_width < player_x and not obstacle_passed:
        score += 1
        obstacle_passed = True

    # Affichage du joueur
    pygame.draw.rect(WINDOW, BLACK, player_rect)

    # Affichage de l'obstacle
    pygame.draw.rect(WINDOW, BLACK, obstacle_rect1)
    pygame.draw.rect(WINDOW, BLACK, obstacle_rect2)

    # Réinitialisation de l'obstacle lorsqu'il sort de l'écran
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WINDOW_WIDTH
        obstacle_height = random.randint(50, 300)
        obstacle_passed = False

    # Affichage du score
    display_score()

    pygame.display.update()
    clock.tick(30)

# Fermeture de Pygame
pygame.quit()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

   

 