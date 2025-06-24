import random

# A1
random.seed(a="propra", version=2)

# A2
rd1 = random.randrange(-10,10)
print("[-10,10]:\t", rd1)

# A3
rd2 = [random.randrange(-1000,1000) for i in range(0,4)]
print("-1000..1000:\t", rd2)

# A4
rd3 = [random.gauss(10,3) for i in range(0,5)]
print("normalverteilt:\t, ", rd3)

# A5
seq = [i for i in range(0,len(rd3))]
random.shuffle(seq)
rd4 = [rd3[seq[i]] for i in range(0, len(rd3))]
print("permutiert:\t", rd4)

# A6
random.shuffle(seq)
rd5 = [rd4[seq[i]] for i in range(0,2)]
print("davon 2:", rd5)

# A7
def throw_dice(k,n):
	return random.choices(range(1,n+1),k=k)

# A8
print("Würfeln:\t", throw_dice(10,6))

	