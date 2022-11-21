"""
Создан 27.10.2022
Обучающий курс Python QA Engineer.
Домашняя работа №2. Unit-тесты класса Сircle
"""

import pytest

from src.Circle import Circle


def test_area():
    c = Circle(radius=5)
    assert c.area == 78.53981633974483


def test_perimeter():
    c = Circle(radius=5)
    assert c.perimeter == 31.41592653589793


def test_add_area_positive():
    c1 = Circle(radius=4)
    c2 = Circle(radius=7)
    assert c2.add_area(c1) == 204.20352248333654


def test_create_circle():
    circle = Circle(20)
    assert isinstance(circle, Circle)


@pytest.mark.parametrize("radius", [0, -2])
def test_create_circle_invalid_value(radius):
    try:
        Circle(radius)
    except ValueError as e:
        assert str(e) == f"Radius must be a positive value, not {radius}"


def test_check_add_area():
    circle_1 = Circle(20)
    area_1 = circle_1.area
    circle_2 = Circle(22)
    area_2 = circle_2.area
    assert circle_1.add_area(circle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [1, "text", int()])
def test_add_area_invalid(figure):
    try:
        circle = Circle(20)
        circle.add_area(figure)
    except ValueError as e:
        assert str(e) == "Object is not a geometry figure"
