import math
from typing import List

def perspective_projection(fov: float, aspect: float, near: float, far: float) -> List[List[float]]:
    f = 1 / math.tan(math.radians(fov)/2)
    return [
        [f/aspect,0,0,0],
        [0,f,0,0],
        [0,0,(far+near)/(near-far),(2*far*near)/(near-far)],
        [0,0,-1,0]
    ]