from app.src.calculator import Calculator
cal=Calculator()
def test_add():
    assert cal.add(1,1)==2
    assert cal.add(1,2)==3
def test_subtract():

    assert cal.subtract(4,1)==3

    assert cal.subtract(2,1)==1
def test_multiply():
    assert cal.multiply(1,2)==2	
    assert cal.multiply(2,3)==6
