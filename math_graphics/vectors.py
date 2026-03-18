import math
from typing import List, Union

class Vector2:
    """
    Representa um vetor bidimensional (2D) com componentes x e y.
    Suporta operações matemáticas básicas como adição, subtração, multiplicação e divisão por escalar.
    """
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector2':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x / scalar, self.y / scalar)

    def dot(self, other: 'Vector2') -> float:
        """
        Calcula o produto escalar (dot product) entre este vetor e outro vetor 2D.
        """
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        """
        Calcula a magnitude (ou comprimento) do vetor.
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> 'Vector2':
        """
        Retorna um novo vetor normalizado (com magnitude igual a 1) na mesma direção.
        Se a magnitude do vetor original for 0, retorna um vetor nulo para evitar divisão por zero.
        """
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0.0, 0.0)
        return Vector2(self.x/mag, self.y/mag)

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"


class Vector3:
    """
    Representa um vetor tridimensional (3D) com componentes x, y e z.
    Suporta operações matemáticas básicas como adição, subtração, multiplicação e divisão por escalar.
    """
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> 'Vector3':
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> 'Vector3':
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other: 'Vector3') -> float:
        """
        Calcula o produto escalar (dot product) entre este vetor e outro vetor 3D.
        """
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other: 'Vector3') -> 'Vector3':
        """
        Calcula o produto vetorial (cross product) entre este vetor e outro vetor 3D.
        Retorna um novo vetor perpendicular a ambos os vetores originais.
        """
        return Vector3(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def magnitude(self) -> float:
        """
        Calcula a magnitude (ou comprimento) do vetor.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> 'Vector3':
        """
        Retorna um novo vetor normalizado (com magnitude igual a 1) na mesma direção.
        Se a magnitude do vetor original for 0, retorna um vetor nulo para evitar divisão por zero.
        """
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0.0, 0.0, 0.0)
        return Vector3(self.x/mag, self.y/mag, self.z/mag)

    def __repr__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"