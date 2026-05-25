from homeprice.calc import House


# initial test of House class
def test_init():
    house = House("Cambridge House", 2200)
    assert house.name is not None
    assert house.size > 100
