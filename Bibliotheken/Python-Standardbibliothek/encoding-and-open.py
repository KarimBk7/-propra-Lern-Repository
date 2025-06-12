
filenames = [f"encoding/datei{i+1}" for i in range(4)]
encodings = ['utf8', 'cp500', 'iso-8859-1', 'iso-8859-9', 'EBCDIC-CP-BE']

for file in filenames:
    for enc in encodings:
        #with open(file, mode="rt" ,errors="replace") as f:
        with open(file, mode="rb") as f:
            content = f.read()
            result = content.decode(enc, errors="replace")
        print(f"Date: {file} mit {enc}: {content}")

