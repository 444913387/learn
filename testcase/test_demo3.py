import pytest
from mylibs.HttpSender import HttpSender


class Test_demo3(HttpSender):
    data_list = [('xiaoming', '123456'), ('xiaohong', '88888888')]

    @pytest.mark.parametrize(('username', 'password'), data_list)
    def test_xx(self, username, password):
        print(username, password)
        assert 1


if __name__ == '__main__':
    pytest.main(['test_demo3.py'])
