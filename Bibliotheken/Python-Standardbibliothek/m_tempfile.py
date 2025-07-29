import tempfile
import os

# A1
with tempfile.TemporaryDirectory(prefix="propra-") as dirr:
	print("path of temp dir:", dirr)

	# A2 
	print("OS standard temp dir:", tempfile.gettempdir())

	# A3
	with tempfile.NamedTemporaryFile(prefix="propra-", delete=False, dir=dirr) as tmp:
		print("temp file:", tmp.name)

		# A4
		with open(tmp.name, mode="w") as file:
			file.write("Das ist der Inhalt meiner temporaeren Datei.")
		
		# A5
		print("temp file exists after closing:", os.path.exists(tmp.name))

		# A6
		with open(tmp.name, mode="rb") as file:
			print("temp file content:", file.read())
	
	# A7
	print("temp file exists after with statement:", os.path.exists(tmp.name))

	# A8
	with tempfile.TemporaryFile(prefix="propra-") as utmp:
		print("unnamed temp file name:", utmp.name)

	# A9
	with tempfile.SpooledTemporaryFile(max_size=1000, mode="w") as stmp:
		print("spooled temp file name:", stmp.name)
		
		# A10
		text = 1000 * "ProPra"
		stmp.write(text)
		print("spooled temp file name after reaching 1KB size:", stmp.name)
	
# A11
print("temp dir exist after with statement:", os.path.exists(dirr))