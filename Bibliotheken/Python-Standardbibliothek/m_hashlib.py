import hashlib

# A1
print(hashlib.algorithms_available)


# A2
h = hashlib.new("sha256")


# A3
h.update(b"ProPra")
pp = h.hexdigest()
print("1. ProPra SHA-256:\t", pp)


# A4
h = hashlib.new("sha256")
h.update(b"ProPra ")
pp_ = h.hexdigest()
print("2. added a space:\t", pp_)


# A5
def compare(h1, h2):
	found = 0
	for i, j in zip(pp, pp_) :
		if i == j:
			found += 1
	return found

expected = 64 * (1/16)  # Hash erstellt 64 Hex-Zeichen und Hexadezimal hat 16 verschiedene Zeichen
print("3. identical digits: expected: ", expected , "; found: ", compare(pp, pp_))


# A6
h2 = hashlib.new("sha256")
h2.update(b"ProPra FU Berlin")
h.update(b"FU Berlin")			# Aktuell "ProPra "
print("4. u(a); u(b) = u(a + b):\t", h.hexdigest() == h2.hexdigest())


# A8
with open("m_hashlib.txt", mode="rb") as f:
    content = f.read()

h3 = hashlib.new("sha256")
h3.update(b""+content) 
print("5. file checksum:\t", h3.hexdigest())
