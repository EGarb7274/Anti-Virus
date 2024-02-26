import os
def isFileMalicious(filePath, signiture):
	try:
		with open(filePath, "rb") as file:
			fileContent = file.read()
			if signiture in fileContent:
				return True
		return False
	except FileNotFoundError
		print("file not found")
		return False

if __name__ == "__main__":
	maliciousSigniture = b"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
	filePath = r"C:\Users\Evan\Downloads\eicarcom2.zip"

	if isFileMalicious(filePath, maliciousSigniture):
		print("Potentially malicious file")
	else:
		print("File free from virus")