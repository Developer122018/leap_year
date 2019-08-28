
'''
Rules
 year divided by 4 is leap
 year not exactly divisible by 4 is not leap
 year divisible by 100 is not leap
 year divisible by 400 is leap

'''

def _unusual_normal_year(p_year):
    return p_year % 100 == 0 and not p_year % 400 == 0

def _check_normal_leap_year(p_year):
    return p_year % 4 == 0

def is_leap(p_year):
    return not _unusual_normal_year(p_year) and  _check_normal_leap_year(p_year)


def test_normal_leap_year():
    assert is_leap(1996)

def test_non_leap_year():
    assert  not is_leap(1997)

def test_year_divisible_by_100_is_not_leap():
    assert not is_leap(1900)

def test_year_divisible_by_400_is_leap():
    assert is_leap(2000)