"""
Создан 27.10.2022
Обучающий курс Python QA Engineer.
Домашняя работа №2. Unit-тесты класса Rectangle
"""
import pytest

from src.Rectangle import Rectangle


def test_create_rectangle():
    rectangle = Rectangle(20, 79)
    assert isinstance(rectangle, Rectangle)


def test_check_perimeter():
    rectangle = Rectangle(2, 4)
    perimeter = 2 * (2 + 4)
    assert rectangle.perimeter == perimeter


def test_check_area():
    rectangle = Rectangle(3, 5)
    area = 3 * 5
    assert rectangle.area == area


def test_check_add_area():
    rectangle_1 = Rectangle(2, 10)
    area_1 = rectangle_1.area
    rectangle_2 = Rectangle(20, 10)
    area_2 = rectangle_2.area
    assert rectangle_1.add_area(rectangle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [7, "text", int()])
def test_add_area_invalid(figure):
    try:
        rectangle = Rectangle(10, 30)
        rectangle.add_area(figure)
    except ValueError as e:
        assert str(e) == "Object is not a geometry figure"
