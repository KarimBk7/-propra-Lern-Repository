print("Hello World")

def get_permutations(string, i=0):
    res = []
    if i == len(string):
        res.append(string)
        
    for j in range(i, len(string)):
        chars = list(string)
        chars[i], chars[j] = chars[j], chars[i]
        res.extend(get_permutations("".join(chars), i + 1))
    return res

print(get_permutations("FUB"), end="\nHelloWorld\n")