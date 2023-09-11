# Import Library
import pygame

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# Initialize pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode((size))

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Main Program Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Drawing Code
    # Clear the screen to white. Don't put other drawing commands above this, or they will 
    # be erased with this command. 
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Update screen with what is drawn
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

pygame.quit()