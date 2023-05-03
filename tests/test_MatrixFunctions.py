from unittest import TestCase

from MatrixFunctions import dot_product, sub


class Test(TestCase):
    def test_dot_product(self):
        v3 = [1, 2]
        v4 = [3, 4, 5]
        try:
            dot_product(v3, v4)
            assert False
        except ValueError:
            pass

        m1 = [[1, 2], [3, 4]]
        m2 = [[5, 6], [7, 8]]
        assert dot_product(m1, m2) == [[19, 22], [43, 50]]
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        assert dot_product(v1, v2) == 32

        # invalid sizes
        m3 = [[1, 2, 3], [4, 5, 6]]
        m4 = [[1, 2], [3, 4]]
        try:
            dot_product(m3, m4)
            assert False
        except ValueError:
            pass

    def test_sub(self):
        t1 = [1]

        assert sub(t1, 1) == [0]

        t2 = [1, 1, 1, 1, 1]

        assert sub(t2, 2) == [-1, -1, -1, -1, -1]