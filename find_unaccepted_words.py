file_path = input("File path: ")
s = input("Finding str: ")

with open(file_path, encoding = 'utf-8') as f:
	for line in f.readlines():
		if line.count(s):
			print(line[:line.find('<!--')], end='\n\n')

