# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for j in arg1[1:]:
        division /= j
    return division


@pytest.mark.parametrize("arg, result",
                         [
                                 pytest.param((-80, 10, 6), 1, marks=pytest.mark.skip("Пропуск теста")),
                                 pytest.param((1, 2, 1), 0.5, marks=pytest.mark.smoke),
                                 ((9, 3), 3.0),
                         ])
def test_1(arg, result):
    """ Проверка деления"""
    result_res = all_division(*arg)
    assert result == result_res

