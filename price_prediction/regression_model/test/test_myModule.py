from myModule import *
import pytest

@pytest.fixture
def input_value():
    return 8

def test_squre(input_value):
    #when 
    subject = squre(input_value)
    #then 
    assert subject == 64