f = open("names.txt", "r")

names = []

for line in f:
	line = line.strip()
	names.append(line)

f.close()

print(names)
print(names)

for name in names:
	if name[0] == "T":
		print(name)
