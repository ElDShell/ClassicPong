# Pong Game

This is a simple Pong game built using Pygame, featuring a collision detection system and sound effects. The game tracks player scores and will be expanded with new features in the near future.

## Features

- **Player Score Display**: There is a horizontal rule (HR) above the game screen displaying the scores of Player 1 and Player 2.
- **Ball Collision**: The ball changes direction when it touches the HR or the paddles.
- **Sound Effects**: A collision sound is played each time the ball hits the paddles, the HR, or the edges of the screen.

## Planned Features
- **AI Opponent**: Implement an AI opponent that can play against the user.
## How to Play

1. **Player 1** (Left Paddle): Use the `W` and `S` keys to move the paddle up and down.
2. **Player 2** (Right Paddle): Use the `UP` and `DOWN` arrow keys to control the right paddle.
3. The game continues as the ball bounces between the two paddles and the screen edges.
4. A player scores a point when the opposing player fails to hit the ball.
5. The scores are updated and displayed above the play area.

## Requirements

- Python 3.x
- Pygame

You can install Pygame using the following command:
```bash
pip install pygame