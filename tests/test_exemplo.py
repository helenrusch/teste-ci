def soma(a, b):
    return a + b

def test_soma_1():
    assert soma(1, 1) == 2

def test_soma_2():
    assert soma(2, 2) == 4

def test_soma_3():
    assert soma(0, 0) == 0

def test_soma_4():
    assert soma(-1, 1) == 0

def test_soma_5():
    assert soma(10, 5) == 15