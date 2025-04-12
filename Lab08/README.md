# Lab 08 - Pygame Projects

This repository contains three pygame projects:

1. **Racer Game** - A car racing game with coin collection
2. **Snake Game** - A snake game with levels and wall collisions
3. **Paint Application** - A drawing application with multiple tools

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

#### Controls:

- **Arrow Keys** - Move the car
- **Objective** - Avoid blue cars and collect yellow coins

### Snake Game

```
cd snake
python3 snake.py
```

#### Controls:

- **Arrow Keys** or **WASD** - Control the snake
- **R** - Restart game after game over
- **Q** - Quit game

#### Features:

- Wall collision detection
- Leveling system with increasing difficulty
- Score counter

### Paint Application

```
cd paint
python3 paint.py
```

#### Tools:

- **Pencil** - Free drawing
- **Rectangle** - Draw rectangles
- **Circle** - Draw circles
- **Eraser** - Erase drawings

#### Controls:

- **C** - Clear canvas
- **S** - Save drawing as "painting.png"

## Project Structure

```
Lab08/
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
