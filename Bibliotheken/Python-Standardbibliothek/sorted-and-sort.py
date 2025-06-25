import operator

what = "Tupel von Alter, Gewicht, Körpergröße"
data = [
    (22, 69, 177,), 
    (22, 71, 172,), 
    (48, 72, 174,), 
    (38, 89, 179,), 
    (71, 59, 170,), 
]

# A3
def height(tuple):
	return tuple[2]


# A5
def excess_weight(tuple):
	return tuple[2] - tuple[1]


# A6
class MyTuple(tuple):

	def __lt__(self, other: 'MyTuple') -> bool:
		if not self.is_big and other.is_big:
			return True
		else: 
			return tuple(self) < tuple(other)


	@property
	def is_big(self) -> bool:
		return self[2] > 172

data2 = [MyTuple(t) for t in data]


print(what)
print(data)
print("Sortiert:")
print(sorted(data))  # Schritt 1
print("Sortiert nach Körpergröße 1:")
print(sorted(data,key=height))  # Schritt 2
print("Sortiert nach Körpergröße 2:")
print(sorted(data,key=operator.itemgetter(2)))  # Schritt 3
print("Sortiert nach Übergewicht:")
print(sorted(data, key=excess_weight))  # Schritt 4
print("Sortiert in Gewichtsgruppen:")
print(sorted(data2))  # Schritt 5