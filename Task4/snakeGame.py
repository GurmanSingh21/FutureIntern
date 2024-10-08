import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set up display
WIDTH = 600
HEIGHT = 400
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock and snake settings
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Score: " + str(score), True, GREEN)
    dis.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLUE, [x[0], x[1], snake_block, snake_block])

# Message display function
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body list and initial length
    snake_list = []
    snake_length = 1

    # Random position for food
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            # Handling user input for replay or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handling key events for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Checking boundaries
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake's position
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        # Draw food
        pygame.draw.rect(dis, GREEN, [food_x, food_y, snake_block, snake_block])

        # Update snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        # Update the screen
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Set the speed of the snake
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
