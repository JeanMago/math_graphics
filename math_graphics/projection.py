import math
from typing import List

def perspective_projection(fov: float, aspect: float, near: float, far: float) -> List[List[float]]:
    """
    Cria uma matriz de projeção perspectiva 4x4.
    
    :param fov: Campo de visão (Field of View) no eixo Y, em graus.
    :param aspect: Razão de aspecto (largura dividida pela altura) da tela.
    :param near: Distância até o plano de corte mais próximo (near clipping plane).
    :param far: Distância até o plano de corte mais distante (far clipping plane).
    :return: Uma matriz 4x4 representando a projeção perspectiva.
    """
    f = 1 / math.tan(math.radians(fov)/2)
    return [
        [f/aspect,0,0,0],
        [0,f,0,0],
        [0,0,(far+near)/(near-far),(2*far*near)/(near-far)],
        [0,0,-1,0]
    ]