import pytest

def smallest_letter_and_digit(input: str) -> tuple[str | None, int | None]:
	min_dig = None
	min_let = None
    
	for i in input:
        
		if i.islower() and not i in {'ä','ü','ö'}:
			if min_let == None or i < min_let:
				min_let = i 

		else: 
			try:
				if min_dig == None or int(i) < min_dig:
					min_dig = int(i)
			except:
				continue

	return (min_let, min_dig)


@pytest.mark.parametrize("input,letter,digit", [("ä", None, None), ("321gc", "c", 1), ("äüöz","z", None), ("9876543210", None, 0)])
def test_smallest_letter_and_digit(input, letter, digit):
    result = smallest_letter_and_digit(input)
    assert result[0] == letter and result[1] == digit