import pygame
import random  # Make sure this import is included
import math

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 15
PADDLE_HEIGHT = 20
PADDLE_WIDTH = 100
PADDLE_COLOR = (255, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timed Pong Game")

# Load background image
background_image = pygame.image.load("assets/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load sound for game over
game_over_sound = pygame.mixer.Sound("assets/gta.wav")

# Load new sounds
coin_sound = pygame.mixer.Sound("assets/coin.mp3")  # Coin collected sound
wrong_sound = pygame.mixer.Sound("assets/wrong.mp3")  # Red ball collected sound

# Load lofi music and set it to loop
pygame.mixer.music.load("assets/lofi.mp3")
pygame.mixer.music.set_volume(0.3)  # Adjust the volume as needed
pygame.mixer.music.play(-1, 0.0)  # Loop indefinitely

# PowerUp for increasing and decreasing time
class PowerUp:
    def __init__(self, x, y, time_change):
        self.x = x
        self.y = y
        self.time_change = time_change

    def draw(self):
        color = GREEN if self.time_change > 0 else RED
        pygame.draw.circle(screen, color, (self.x, self.y), 10)

    def collect(self):
        return self.time_change  # Change the time (positive or negative)


class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = random.uniform(0.3, 0.8)  # Random angle
        self.velocity_x = math.cos(self.angle) * self.speed
        self.velocity_y = math.sin(self.angle) * self.speed

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

    def check_paddle_collision(self, paddle_rect):
        global score
        future_y = self.y + self.velocity_y
        if (
            paddle_rect.colliderect(
                pygame.Rect(self.x - self.radius, future_y - self.radius, self.radius * 2, self.radius * 2)
            )
            and self.velocity_y > 0
        ):
            self.velocity_y = -abs(self.velocity_y)
            self.y = paddle_rect.top - self.radius
            score += 1  # Increment score when the ball hits the paddle

    def check_wall_collision(self):
        if self.x >= WIDTH - self.radius or self.x <= self.radius:
            self.velocity_x = -self.velocity_x
        if self.y <= self.radius:
            self.velocity_y = -self.velocity_y


def draw_text(text, size, x, y, color=WHITE, center=True):
    font = pygame.font.SysFont(None, size)
    rendered_text = font.render(text, True, color)
    if center:
        x -= rendered_text.get_width() // 2
    screen.blit(rendered_text, (x, y))


# Mode Selection Screen
def select_mode_screen():
    global timer_seconds  # Make sure the timer is accessible
    screen.fill(BACKGROUND_COLOR)
    draw_text("Select Game Mode", 60, WIDTH // 2, HEIGHT // 3, WHITE)

    draw_text("1. Easy (10 minutes)", 40, WIDTH // 2, HEIGHT // 2 - 20, WHITE)
    draw_text("2. Medium (7 minutes)", 40, WIDTH // 2, HEIGHT // 2 + 20, WHITE)
    draw_text("3. Hard (4 minutes)", 40, WIDTH // 2, HEIGHT // 2 + 60, WHITE)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # 10 minutes
                    timer_seconds = 10 * 60  # 10 minutes in seconds
                    waiting = False
                elif event.key == pygame.K_2:  # 7 minutes
                    timer_seconds = 7 * 60  # 7 minutes in seconds
                    waiting = False
                elif event.key == pygame.K_3:  # 4 minutes
                    timer_seconds = 4 * 60  # 4 minutes in seconds
                    waiting = False
    return timer_seconds


# Game over screen
def game_over_screen():
    global game_over_sound
    screen.fill(BACKGROUND_COLOR)
    draw_text("GAME OVER", 60, WIDTH // 2, HEIGHT // 3, WHITE)
    draw_text("Press R to Restart", 40, WIDTH // 2, HEIGHT // 2, WHITE)
    draw_text("Press Q to Quit", 40, WIDTH // 2, HEIGHT // 2 + 40, WHITE)
    pygame.display.update()

    game_over_sound.play()  # Play game over sound when time runs out

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    return True
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    return False


# Pause screen
def pause_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("PAUSED", 60, WIDTH // 2, HEIGHT // 3, WHITE)
    draw_text("Press P to Resume", 40, WIDTH // 2, HEIGHT // 2 - 20, WHITE)
    draw_text("Press Q to Quit", 40, WIDTH // 2, HEIGHT // 2 + 20, WHITE)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Resume the game
                    return True
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    return False


# Game variables
clock = pygame.time.Clock()
score = 0
lives = 3
timer_seconds = 10 * 60  # Default time (10 minutes in seconds)

ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
paddle_width = PADDLE_WIDTH
paddle_height = PADDLE_HEIGHT

# Initialize green and red power-ups
green_power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2), 10)  # 10 seconds added
red_power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2), -10)  # 10 seconds deducted

# Mode selection screen before starting the game
timer_seconds = select_mode_screen()  # Get the selected mode

# Game loop
running = True
paused = False  # Initialize the paused variable
start_ticks = pygame.time.get_ticks()  # Start the timer

while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(background_image, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause the game
                paused = True
            if event.key == pygame.K_q:  # Quit the game
                running = False

    if paused:
        if not pause_screen():  # If the user chooses to quit from the pause screen
            break
        paused = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 10
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 10

    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle_rect)

    # Ball update
    ball.check_wall_collision()
    ball.check_paddle_collision(paddle_rect)
    ball.move()
    ball.draw()

    # Power-ups logic (green and red)
    green_power_up.draw()
    if (
        ball.x - green_power_up.x < 15
        and ball.y - green_power_up.y < 15
        and abs(ball.x - green_power_up.x) < 20
        and abs(ball.y - green_power_up.y) < 20
    ):
        timer_seconds += green_power_up.collect()  # Increase time by 10 seconds
        coin_sound.play()  # Play coin sound when green power-up is collected
        green_power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2), 10)

    red_power_up.draw()
    if (
        ball.x - red_power_up.x < 15
        and ball.y - red_power_up.y < 15
        and abs(ball.x - red_power_up.x) < 20
        and abs(ball.y - red_power_up.y) < 20
    ):
        timer_seconds += red_power_up.collect()  # Decrease time by 10 seconds
        wrong_sound.play()  # Play wrong sound when red power-up is collected
        red_power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2), -10)

    # Check if the ball falls off the paddle (game over conditions)
    if ball.y >= HEIGHT:
        lives -= 1  # Lose a life
        if lives <= 0:  # Game over if no lives remain
            if not game_over_screen():  # Game over screen
                break
            score = 0  # Reset score
            lives = 3  # Reset lives
            timer_seconds = 10 * 60  # Reset time (10 minutes)
        else:  # Reset the ball and restart the timer
            ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)  # Reset ball position
            start_ticks = pygame.time.get_ticks()  # Restart the timer

    # Timer update (decreases based on real-world time)
    time_passed = (pygame.time.get_ticks() - start_ticks) / 1000  # Time in seconds
    remaining_time = timer_seconds - int(time_passed)

    if remaining_time <= 0:
        running = False  # End the game when time runs out

    # Display remaining time in seconds only (no minutes)
    draw_text(f"Time: {remaining_time}s", 36, WIDTH // 2, 10)

    # Display score
    draw_text(f"Score: {score}", 36, 10, 10, center=False)

    # Display lives in the top-right corner
    draw_text(f"Lives: {lives}", 36, WIDTH - 90, 10, color=WHITE, center=False)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

# Add this at the bottom of your existing script
def run():
    # Move your existing game loop into this function
    print("Starting Timed Mode (New Pong Game)")
    # Place the game loop code here

if __name__ == "__main__":
    run()  # If run directly, start the game

