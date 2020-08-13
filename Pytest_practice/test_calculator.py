import yaml

from Hogwarts.Pytest_practice.calculator import Calculator
import pytest


def read_data(path):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        cal_data = data['add']['datas']
        cal_ids = data['add']['ids']
    return [cal_data, cal_ids]


class Test_Calculator:

    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,ex", read_data('./test_data/test_add.yml')[0],
                             ids=read_data('./test_data/test_add.yml')[1])
    def test_add(self, a, b, ex):
        sum_resault = self.cal.add(a, b)
        assert sum_resault == ex

    @pytest.mark.sub
    @pytest.mark.parametrize("a,b,ex", read_data('./test_data/test_sub.yml')[0],
                             ids=read_data('./test_data/test_add.yml')[1])
    def test_sub(self, a, b, ex):
        sum_resault = self.cal.sub(a, b)
        assert sum_resault == ex

    @pytest.mark.mul
    @pytest.mark.parametrize("a,b,ex", read_data('./test_data/test_mul.yml')[0],
                             ids=read_data('./test_data/test_add.yml')[1])
    def test_mul(self, a, b, ex):
        sum_resault = self.cal.mul(a, b)
        assert sum_resault == ex

    @pytest.mark.div
    @pytest.mark.parametrize("a,b,ex", read_data('./test_data/test_div.yml')[0],
                             ids=read_data('./test_data/test_add.yml')[1])
    def test_div(self, a, b, ex):
        sum_resault = self.cal.div(a, b)
        assert sum_resault == ex

    def test_diverror(self):
        with pytest.raises(ZeroDivisionError) as err_info:
            self.cal.div(10, 0)
            print(err_info.type)
