import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 10
ENEMY_SIZE = 50
ENEMY_SPEED = 10
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Player
player = pygame.image.load("D:/EnemyRain/a.png")
player = pygame.transform.scale(player, (PLAYER_SIZE, PLAYER_SIZE))
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE

# Enemies
enemies = []
enemy_spawn_counter = 0

# Score
score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    # Spawn enemies
    if enemy_spawn_counter == 60:
        enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])
        enemy_spawn_counter = 0

    # Move and remove enemies
    for enemy in enemies:
        enemy[1] += ENEMY_SPEED
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Check for collisions
    for enemy in enemies:
        if (
            player_x < enemy[0] + ENEMY_SIZE
            and player_x + PLAYER_SIZE > enemy[0]
            and player_y < enemy[1] + ENEMY_SIZE
            and player_y + PLAYER_SIZE > enemy[1]
        ):
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    screen.blit(player, (player_x, player_y))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), [enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE])

    # Update the display
    pygame.display.update()

    # Increase the score
    score += 1

    # Increase enemy spawn counter
    enemy_spawn_counter += 4

    # Set the frame rate
    clock.tick(60)

# Clean up and quit
pygame.quit("Game Over")