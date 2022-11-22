"""
Создан 27.10.2022
Обучающий курс Python QA Engineer.
Домашняя работа №2. Unit-тесты класса Square
"""
import pytest

from src.Square import Square


def test_create_square():
    square = Square(22)
    assert isinstance(square, Square)


def test_check_perimeter():
    square = Square(4)
    perimeter = 4 * 4
    assert square.perimeter == perimeter


def test_check_area():
    square = Square(4)
    area = 4 ** 2
    area = round(area, 2)
    assert square.area == area


def test_check_add_area():
    square_1 = Square(5)
    area_1 = square_1.area
    square_2 = Square(10)
    area_2 = square_2.area
    assert square_1.add_area(square_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [20, "text", int()])
def test_add_area(figure):
    try:
        square = Square(6)
        square.add_area(figure)
    except ValueError as e:
        assert str(e) == "Object is not a geometry figure"
