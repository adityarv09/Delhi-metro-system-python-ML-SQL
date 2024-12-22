import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock
clock = pygame.time.Clock()

# Ball position and velocity
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 5, 5

# Paddles position
player1_y = player2_y = (HEIGHT - PADDLE_HEIGHT) // 2
player1_score = player2_score = 0
PADDLE_SPEED = 6

def draw():
    screen.fill(BLACK)
    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (10, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # Draw scores
    font = pygame.font.Font(None, 74)
    text1 = font.render(str(player1_score), True, WHITE)
    text2 = font.render(str(player2_score), True, WHITE)
    screen.blit(text1, (WIDTH // 4, 20))
    screen.blit(text2, (WIDTH - WIDTH // 4, 20))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_x - BALL_RADIUS <= 20 and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT) or \
       (ball_x + BALL_RADIUS >= WIDTH - 20 and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x < 0:
        player2_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx
    if ball_x > WIDTH:
        player1_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx

    draw()
    clock.tick(FPS)
