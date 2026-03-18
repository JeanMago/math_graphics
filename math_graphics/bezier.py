from typing import Union

def bezier_curve(p0: Union['Vector2', 'Vector3'], 
                 p1: Union['Vector2', 'Vector3'], 
                 p2: Union['Vector2', 'Vector3'], 
                 p3: Union['Vector2', 'Vector3'], 
                 t: float) -> Union['Vector2', 'Vector3']:
    return (
        (1-t)**3 * p0 +
        3*(1-t)**2*t * p1 +
        3*(1-t)*t**2 * p2 +
        t**3 * p3
    )