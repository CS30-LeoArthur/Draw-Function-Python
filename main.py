# Import Library
import pygame

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)
PINK = (255, 100, 255)


def main():
    # Initialize pygame
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode((size))

    # platform function
    def draw_platforms(rect_x, rect_y, rect_width, rect_height, colour_1, colour_2):
        pygame.draw.rect(screen, colour_1, [rect_x, rect_y, rect_width, rect_height])
        pygame.draw.rect(screen, colour_2, [rect_x, rect_y + rect_height, rect_width, rect_height + 10])


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

        # Draw Platforms
        draw_platforms(400, 100, 200, 10, RED, GREEN)
        draw_platforms(250, 200, 100, 15, PURPLE, BLUE)
        draw_platforms(320, 300, 300, 5, BLACK, PINK)

        # Update screen with what is drawn
        pygame.display.flip()

        # Limit to 60 fps
        clock.tick(60)

    pygame.quit()



# Invoke main to begin program
if __name__ == "__main__":
    main()