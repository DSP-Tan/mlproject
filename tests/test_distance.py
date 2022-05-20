from mlproject.distance import haversine

def test_type_of_haversine():
    assert type(haversine(2,2,1,1)) == float

def test_0_of_haversine():
    assert round(haversine(1,1,1,1),1) == 0.0

