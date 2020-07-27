import pytest
from mylibs.HttpSender import HttpSender


class TestDemo2(HttpSender):
    datalist = ['xiaoming', 'xiaohong']

    @pytest.mark.parametrize('params', datalist)
    def test_a(self, params):
        print(params)
        assert 1


if __name__ == '__main__':
    pytest.main(['test_demo2.py'])