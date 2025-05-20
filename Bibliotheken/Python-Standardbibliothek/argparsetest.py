import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", help="quadriert zahl", default="argparse.config")
parser.add_argument("-m", "--maxdepth", "--depth", help ="echo is string", type=int, default=1)
parser.add_argument("-b", "--batch", help="Batch file", nargs='+', type=str)

args = parser.parse_args()

datei = open(args.config,'r')
print(datei.read())

print(f"\nMaxdepth ist {args.maxdepth}\n")

if args.batch:
	print("Batch-Files:")
	for file in args.batch:
		print(file)

