import pytest


def func(x):
    return x + 1

@pytest.mark.flaky(reruns=3,reruns_delay=1)
def test_a():
    print('---test_a---')
    assert func(3) == 1111

@pytest.mark.flaky(reruns=3,reruns_delay=1)
def test_b():
    print('---test_b---')
    assert 1


if __name__ == '__main__':
    pytest.main([ 'test_demo.py'])
