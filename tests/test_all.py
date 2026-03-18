from math_graphics.vectors import Vector3

def test_cross():
    v1 = Vector3(1,0,0)
    v2 = Vector3(0,1,0)
    v3 = v1.cross(v2)
    assert (v3.x, v3.y, v3.z) == (0,0,1)