import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    # The key to understand this function is to draw several pairs of
    # rectangles and then focus ONLY on what you are looking for.
    if rectangles_are_intersected(R1, R2):
        x = max(R1.x, R2.x)
        y = max(R1.y, R2.y)
        width = min(R1.x + R1.width, R2.x + R2.width) - x
        height = min(R1.y + R1.height, R2.y + R2.height) - y
        return Rectangle(x, y, width, height)
    return Rectangle(0, 0, -1, -1)


def rectangles_are_intersected(r1: Rectangle, r2: Rectangle) -> bool:
    x_axis_condition_1 = r1.x + r1.width >= r2.x
    x_axis_condition_2 = r2.x + r2.width >= r1.x
    y_axis_condition_1 = r1.y + r1.height >= r2.y
    y_axis_condition_2 = r2.y + r2.height >= r1.y
    return (x_axis_condition_1 and
            x_axis_condition_2 and
            y_axis_condition_1 and
            y_axis_condition_2)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
