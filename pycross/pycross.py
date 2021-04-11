import numbers
import random

try:
    from .config import *
except ImportError:
    from config import *


class Pycross:

    def __init__(
            self, grid_width, grid_height,
            hit_percent=0.6, hit_value=1, miss_value=0):
        assert miss_value != hit_value
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.hit_percent = hit_percent
        self.hit_value = hit_value
        self.miss_value = miss_value

    @property
    def grid_width(self):
        return self._grid_width

    @grid_width.setter
    def grid_width(self, grid_width):
        validate_grid_size(grid_width, 'grid_width')
        self._grid_width = int(grid_width)

    @property
    def grid_height(self):
        return self._grid_height

    @grid_height.setter
    def grid_height(self, grid_height):
        validate_grid_size(grid_height, 'grid_height')
        self._grid_height = int(grid_height)

    @property
    def hit_percent(self):
        return self._hit_percent

    @hit_percent.setter
    def hit_percent(self, hit_percent):
        validate_hit_percent(hit_percent, 'hit_percent')
        if hit_percent > 1:
            hit_percent = hit_percent / 100
        self._hit_percent = hit_percent

    @property
    def hit_value(self):
        return self._hit_value

    @hit_value.setter
    def hit_value(self, hit_value):
        # TODO: assert mis/hit values are not equal
        # assert self._miss_value != hit_value
        self._hit_value = hit_value

    @property
    def miss_value(self):
        return self._miss_value

    @miss_value.setter
    def miss_value(self, miss_value):
        # TODO: assert mis/hit values are not equal
        # assert self._hit_value != miss_value
        self._miss_value = miss_value

    def generate_puzzle(self, weighted=True):
        if weighted:
            return self.generate_weighted_puzzle()
        return self.generate_unweighted_puzzle()

    def generate_weighted_puzzle(self):

        generations = 0
        while True:
            puzzle = self.generate_unweighted_puzzle()
            generations += 1
            grid_size = self._grid_width * self._grid_height
            miss_count = sum([
                x.count(self._miss_value) for x in puzzle])

            if (
                    (miss_count / grid_size >= MIN_HIT_PERCENT) and
                    (miss_count / grid_size <= MAX_HIT_PERCENT)):
                break

        print('Puzzle generated after {} generations.'.format(generations))

        return puzzle

    def generate_unweighted_puzzle(self):
        return [
            [
                random.choice([self._hit_value, self._miss_value])
                for x in range(self._grid_width)]
            for y in range(self._grid_height)]


def _validate(value, tag, min_value, max_value):
    if not isinstance(value, numbers.Number):
        raise TypeError(
            'Variable {} must be a number: {}'.format(
                tag, value))

    if value < 1:
        value = value * 100

    if int(value) < min_value:
        raise ValueError(
            'Variable {} must be {} or greater: {}'.format(
                tag, min_value, value))

    if int(value) > max_value:
        raise ValueError(
            'Variable {} must be {} or less: {}'.format(
                tag, max_value, value))

    return True


def validate_grid_size(value, tag):
    return _validate(value, tag, MIN_GRID_SIDE, MAX_GRID_SIDE)


def validate_hit_percent(value, tag):
    return _validate(value, tag, MIN_HIT_PERCENT*100, MAX_HIT_PERCENT*100)


if __name__ == '__main__':
    game = Pycross(20, 20, 0.6, u'\u2588', ' ')
    # game.miss_value = u'\u2588'
    puzzle = game.generate_puzzle()
    for x in puzzle:
        print(''.join(x))
