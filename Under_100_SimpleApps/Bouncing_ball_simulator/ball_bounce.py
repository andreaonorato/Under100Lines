# This program shows the simulation of 5 balls bouncing under gravitational acceleration.
# It is also accompanied by elastic collision with the walls of the container.
# It is fun to watch.

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Setting screen size of pygame window to 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))

# Load background image
background = pygame.image.load('background-img.jpg')

# Adding title
pygame.display.set_caption('Ball Bounce Simulation')

class Ball:
    # Static variables for all Ball objects
    ball_image = pygame.image.load('ball.png')
    gravity = 1

    def __init__(self):
        # Initialize ball's velocity and position
        self.velocityX = 4
        self.velocityY = 4
        self.X = random.randint(0, 768)
        self.Y = random.randint(0, 350)

    def render_ball(self):
        """Render the ball on the screen"""
        screen.blit(Ball.ball_image, (self.X, self.Y))

    def move_ball(self):
        """Update the ball's position based on its velocity and handle collisions"""
        # Apply gravity to the y component of velocity
        self.velocityY += Ball.gravity

        # Update position based on velocity
        self.X += self.velocityX
        self.Y += self.velocityY

        # Collision with the walls leads to change in velocity
        if self.X < 0 or self.X > 768:
            self.velocityX *= -1
        if self.Y < 0 and self.velocityY < 0:
            self.velocityY *= -1
            self.Y = 0
        if self.Y > 568 and self.velocityY > 0:
            self.velocityY *= -1
            self.Y = 568

# List of balls created as objects
ball_list = [Ball() for _ in range(5)]

# The main program loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pause for a short duration to control the frame rate
    time.sleep(0.02)

    # Draw the background
    screen.blit(background, (0, 0))

    # Render and move each ball
    for ball_item in ball_list:
        ball_item.render_ball()
        ball_item.move_ball()

    # Update the display
    pygame.display.update()
