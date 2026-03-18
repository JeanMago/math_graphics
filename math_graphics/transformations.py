import math
from typing import List

def translation_matrix(tx: float, ty: float, tz: float) -> List[List[float]]:
    """
    Cria uma matriz de translação 4x4.
    
    :param tx: Deslocamento no eixo X.
    :param ty: Deslocamento no eixo Y.
    :param tz: Deslocamento no eixo Z.
    :return: Uma matriz 4x4 representando a translação.
    """
    return [
        [1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0,1]
    ]

def scale_matrix(sx: float, sy: float, sz: float) -> List[List[float]]:
    """
    Cria uma matriz de escala 4x4.
    
    :param sx: Fator de escala no eixo X.
    :param sy: Fator de escala no eixo Y.
    :param sz: Fator de escala no eixo Z.
    :return: Uma matriz 4x4 representando a escala.
    """
    return [
        [sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]
    ]

def rotation_z(angle: float) -> List[List[float]]:
    """
    Cria uma matriz de rotação 4x4 em torno do eixo Z.
    
    :param angle: O ângulo de rotação em graus.
    :return: Uma matriz 4x4 representando a rotação.
    """
    rad = math.radians(angle)
    return [
        [math.cos(rad), -math.sin(rad),0,0],
        [math.sin(rad), math.cos(rad),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ]