import pprint

# A1
fruits = ['apple', 'banana', 'blueberry', 'orange', 'peach', 'pear']
sorted_fruits = sorted(fruits, key=lambda x: x[::-1])
print("sorted by last letters:", sorted_fruits)


# A2
def choose_operator(word):
    word = word.lower()
    
    if word == "times":
        return (lambda x,y : x*y)
    elif word == "minus":
        return (lambda x,y : x-y)
    elif word == "divided by":
        return (lambda x,y : x/y)
    elif word == "plus":
        return (lambda x,y : x+y)


print("\n8 times 3 =", choose_operator("times")(8, 3))
print("10 minus 4 =", choose_operator("minus")(10, 4))
print("15 divided by 3 =", choose_operator("divided by")(15, 3))
print("9 plus 7 =", choose_operator("plus")(9, 7))


# A3
def generate_substrings(text: str, delimiter: str):
    tmp = ""
    for ch in text:
        if ch == delimiter:
            substr = tmp
            tmp = ""
            yield substr
        else:
            tmp = tmp + ch
    yield tmp
            
    
gen = generate_substrings("Generatoren sind sehr praktisch.", " ")
print("\nfirst three words:", list([next(gen) for _ in range(3)]))



# A4
numbers = list(range(10))
print("\ndivisible by 2", list(filter(lambda x : x%2==0, numbers)))
print("divisible by 7", list(filter(lambda x : x%7==0, numbers)))


# A5
alp = "abcdefghijklmnopqrstuvwxyzäüöß"
def positions_of_matching_words(text, condition):
    words = []
    word = ""
    is_word = False
    for ch in text:
        if ch.lower() in alp:
            word += ch
            is_word = True
        else:
            if is_word:
                words.append(word)
            word = ""
            is_word = False
            
    res = filter(lambda x: condition(x[1]), enumerate(words))
            
    return res

t = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore."
res = positions_of_matching_words(t, lambda x: 'y' in x)
print("\nposition of all words with letter 'y':", list(res))



# A6
prod = ["Laptop", "Smartphone", "Tablet", "Monitor"]
prices = [999.00, 599.59, 299.95, 199.99]
some_products = list(map(lambda x: dict(product = x[0], price = x[1]), zip(prod,prices)))
print("\nproducts with prices")
pprint.pp(some_products)


# A7 
def convert_currency(products, rate):
    for pr in products:
        pr["price"] = pr["price"] * rate
        yield pr


products_in_usd = convert_currency(some_products, 1.13)
p = next(products_in_usd)
print("\nThe", p["product"], "costs", p["price"], "USD")


# A8
stock = (4, 0, 1, 7)

def add_attributes(products, key, values):
     return list(map(lambda pair: {**pair[0], key: pair[1]}, zip(products, values)))
    
products_with_stock = add_attributes(some_products, "stock", stock)

print("product not in stock:", list(filter(lambda x : x["stock"] == 0 ,products_with_stock))[0])


i = 0
for prod in some_products:
    prod["stock"] = stock[i]
    i += 1
    
print(some_products)