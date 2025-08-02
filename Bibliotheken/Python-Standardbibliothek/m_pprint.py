import json
import pprint

# A1
with open("m_pprint.json", mode="r") as fl:
	data = json.load(fl)

# A2
print("pretty print:")
pprint.pp(data)


# A3
pp = pprint.PrettyPrinter(indent=4, depth=2, sort_dicts=False)

# A4
print("\nwith PrettyPrinter object:")
pp.pprint(data[1])
pp.pprint(data[3])