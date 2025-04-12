# Lab 09 - Enhanced Pygame Projects

This repository contains three enhanced pygame projects based on Lab08:

1. **Racer Game** - A car racing game with different coin weights and dynamic enemy speed
2. **Snake Game** - A snake game with different food weights and disappearing food
3. **Paint Application** - A drawing application with multiple shape tools

## Setup and Installation

1. Create a virtual environment:

   ```
   python3 -m venv .venv
   ```

2. Activate the virtual environment:

   ```
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```
   python3 -m pip install -r requirements.txt
   ```

## Running the Projects

### Racer Game

```
cd racer
python3 racer.py
```

#### Enhanced Features:

- **Different Coin Types**:
  - Bronze coins (60% probability, worth 1 point)
  - Silver coins (30% probability, worth 2 points)
  - Gold coins (10% probability, worth 5 points)
- **Dynamic Enemy Speed**: Enemy cars speed up after collecting a certain number of coins
- **Score Display**: Shows both score and current enemy speed

#### Controls:

- **Arrow Keys** - Move the car
- **Objective** - Avoid blue cars and collect colored coins

### Snake Game

```
cd snake
python3 snake.py
```

#### Enhanced Features:

- **Different Food Types**:
  - Regular food (70% probability, worth 1 point)
  - Bonus food (20% probability, worth 2 points)
  - Special food (10% probability, worth 5 points)
- **Disappearing Food**: Food disappears after 15 seconds if not eaten
  - Visual countdown timer appears when 5 seconds remain
  - Food blinks faster as time runs out
- **Different Food Shapes**: Each food type has a unique shape

#### Controls:

- **Arrow Keys** or **WASD** - Control the snake
- **R** - Restart game after game over
- **Q** - Quit game

### Paint Application

```
cd paint
python3 paint.py
```

#### Enhanced Features:

Four new shape tools added:

- **Square** - Draws a perfect square
- **Right Triangle** - Draws a right-angled triangle
- **Equilateral Triangle** - Draws an equilateral triangle
- **Rhombus** - Draws a diamond shape

#### Controls:

- **Mouse** - Draw shapes and use tools
- **C** - Clear canvas
- **S** - Save drawing as "painting.png"

## Project Structure

```
Lab09/
├── README.md
├── requirements.txt
├── racer/
│   ├── racer.py
│   └── assets/
├── snake/
│   ├── snake.py
│   └── assets/
└── paint/
    ├── paint.py
    └── assets/
```
