#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import allure
import pytest

from test_calc.calc import Calc


@allure.feature("测试calc")
class TestClac:

    @pytest.fixture()
    @allure.story("实例化")
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b,answer', [(1, 1, 2), (-1, -1, -2), (0.1, 0.1, 0.2)])
    @allure.story("测试加法")
    def test_add(self, setup, a, b, answer):
        result = self.calc.add(a, b)
        print("答案：{0}".format(result))
        assert result == answer

    @pytest.mark.parametrize('a,b,answer', [(1, 0, 0), (-1, -1, 1), (0.4, 0.2, 2), (4, 2, 2)])
    @allure.story("测试除法")
    def test_div(self, setup, a, b, answer):
        try:
            result = self.calc.div(a, b)
            print("答案：{0}".format(result))
            assert result == answer

        except ZeroDivisionError as e:
            print(e.message)

    @pytest.mark.parametrize('a,b,answer', [(1, 1, 0), (-2, -1, -1), (0.2, 0.1, 0.1)])
    @allure.story("测试减法")
    def test_sub(self, setup, a, b, answer):
        result = self.calc.sub(a, b)
        print("答案：{0}".format(result))
        assert result == answer

    @pytest.mark.parametrize('a,b,answer', [(1, 1, 1), (-1, -1, 1), (0.1, 1, 0.1)])
    @allure.story("测试乘法")
    def test_mul(self, setup, a, b, answer):
        result = self.calc.mul(a, b)
        print("答案：{0}".format(result))
        assert result == answer


if __name__ == '__main__':
    pytest.main(['-vs', 'test01_calc.py'])
