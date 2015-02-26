from math import cos, pi
from math import sin
from vector2D import Vector2D


class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self, *args, **kwargs):
        return str(self.a) + ' ' + str(self.b) + '\n' \
            + str(self.c) + ', ' + str(self.d)

    def __str__(self):
        return str(self.a) + ' ' + str(self.b) + '\n' \
            + str(self.c) + ', ' + str(self.d)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b \
            and self.c == other.c and self.d == self.d

    def dot(self, other):
        if type(other) is Matrix:
            return self.__matrix_product(other)
        if type(other) is Vector2D:
            return self.__vector_product(other)
        raise Exception("Product not defined for type " + str(type(other)))

    def __matrix_product(self, matrix):
        a = self.a * matrix.a + self.b * matrix.c
        b = self.a * matrix.b + self.b * matrix.d
        c = self.c * matrix.a + self.d * matrix.c
        d = self.c * matrix.b + self.d * matrix.d
        return Matrix(a, b, c, d)

    def __vector_product(self, vector):
        v1 = self.a * vector.x + self.b * vector.y
        v2 = self.c * vector.x + self.d * vector.y
        return Vector2D(v1, v2)

    @staticmethod
    def rotation_matrix(alpha):
        a = cos(alpha)
        b = sin(alpha)
        c = -sin(alpha)
        d = cos(alpha)
        return Matrix(a, b, c, d)

    @staticmethod
    def reflection_matrix(alpha):
        rotation = Matrix.rotation_matrix(alpha)
        rotation_inverse = Matrix.rotation_matrix(-alpha)
        reflection = Matrix(1, 0, 0, -1)
        return rotation_inverse.dot(reflection.dot(rotation))

import unittest


class MatrixTests(unittest.TestCase):
    def setUp(self):
        self.x = Vector2D(1, 0)
        self.y = Vector2D(0, 1)
        self.v1 = Vector2D(1, 1)
        self.v2 = Vector2D(1, 0)
        self.identity = Matrix(1, 0, 0, 1)
        self.matrix1 = Matrix(1, 1, 1, 1)
        self.matrix2 = Matrix(0, 1, 0, 1)

    def test_matrix_product(self):
        self.assertEqual(self.identity.dot(self.matrix1), self.matrix1)

    def test_vector_product(self):
        self.assertEqual(self.identity.dot(self.v1), self.v1)

    def test_rotation_matrix(self):
        self.assertEqual(Matrix.rotation_matrix(0), self.identity)

    def test_reflection_matrix(self):
        self.assertEqual(Matrix.reflection_matrix(0), Matrix(1, 0, 0, -1))

    def test_reflection(self):
        self.assertEqual(Matrix.reflection_matrix(pi / 4).dot(self.x), self.y)

if __name__ == '__main__':
    unittest.main()
