from typing import Dict, Tuple
import logging
logger = logging.getLogger(__name__)

SPEED = 1
TURN = 0.5


def get_motor_speeds(keys_pressed: Dict[str, bool]) -> Tuple[float, float]:
    left_speed = 0
    right_speed = 0
    for key, pressed in keys_pressed.items():
        if pressed:
            if key == 'up':
                left_speed += SPEED
                right_speed += SPEED
            elif key == 'down':
                left_speed -= SPEED
                right_speed -= SPEED
            elif key == 'left':
                left_speed -= TURN
                right_speed += TURN
            elif key == 'right':
                left_speed += TURN
                right_speed -= TURN
    return left_speed, right_speed
