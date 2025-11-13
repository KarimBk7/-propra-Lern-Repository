import sys
import random as rd
import hashlib
import subprocess
import pytest

def initrandom():
    return rd.seed(42)

def random_line() -> str:
	byte = rd.randbytes(4)
	digest = hashlib.sha512(byte).hexdigest()
	return digest + "\n"

def random_lines_generator(n: int) -> [str]:
	initrandom()
	collection = []
	for i in range(n):
		collection.append(random_line())
	return collection

def sorted_lines_generator_python(n: int) ->[str]:
	initrandom()
	return sorted(random_lines_generator(n))

def median(numlines: int, sorted_lines_iterator: [str]) -> str:
	initrandom()
	n = numlines
	ind = n // 2

	if ind > len(sorted_lines_iterator):
		Exception("Index Groesser als Liste! sorted_lines_generator_python()")

	for i, line in enumerate(sorted_lines_iterator):
		if i == ind:
			return line

def test_random_line():
    initrandom()
    assert random_line().endswith("2ed9f9\n")


def test_random_lines():
	initrandom()
	ls = random_lines_generator(4)
	assert ls[0].startswith("6e9a55")
	assert ls[3].endswith("0f757a\n")

'''
def test_median4():
    initrandom()
    res = median(4, sorted_lines_generator_python(4))
    assert res.startswith('72f436')
    assert res.endswith('d68c77\n')
'''

@pytest.mark.parametrize(
    "generator",
    [
    sorted_lines_generator_python(4),
    sorted_lines_generator_subprocess(4)
    ]
)

def test_median(generator):
	res = median(generator)
	assert res.startswith("72f436")
 	assert res.endswith("d68c77\n")


def sorted_lines_generator_subprocess(n: int) -> [str]:
	initrandom()
	proc = subprocess.Popen(
		["sort"],
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		text=True,
	)

	for line in random_lines_generator(n):
		proc.stdin.write(line)
	proc.stdin.close()

	res = []
	for line in proc.stdout:
		res.append(line)

	proc.stdout.close()
	proc.wait()
	return res

if __name__ == "__main__":
	n = int(sys.argv[2])
	if not isinstance(n, int):
		Exception("Second argument should be integer.")

	if sys.argv[1] == "local":
		print(median(n, sorted_lines_generator_python(n)))
	elif sys.argv[1] == "print":
		print(random_lines_generator(n))
	elif sys.argv[1] == "subprocess":
		print(sorted_lines_generator_subprocess(n))
	else:
		Exception("Invalid Argument: Use either 'local' or 'print'.")