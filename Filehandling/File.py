

#print(file.readline()) first line only
#print(file.readline()) seconf line only  line by line reading

# file = open('Filehandling/info.txt', 'w')
# print(file.write("hello"))
# file.close()

# file = open('Filehandling/info.txt', 'r')
# print(file.read())
# file.close()


file = open('Filehandling/info.txt', 'a')
append = file.write('bye')
print(append)
file.close()


file = open('Filehandling/info.txt', 'r')
print(file.read())
file.close()



#relative  same python folder
#absolitive path

#file.read()
#file.readline()
#print(file.readlines())