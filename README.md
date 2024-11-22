# PowerPong: Elevate Your Pong Experience with Strategic Power-Ups!

PowerPong is an advanced take on the classic Pong game, built using Pygame. This project introduces innovative gameplay elements, such as strategic power-ups and downgrades, adding a unique and challenging twist to the traditional Pong mechanics.

---

## **Table of Contents**
1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Customization](#customization)
5. [Contributing](#contributing)
6. [License](#license)

---

## **Features**
- **Authentic Pong Mechanics**: Control your paddle with precision, bounce the ball, and aim to score points.
- **Strategic Power-Ups & Downgrades**: 
  - Power-ups: Increase your paddle size for better control.
  - Downgrades: Decrease your paddle size for added challenge.
- **Performance Tracking**: Keep track of your score and remaining lives during the game.
- **Customizable Background**: Use your favorite image as the game’s background.
- **Clear Game Over Display**: Receive a notification when the game ends, encouraging you to try again.

---

## **Getting Started**

### **Prerequisites**
Before running the game, ensure you have the following installed:
1. **Python** (3.6 or higher)  
   [Download Python here](https://www.python.org/downloads/)
2. **Pygame** library  
   Install it via pip:
   ```bash
   pip install pygame
   ```

---

### **Installation**
Follow these steps to set up PowerPong on your local machine:

1. **Clone the Repository**  
   Use the command below to clone the repository:
   ```bash
   git clone https://github.com/DarynOngera/miniproj.git
   ```
   
2. **Navigate to the Project Directory**
   ```bash
   cd miniproj
   ```

3. **Run the Game**  
   Start the game by running:
   ```bash
   python startgame.py
   ```

---

## **How to Play**

1. **Game Objective**  
   Prevent the ball from passing your paddle while attempting to score against your opponent.

2. **Controls**  
   - Player 1 (Left Paddle):  
     - Move Left: `Arrow Left`  
     - Move Right: `Arrow Right`

3. **Power-Ups & Downgrades**  
   - **Power-Up**: Catch power-ups to increase your paddle size.
   - **Downgrade**: Avoid downgrades that shrink your paddle size.

4. **Game Over**  
   When one player loses all their lives, the game ends with a "Game Over" message.

---

## **Customization**

Personalize your PowerPong experience by modifying the constants in the `mainpong.py` or `newpong.py`file.

### Available Customizations:
1. **Screen Dimensions**
   ```python
   WIDTH = 800  # Set screen width
   HEIGHT = 600  # Set screen height
   ```

2. **Paddle Size**
   ```python
   PADDLE_WIDTH = 20  # Set paddle width
   PADDLE_HEIGHT = 100  # Set paddle height
   ```

3. **Ball Size**
   ```python
   BALL_RADIUS = 10  # Set ball radius
   ```

4. **Colors**
   - Paddle color:
     ```python
     PADDLE_COLOR = (255, 255, 255)  # Set paddle color (RGB format)
     ```
   - Background color (used if no image is applied):
     ```python
     BACKGROUND_COLOR = (0, 0, 0)  # Set background color (RGB format)
     ```

5. **Background Image**  
   Replace the background image by providing the path to your preferred image:
   ```python
   BACKGROUND_IMAGE = "path/to/your/image.png"
   ```

---

## **Contributing**

We welcome contributions from the community! Here’s how you can help:
1. **Report Bugs**  
   Identify and report any issues with the game.
2. **Suggest Features**  
   Share ideas for new power-ups, mechanics, or visual effects.
3. **Submit Code**  
   Fork the repository, make changes, and submit a pull request.

---

## **License**

This project is open-source and distributed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

---

With PowerPong, you get more than just a game – you get a dynamic experience that challenges your reflexes and strategic thinking. Install, play, and let the fun begin! 🎮