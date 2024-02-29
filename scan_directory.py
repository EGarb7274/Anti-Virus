import os
from file_corrupt import isFileCorrupt

def scanFiles(directory):
	for root, _, files in os.walk
		for file in files:
			file_path = os.path.join(root, file)
			print(file_path)
			if isFileCorrupt(file_path, signiture = b"\x89PNG\r\n\x1a\n"):
				print(file_path + "Is not corrupted")
			else:
				print(file_path + "File is corrupted")
		

if __name__ == "__main__":
	specified_folder = r""
	scanFiles(specified_folder)