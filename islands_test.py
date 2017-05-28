import islands
import unittest


class IslandTests(unittest.TestCase):
    def test_grid1_equals_1(self):
        grid = [[1]]
        self.assertEqual(islands.count_islands(grid), 1)

    def test_grid2_equals_0(self):
        grid = [[0]]
        self.assertEqual(islands.count_islands(grid), 0)

    def test_grid3_equals_1(self):
        grid = [[0, 1], [0, 1]]
        self.assertEqual(islands.count_islands(grid), 1)

    def test_grid4_equals_2(self):
        grid = [[1, 0, 1], [0, 0, 1]]
        self.assertEqual(islands.count_islands(grid), 2)

if __name__ == '__main__':
    unittest.main()