import unittest
 
from area import calculate_total
 
def test_data01():
    result = calculate_total('a',50,60,100,120)
    assert result["roomtype"] == 1500
    assert result["calwater"] == 50
    assert result["calelect"] == 120
    assert result["price"] == 1670
    

def test_data02():
    result = calculate_total('b',100,120,200,250)
    assert result["roomtype"] == 2000
    assert result["calwater"] == 100
    assert result["calelect"] == 300
    assert result["price"] == 2400

def test_data03():
    result = calculate_total('c',100,130,210,250)
    assert result["roomtype"] == 500
    assert result["calwater"] == 150
    assert result["calelect"] == 240
    assert result["price"] == 890

def test_data04():
    result = calculate_total('a',0,0,0,0)
    assert result["roomtype"] == 1500
    assert result["calwater"] == 0
    assert result["calelect"] == 0
    assert result["price"] == 1500