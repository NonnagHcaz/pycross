
import unittest
from .context import pycross
# from .context.pycross_config import *

MIN_GRID_SIDE = 5
MAX_GRID_SIDE = 20
MIN_HIT_PERCENT = 0.4
MAX_HIT_PERCENT = 0.6


class PycrossTests(unittest.TestCase):
    def setUp(self):
        grid_width = 20
        grid_height = 20
        hit_percent = 0.5
        hit_value = 1
        miss_value = 0
        self.game = pycross.Pycross(
            grid_width, grid_height,
            hit_percent, hit_value, miss_value)

    def tearDown(self):
        pass

    def test_get_grid_width(self):
        self.assertTrue(self.game.grid_width == 20)

    def test_get_grid_height(self):
        self.assertTrue(self.game.grid_height == 20)

    def test_get_hit_percent(self):
        self.assertTrue(self.game.hit_percent == 0.5)

    def test_get_hit_value(self):
        self.assertTrue(self.game.hit_value == 1)

    def test_get_miss_value(self):
        self.assertTrue(self.game.miss_value == 0)

    def test_set_grid_width(self):
        self.game.grid_width = 10
        self.assertTrue(self.game.grid_width == 10)

    def test_set_grid_height(self):
        self.game.grid_height = 10
        self.assertTrue(self.game.grid_height == 10)

    def test_set_hit_percent(self):
        self.game.hit_percent = 0.6
        self.assertTrue(self.game.hit_percent == 0.6)

    def test_set_hit_percent_norm(self):
        self.game.hit_percent = 55
        self.assertTrue(self.game.hit_percent == 0.55)

    def test_set_hit_value(self):
        self.game.hit_value = 'a'
        self.assertTrue(self.game.hit_value == 'a')

    def test_set_miss_value(self):
        self.game.miss_value = 'b'
        self.assertTrue(self.game.miss_value == 'b')

    def test_set_grid_width_error_under(self):
        with self.assertRaises(ValueError):
            self.game.grid_width = 0

    def test_set_grid_height_error_under(self):
        with self.assertRaises(ValueError):
            self.game.grid_height = 0

    def test_set_hit_percent_error_under(self):
        with self.assertRaises(ValueError):
            self.game.hit_percent = 0

    def test_set_grid_width_error_over(self):
        with self.assertRaises(ValueError):
            self.game.grid_width = 100

    def test_set_grid_height_error_over(self):
        with self.assertRaises(ValueError):
            self.game.grid_height = 100

    def test_set_hit_percent_error_over(self):
        with self.assertRaises(ValueError):
            self.game.hit_percent = 101

    def test_set_grid_width_error_string(self):
        with self.assertRaises(TypeError):
            self.game.grid_width = '100'

    def test_set_grid_height_error_string(self):
        with self.assertRaises(TypeError):
            self.game.grid_height = '100'

    def test_set_hit_percent_error_string(self):
        with self.assertRaises(TypeError):
            self.game.hit_percent = '101'

    def test_generate_weighted_puzzle(self):
        puzzle = self.game.generate_puzzle(weighted=True)
        grid_size = self.game.grid_width * self.game.grid_height
        miss_count = sum([
            x.count(self.game.miss_value) for x in puzzle])

        self.assertTrue(
            (miss_count / grid_size >= MIN_HIT_PERCENT) and
            (miss_count / grid_size <= MAX_HIT_PERCENT))

    def test_generate_unqeighted_puzzle(self):
        self.game.generate_puzzle(weighted=False)

    # @unittest.skip
    # def test_get_(self):
    #     self.fail()
