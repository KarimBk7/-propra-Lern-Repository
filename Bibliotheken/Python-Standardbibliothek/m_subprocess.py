# A1
import subprocess

# A2 und A3
process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
ausgabe, _ = process.communicate()

# A4
liste = ausgabe.split(b"\n")
result = [i for i in liste if i.endswith(b"bash")]

# A5
print(result)