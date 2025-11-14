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

def random_lines_generator(n: int):
	total_lines = 0

	for i in range(n):
		line = random_line()
		total_lines += len(line)
		
  
		if i % 200_000 == 0:
			mb = total_lines / (1024 * 1024)
			print(f"line {i}: {mb:.1f} MB total output", file=sys.stderr)

		yield line

def sorted_lines_generator_python(n: int):
	initrandom()

	lines = list(random_lines_generator(n))
	for line in sorted(lines):
		yield line

def median(numlines: int, sorted_lines_iterator: [str]) -> str:	
	n = numlines
	ind = n // 2
	count = 0

	for i, line in enumerate(sorted_lines_iterator):
		count += 1
  
		if count % 200_000 == 0:
			print("have read 200k lines", file=sys.stderr)
   
		if i == ind:
			return line


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

	for line in proc.stdout:
		yield line

	proc.stdout.close()
	proc.wait()

#-------------Tests----------------

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
	res = median(4, generator)
	assert res.startswith("72f436")
	assert res.endswith("d68c77\n")


#--------------------Main------------------

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Fehlende oder zu viele Argumente")
		sys.exit(1)

	mode = sys.argv[1]		
	n = int(sys.argv[2])
 
 
	if not isinstance(n, int):
		Exception("Second argument should be integer.")

	if mode == "local":
		print(median(n, sorted_lines_generator_python(n)))
	elif mode == "print":
		print(random_lines_generator(n))
	elif mode == "subprocess":
		print(sorted_lines_generator_subprocess(n))
	else:
		Exception("Invalid Argument: Use either 'local' or 'print'.")