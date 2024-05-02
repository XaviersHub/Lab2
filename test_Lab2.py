import Lab2 
import statistics

def test_min_max():
    lst = Lab2.find_min_max([12,34,54,23,43,65])
    testlst = [12,65]
    assert(lst == testlst)

def test_calc_avg():
    lst = Lab2.calc_average_temp([12,34,54,23,43,65])
    testlst = (12+34+54+23+43+65)/6
    assert(lst == testlst)

def test_calc_median():
    lst = Lab2.calc_median_temp([12,34,54,23,43,65])
    testlst = (34+43)/2
    assert(lst == testlst)