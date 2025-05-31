import argparse_subcommand as ap_sub
import os
import glob
import datetime

meaning = "some help text for the subcommand"

def add_arguments(parser: ap_sub.ArgumentParser): 
	parser.add_argument("-age", "--age", help="maxage", default="48")
	parser.add_argument("file", nargs="+", help="List of files")

def execute(args: ap_sub.Namespace): 

	zahl = "" 
	einheit = ""
	for i in args.age:			# finde einheit und zahl aus args.age heraus
		if i.isdigit():
			zahl += i
		else:
			einheit += i
	zahl = int(zahl)

	limit=0
	if einheit == "d":			# bestimme limit anhang einheit
		limit = datetime.datetime.now() - datetime.timedelta(days=zahl)
	elif einheit == "h":
		limit = datetime.datetime.now() - datetime.timedelta(hours=zahl)
	elif einheit == "m":
		limit = datetime.datetime.now() - datetime.timedelta(minutes=zahl)
	elif einheit == "s":
		limit = datetime.datetime.now() - datetime.timedelta(seconds=zahl)
	else:
		Exception("Error (lsnew): Invalid age parameter. Use 'number(d,h,m,s)' instead.")



	files = []
	for x in args.file:
		file = glob.glob(x)
		if not (file == []):				# falls es kein einziges file gefunden wurde
			if not (file[0] in files):		# schaut ob file nicht bereits gespeichert wurde

				mtime = datetime.datetime.fromtimestamp(os.stat(file[0]).st_mtime)		# mtime

				if mtime > limit:			# teste ob mtime nicht älter als args.age ist
					mtime = mtime.strftime("%Y-%m-%d %H:%M:%S")							# umwandeln in zeitstempel
					files.append((mtime,file[0]))
					print(f"{mtime:<20}  {file[0]:>10}")
