import pygame
import subprocess

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)


# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game Menu")


# Function to draw text on the screen
def draw_text(text, size, x, y, color=WHITE, center=True):
    font = pygame.font.SysFont(None, size)
    rendered_text = font.render(text, True, color)
    if center:
        x -= rendered_text.get_width() // 2
    screen.blit(rendered_text, (x, y))

# Main menu function
def main_menu():
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        
        # Draw menu options
        draw_text("Welcome to Power Pong!", 50, WIDTH // 2, HEIGHT // 3)
        draw_text("1. Infinite Mode", 36, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("2. Timed Mode", 36, WIDTH // 2, HEIGHT // 2 + 50)
        draw_text("Press Q to Quit", 30, WIDTH // 2, HEIGHT - 100)
        
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Launch `mainpong.py`
                    subprocess.run(["python", "mainpong.py"])
                elif event.key == pygame.K_2:
                    # Launch `newpong.py`
                    subprocess.run(["python", "newpong.py"])
                elif event.key == pygame.K_q:
                    running = False

    pygame.quit()

# Run the menu
if __name__ == "__main__":
    main_menu()
