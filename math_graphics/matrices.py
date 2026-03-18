from typing import List

def multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    if not A or not B or not B[0]:
        return []
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k]*B[k][j]
    return result


def mat4_identity() -> List[List[float]]:
    return [[1 if i==j else 0 for j in range(4)] for i in range(4)]