"""
Math Graphics - Biblioteca profissional de matemática para computação gráfica.
"""

from .vectors import Vector2, Vector3
from .matrices import multiply, mat4_identity
from .transformations import translation_matrix, scale_matrix, rotation_z
from .projection import perspective_projection
from .bezier import bezier_curve

__all__ = [
    "Vector2",
    "Vector3",
    "multiply",
    "mat4_identity",
    "translation_matrix",
    "scale_matrix",
    "rotation_z",
    "perspective_projection",
    "bezier_curve",
]