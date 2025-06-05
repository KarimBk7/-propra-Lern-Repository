import requests
import sys

def do_get(url: str, searchstring: str):
	r = requests.get(url)
	print("Status: ",r.status_code)
	print("received ",len(r.text),"characters for ",r.url)
	
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


if __name__=="__main__":
	if sys.argv[1] == "do_get":
		#_, _, url, searchstring = sys.argv
		do_get(sys.argv[2], sys.argv[3])

#do_get("https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/chapter-Basis.html","grundlegend")