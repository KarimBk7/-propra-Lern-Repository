import requests
import sys
from charset_normalizer import from_bytes
import json

def do_get(url: str, searchstring: str):
	r = requests.get(url)
	print("Status: ",r.status_code)
	print("received ",len(r.text),"characters for ",r.url)
	
	# K1 charset normalizer
	detection = from_bytes(r.content).best()
	r.encoding = detection.encoding if detection else r.encoding


	print("Encoding: ", r.encoding)
	print("Headers:")
	for name, value in r.headers.items():
		if not (name.startswith("x-") or name.startswith("X-")):
			print("	", name+":	", value)

	print("search for",searchstring)
	search = r.text.find(searchstring)
	if search == -1:
		print("(not found)")
	else:
		for i in range(search, search+250):
			print(r.text[i],end="")
		print()


def do_post(url: str, jsontext: str):
	
	x = requests.post(url, jsontext)
	print("Status: ",x.status_code)
	result = json.dumps(x.json(), indent=4)
	print(result)
	


if __name__=="__main__":
	if sys.argv[1] == "do_get":
		#_, _, url, searchstring = sys.argv
		do_get(sys.argv[2], sys.argv[3])

	elif sys.argv[1] == "do_post":
		do_post(sys.argv[2], sys.argv[3])
