import pygame
import random
import math
import time  # For countdown delays

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
YELLOW = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Pong Game")

# Load background image
background_image = pygame.image.load("assets/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load sound for game over
game_over_sound = pygame.mixer.Sound("assets/gta.wav")

# Load new sounds
coin_sound = pygame.mixer.Sound("assets/coin.mp3")  # Coin collected sound
lofi_music = pygame.mixer.Sound("assets/lofi.mp3")  # Lo-fi music
wrong_sound = pygame.mixer.Sound("assets/wrong.mp3")  # Red ball collected sound

# Play lo-fi music in a loop until lives are lost
lofi_music.set_volume(0.3)  # Adjust volume if needed
lofi_music.play(loops=-1, maxtime=0)  # Infinite loop


class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 10)

    def collect(self):
        return 30  # Increase paddle width


class Downgrade:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), 10)

    def collect(self):
        return -30  # Decrease paddle width


class YellowSquare:
    def __init__(self, x, y, duration):
        self.x = x
        self.y = y
        self.size = 20
        self.spawn_time = pygame.time.get_ticks()
        self.duration = duration
        self.active = True

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.size, self.size))

    def is_expired(self):
        if pygame.time.get_ticks() - self.spawn_time > self.duration:
            self.active = False
        return not self.active

    def collect(self):
        self.active = False
        return 3  # Increase score by 3 points


class Ball:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = random.uniform(0.3, 0.8)
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


def game_over():
    global running
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_text("GAME OVER", 50, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Press R to Restart or Q to Quit", 36, WIDTH // 2, HEIGHT // 2 + 20)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False


def countdown():
    """Display a countdown before starting the game."""
    for i in range(3, 0, -1):
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background_image, (0, 0))
        draw_text(str(i), 100, WIDTH // 2, HEIGHT // 2)
        pygame.display.update()
        time.sleep(1)  # Pause for 1 second
    screen.fill(BACKGROUND_COLOR)
    screen.blit(background_image, (0, 0))
    draw_text("GO!", 100, WIDTH // 2, HEIGHT // 2, color=GREEN)
    pygame.display.update()
    time.sleep(1)


# Game variables
clock = pygame.time.Clock()
score = 0
level = 1
lives = 3
paused = False
game_over_played = False  # Flag to check if game over sound has been played

ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)
paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 10
paddle_width = PADDLE_WIDTH
paddle_height = PADDLE_HEIGHT

power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))
downgrade = Downgrade(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))
yellow_square = None

SCORE_THRESHOLD = 5
SPEED_INCREMENT = 1

# Start countdown
countdown()

# Game loop
running = True
while running:
    if not paused:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background_image, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True

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

        # Green power-up logic
        power_up.draw()
        if (
            ball.x - power_up.x < 15
            and ball.y - power_up.y < 15
            and abs(ball.x - power_up.x) < 20
            and abs(ball.y - power_up.y) < 20
        ):
            paddle_width += power_up.collect()
            coin_sound.play()  # Play coin sound when power-up is collected
            power_up = PowerUp(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))

        # Red downgrade logic
        downgrade.draw()
        if (
            ball.x - downgrade.x < 15
            and ball.y - downgrade.y < 15
            and abs(ball.x - downgrade.x) < 20
            and abs(ball.y - downgrade.y) < 20
        ):
            paddle_width += downgrade.collect()
            wrong_sound.play()  # Play wrong sound when downgrade is collected
            downgrade = Downgrade(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))

        # Yellow square logic
        if yellow_square is None and random.randint(1, 200) == 1:
            yellow_square = YellowSquare(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2), 5000)

        if yellow_square:
            yellow_square.draw()
            if yellow_square.is_expired():
                yellow_square = None
            elif (
                yellow_square.active
                and yellow_square.x < ball.x < yellow_square.x + yellow_square.size
                and yellow_square.y < ball.y < yellow_square.y + yellow_square.size
            ):
                score += yellow_square.collect()
                coin_sound.play()  # Play coin sound when yellow square is collected
                yellow_square = None

        # Update score and level
        if score >= SCORE_THRESHOLD * level:
            level += 1
            ball.speed += SPEED_INCREMENT
            ball.velocity_x *= 1.1
            ball.velocity_y *= 1.1

        draw_text(f"Score: {score}", 36, 10, 10, center=False)
        draw_text(f"Level: {level}", 36, WIDTH - 150, 10, center=False)
        draw_text(f"Lives: {lives}", 36, WIDTH // 2, 10)

        if ball.y >= HEIGHT - ball.radius:
            lives -= 1
            if lives <= 0:
                if not game_over_played:  # Play sound only once
                    game_over_sound.play()
                    game_over_played = True
                if not game_over():
                    running = False
                else:
                    score = 0
                    level = 1
                    lives = 3
                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)
            ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, 5)

    else:
        draw_text("PAUSED", 50, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Press P to Resume or Q to Quit", 36, WIDTH // 2, HEIGHT // 2 + 20)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                if event.key == pygame.K_q:
                    running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()


# Add this at the bottom of your existing script
def run():
    # Move your existing game loop into this function
    print("Starting Infinite Mode (Main Pong Game)")
    # Place the game loop code here

if __name__ == "__main__":
    run()  # If run directly, start the game

