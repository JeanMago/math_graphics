from typing import List

def multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiplica duas matrizes bidimensionais A e B.
    
    :param A: Primeira matriz.
    :param B: Segunda matriz.
    :return: Uma nova matriz resultante da multiplicação matricial de A por B. 
             Retorna uma lista vazia se as matrizes forem inválidas ou estiverem vazias.
    """
    if not A or not B or not B[0]:
        return []
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k]*B[k][j]
    return result


def mat4_identity() -> List[List[float]]:
    """
    Cria uma matriz identidade 4x4.
    
    :return: Uma lista de listas representando uma matriz identidade 4x4.
    """
    return [[1 if i==j else 0 for j in range(4)] for i in range(4)]