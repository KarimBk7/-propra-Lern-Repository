import pytest
import blackbox as bb 


@pytest.mark.parametrize(
	"age,expected",
	[
		(0,"Child"), (6,"Child"), (12, "Child"),
		(13, "Teenager"), (15, "Teenager"), (19, "Teenager"),
		(20, "Adult"), (40, "Adult"), (64, "Adult"),
		(65, "Senior"), (90, "Senior"), (120, "Senior"),
		(121, "Invalid"), (160, "Invalid"),  (-124, "Invalid"), (-1, "Invalid")
	]
)
def test_age_category(age, expected):
    assert bb.age_category(age) == expected


@pytest.mark.parametrize(
	"income,expected",
	[
		(10000,0),
		(10001, 0.1), (50000, 4000),
		(50001, 4000.2), (100000, 14000),
		(120000, 20000)
	]
)
def test_tax(income, expected):
	assert bb.tax(income) == expected


@pytest.mark.parametrize(
	"age,income,credit_score,expected",
	[
		(17, 1000, 0, False),
		(18, 10000, 1000, False),
		(18, 30000, 700, True),
		(18, 30000, 699, False)
	]
)
def test_loan_eligibility(age, income, credit_score, expected):
    assert bb.loan_eligibility(age,income,credit_score) == expected

@pytest.mark.skip
@pytest.mark.parametrize(
    "alter, unfaelle, risikoberuf, jahresverdienst, expected",
    [
        (10, 0, False, 10000, 700),
        (40, 0, False, 20000, 475),
        (70, 3, True, 40000, 1260),

        (17, 0, False, 10000, 700),
        (18, 0, False, 10000, 600),
        (25, 0, False, 10000, 600),
        (26, 0, False, 10000, 500),
        (65, 0, False, 10000, 500),
        (66, 0, False, 10000, 700),

        (30, 0, False, 10000, 500),
        (30, 1, False, 10000, 650),
        (30, 2, False, 10000, 650),
        (30, 3, False, 10000, 900),

        (30, 0, False, 14999, 500),
        (30, 0, False, 15000, 475),
        (30, 0, False, 30000, 475),
        (30, 0, False, 30001, 450),

        (17, 3, True, 10000, 1400),
        (70, 3, True, 40000, 1260),
    ],
)
def test_insurance_buggy(alter, unfaelle, risikoberuf, jahresverdienst, expected):
    assert bb.insurance_buggy(alter, unfaelle,risikoberuf,jahresverdienst) == expected
    