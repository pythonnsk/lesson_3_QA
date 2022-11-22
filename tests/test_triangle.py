"""
Создан 27.10.2022
Обучающий курс Python QA Engineer.
Домашняя работа №2. Unit-тесты класса Triangle
"""
import pytest

from src.Triangle import Triangle


def test_create_triangle():
    triangle = Triangle(2, 5, 6)
    assert isinstance(triangle, Triangle)


def test_check_perimeter():
    triangle = Triangle(10, 12, 14)
    perimeter = 10 + 12 + 14
    perimeter = round(perimeter, 2)
    assert triangle.perimeter == perimeter


def test_check_add_area():
    triangle_1 = Triangle(10, 18, 11)
    area_1 = triangle_1.area
    triangle_2 = Triangle(13, 14, 16)
    area_2 = triangle_2.area
    assert triangle_1.add_area(triangle_2) == area_1 + area_2


@pytest.mark.parametrize("figure", [20, "text", int()])
def test_add_area_invalid(figure):
    try:
        rectangle = Triangle(10, 15, 10)
        rectangle.add_area(figure)
    except ValueError as e:
        assert str(e) == "Object is not a geometry figure"
