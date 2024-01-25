import insem

def test_area():
    output = insem.area(2, 5)
    assert output == 10

def test_perimeter():
    output = insem.perimeter(2, 5)
    assert output == 14