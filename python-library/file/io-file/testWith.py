
# with open("test.txt", mode = "w", encoding = "utf-8") as f:
# 	f.write("my first file\n")
# 	f.write("this file\n\n")
# 	f.write("contains three lines\n")

f = open("test.txt", "r", encoding = "utf-8")
# print(f.read())			# string
# print(f.readline()) 	# string
# print(f.readlines()) 	# list
# for line in f:
# 	print(line, end = "")

# for line in f.readline():
# 	print(line)

f.close()