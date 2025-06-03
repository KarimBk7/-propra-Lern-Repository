import sys

# Aufgabe A2
if not sys.flags.quiet:

	# Aufgabe A1
	print("sys.argv[...]:", sys.argv,"\n")

# Aufgabe A3
print("Meldung nach stderr: ", file=sys.stderr)

# Aufgabe A4
print("Aktuelle Python Version", str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro),"\n")

# Aufgabe A5
print(list(sys.modules.keys()),"\n")

# Aufgabe A6
print(sys.path, "\n")