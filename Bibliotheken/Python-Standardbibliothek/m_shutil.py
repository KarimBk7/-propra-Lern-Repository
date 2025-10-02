import os 
import stat
import shutil
import subprocess



workingdir = os.path.join(os.getcwd(),"m_shutil")
dst = os.path.join(workingdir, "destination")
src = os.path.join(workingdir, "sourcedir")


# A2
if os.path.isdir(dst):
	shutil.rmtree(dst)
os.mkdir(dst)



# A1
files = [os.path.join(src, "file1"), os.path.join(src, "dir", "a")]
for f in files: 

	mode = os.stat(f).st_mode
	os.chmod(f, mode | stat.S_IXUSR |stat.S_IXGRP | stat.S_IXOTH)


# A3 
file_name = "file1"
src_file = os.path.join(src, file_name)

shutil.copy(src_file, dst)

dst_file = os.path.join(dst, file_name)
result = subprocess.run(["bash", str(dst_file)])


# A4
file_name = "file2"

dst_file = os.path.join(dst, file_name)
src_file = os.path.join(src, file_name)

shutil.copyfile(src_file, dst_file)


# A5
src_file = os.path.join(dst, "file1")
dst_file = os.path.join(dst, "file2")

shutil.copymode(src_file, dst_file)

result = subprocess.run(["bash", str(dst_file)])


# A6
src_dir = os.path.join(src, "dir")
dst_dir = os.path.join(dst, "dir")
files = os.listdir(str(src_dir))

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for f in files:
	bedingung = True
	for n in numbers:
		if n in f:
			bedingung = False

	if bedingung:
		file_src = os.path.join(src_dir, f)
		file_dst = os.path.join(dst_dir, f)
		os.makedirs(os.path.dirname(file_dst), exist_ok=True)
		shutil.copy2(file_src, file_dst)


# A7
files = os.listdir(str(dst))

for f in files:
	file_src = os.path.join(dst, f)
	file_dst = os.path.join(dst_dir, f)

	if os.path.isfile(file_src):
		shutil.move(file_src, file_dst)


exe = os.path.join(dst_dir,"a")
result = subprocess.run(["bash", str(exe)])


# A8
dst_tar = str(os.path.join(dst_dir, "destination_dir"))
shutil.make_archive(dst_tar, "tar", dst_dir, ".")


# A9
unp_dir = os.path.join(dst, "unpacked")
os.mkdir(unp_dir)

dst_tar = dst_tar + ".tar"
shutil.unpack_archive(dst_tar, unp_dir, "tar")

exe = os.path.join(unp_dir,"a")
result = subprocess.run(["bash", str(exe)])

