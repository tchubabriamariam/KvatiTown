from typing import Tuple
import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    rows, cols = shape
    col_weights = np.linspace(1.0, 0.0, cols)
    row_weights = np.linspace(0.5, 1.0, rows)
    return np.outer(row_weights, col_weights) * 255.0
 
 
def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    rows, cols = shape
    col_weights = np.linspace(0.0, 1.0, cols)
    row_weights = np.linspace(0.5, 1.0, rows)
    return np.outer(row_weights, col_weights) * 255.0
