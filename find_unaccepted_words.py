file_path = input("File path: ")
s = input("Finding str: ")

with open(file_path):
	for line in file_path.read_lines():
		if line.count(s):
			print(line)
		elif line == '\n':
			print(line)

