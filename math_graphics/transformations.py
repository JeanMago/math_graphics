import math
from typing import List

def translation_matrix(tx: float, ty: float, tz: float) -> List[List[float]]:
    return [
        [1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0,1]
    ]

def scale_matrix(sx: float, sy: float, sz: float) -> List[List[float]]:
    return [
        [sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]
    ]

def rotation_z(angle: float) -> List[List[float]]:
    rad = math.radians(angle)
    return [
        [math.cos(rad), -math.sin(rad),0,0],
        [math.sin(rad), math.cos(rad),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]