import math
import pytest

# A1 
def add(x,y):
	return x + y

def test_addition():
	assert add(1, 1)== 2 

def sqrt(x):
    return math.sqrt(x)
    
def test_sqrt():
	assert sqrt(10)**2 == pytest.approx(10)

def test_sqrt_of_negative_value():
	with pytest.raises(ValueError):
		sqrt(-1)