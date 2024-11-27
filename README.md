---

# **PowerPong: Elevate Your Pong Experience with Strategic Power-Ups!**

PowerPong is a modern twist on the classic Pong game, built using Pygame. It introduces innovative gameplay elements such as strategic power-ups and downgrades, two exciting game modes, dynamic challenges, and customizable soundtracks, adding layers of complexity and fun to the traditional Pong mechanics.

---

## **Table of Contents**
1. [Features](#features)  
2. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
3. [Game Modes](#game-modes)  
4. [How to Play](#how-to-play)  
5. [Customization](#customization)  
6. [Contributing](#contributing)  
7. [License](#license)

---

## **Features**
- **Authentic Pong Mechanics**: Control your paddle with precision, bounce the ball, and aim to achieve a high score.
- **Two Unique Game Modes**:  
  - **Infinite Mode**: Play endlessly as long as you don’t lose all your lives.  
  - **Timed Mode**: Test your skills in a race against time with three challenging levels.
- **Strategic Power-Ups & Downgrades**:  
  - Enhance your paddle size or extend your timer with beneficial power-ups.  
  - Avoid downgrades that shrink your paddle or reduce the timer.
- **Pause and Restart Options**:  
  - Press `P` to pause the game. While paused, you can resume (`P`) or quit to the intro screen (`Q`).  
  - When the game ends, restart (`R`) or quit to the intro screen (`Q`).
- **Customizable Background**: Add a personalized touch by setting your favorite image as the background.
- **Background Music and Sound Effects**:  
  - Background music and soundtracks for key events (power-up collected, downgrade collected, and game over) are included and can be customized.
- **Performance Tracking**: Keep an eye on your score, remaining lives, and time during gameplay.
- **Simple and Intuitive Controls**: Play using only the arrow keys.

---

## **Getting Started**

### **Prerequisites**
Before running the game, ensure you have the following installed:
1. **Python** (3.6 or higher)  
   [Download Python here](https://www.python.org/downloads/).
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
   git clone https://github.com/AlvinNathey/graphics_miniproject.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd graphics_miniproject
   ```

3. **Run the Game**  
   Start the game by running:
   ```bash
   python startgame.py
   ```

---

## **Game Modes**

PowerPong offers two distinct game modes for different playstyles:

### **1. Infinite Mode**  
- **Objective**: Play endlessly while scoring as many points as possible.  
- **Mechanics**:  
  - Players begin with 3 lives. The game continues until all lives are lost.  
  - **Power-Ups**:  
    - **Green Rounded Power-Up**: Increases paddle size.  
    - **Yellow Cubed Power-Up**: Adds 3 points to your score.  
  - **Downgrades**:  
    - **Red Rounded Downgrade**: Shrinks paddle size.  
  - **Dynamic Difficulty**:  
    - After every 5 points scored, the ball's speed increases, making the game progressively harder.

---

### **2. Timed Mode**  
- **Objective**: Survive and score as many points as possible within a time limit.  
- **Levels**:  
  - **Easy**: 10-minute timer.  
  - **Medium**: 7-minute timer.  
  - **Hard**: 4-minute timer.  
- **Mechanics**:  
  - Timer adjusts dynamically with power-ups and downgrades:  
    - **Green Rounded Power-Up**: Adds 10 seconds to the timer.  
    - **Red Rounded Downgrade**: Subtracts 10 seconds from the timer.  
  - **Dynamic Difficulty**:  
    - After every 5 points scored, the ball's speed increases, adding an extra layer of challenge.  

---

## **How to Play**

### **Game Objective**  
Prevent the ball from passing your paddle while trying to score as many points as possible in your chosen game mode.

### **Controls**  
- **Move Left**: Press the `Left Arrow` key.  
- **Move Right**: Press the `Right Arrow` key.  
- **Pause/Unpause**: Press `P`.  

### **Game Over**  
- **Infinite Mode**: The game ends when all 3 lives are lost.  
- **Timed Mode**: The game ends when the timer runs out.  

At the end of the game, choose one of the following options:  
- **Restart**: Press `R` to restart the game.  
- **Quit**: Press `Q` to return to the intro screen.

---

## **Customization**

PowerPong allows for extensive customization:

### **1. Background and Screen**
- **Screen Dimensions**:
   ```python
   WIDTH = 800  # Set screen width
   HEIGHT = 600  # Set screen height
   ```
- **Background Image**: Replace the default background by setting the path to your preferred image:
   ```python
   BACKGROUND_IMAGE = "path/to/your/image.png"
   ```

### **2. Game Elements**
- **Paddle Size**:
   ```python
   PADDLE_WIDTH = 20  # Set paddle width
   PADDLE_HEIGHT = 100  # Set paddle height
   ```
- **Ball Size**:
   ```python
   BALL_RADIUS = 10  # Set ball radius
   ```
- **Colors**:
   - Paddle Color:
     ```python
     PADDLE_COLOR = (255, 255, 255)  # Set paddle color (RGB format)
     ```
   - Background Color (if no image is applied):
     ```python
     BACKGROUND_COLOR = (0, 0, 0)  # Set background color (RGB format)
     ```

### **3. Audio**
Customize audio by replacing the files in the `assets/` folder:
- **Background Music**: Replace `lofi.mp3` with your preferred track.  
- **Power-Up Sound**: Replace `coin.mp3` with your custom sound.  
- **Downgrade Sound**: Replace `wrong.mp3`.  
- **Game Over Sound**: Replace `gta.wav`.

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

Enjoy the thrill of PowerPong – where strategy meets reflexes! 🎮
