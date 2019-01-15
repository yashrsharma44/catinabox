from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    # assert True
    cat2human = catmath.cat_years_to_hooman_years
    assert cat2human(10) == 50
    assert cat2human(8) == 40


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    # assert True
    cat2human = catmath.cat_years_to_hooman_years
    assert cat2human(0.8) == 4
    assert cat2human(0.6) == 3
    assert cat2human(0.4) == 2


def test__cat_years_to_hooman_years__0__returns_0():
    # assert True
    cat2human = catmath.cat_years_to_hooman_years
    assert cat2human(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2000) is True
    assert catmath.is_cat_leap_year(1500) is False
    assert catmath.is_cat_leap_year(1235) is False
