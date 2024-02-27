def isFileCorrupt(file_path, signiture):
	try:
		with open(file_path, "rb") as file:
			actual_signiture = file.read(len(signiture)
			return actual_signiture == signiture
	except FileNotFoundError:
		print(f"File not found: {file_path}")
	except Exception as e:
		print("Operation was not able to succeed")

if __name__ == "__main__":
	file_path = r""
	signiture = b"\x89PNG\r\n\x1a\n"
	if(isFileCorrupt(file_path, signiture)):
		print("file is not corruptted")
	else:
		print("file is corrupted")
