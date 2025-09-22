import os 
import stat
import shutil
import subprocess


home = os.path.expanduser("~")
ordner = os.path.join(home, "ws", "propra", "Bibliotheken", "Python-Standardbibliothek", "m_shutil")

# A2
path = os.path.join(ordner, "destination")
if os.path.isdir(path):
	shutil.rmtree(path)
	print("ordner gelöscht")
os.mkdir(path)


# A1
files = [os.path.join(ordner,"sourcedir", "file1"), os.path.join(ordner,"sourcedir", "dir", "a")]
for f in files: 

	mode = os.stat(f).st_mode
	os.chmod(f, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
	print(f"{f}: ist ausführbar.")


# A3 
f1 = os.path.join(ordner, "sourcedir", "file1")
f2 = os.path.join(ordner, "sourcedir", "file2")
shutil.copy2(f1, f2)
subprocess.run([f2], check=True)

shutil.copyfile(f2)
