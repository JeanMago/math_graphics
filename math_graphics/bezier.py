from typing import Union

def bezier_curve(p0: Union['Vector2', 'Vector3'], 
                 p1: Union['Vector2', 'Vector3'], 
                 p2: Union['Vector2', 'Vector3'], 
                 p3: Union['Vector2', 'Vector3'], 
                 t: float) -> Union['Vector2', 'Vector3']:
    """
    Calcula um ponto exato em uma curva de Bézier cúbica para um determinado parâmetro t.
    
    :param p0: Ponto inicial da curva.
    :param p1: Primeiro ponto de controle intermediário.
    :param p2: Segundo ponto de controle intermediário.
    :param p3: Ponto final da curva.
    :param t: Parâmetro de interpolação, variando de 0.0 (início) a 1.0 (fim).
    :return: Um novo vetor (Vector2 ou Vector3) com a posição calculada na curva.
    """
    return (
        (1-t)**3 * p0 +
        3*(1-t)**2*t * p1 +
        3*(1-t)*t**2 * p2 +
        t**3 * p3
    )