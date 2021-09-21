# open a file read and write mode
open_file = open('file1.txt', 'r')

# write something into the file
#open_file.write("Write Something! Boss.\n")

# print successful message
print('file open Successfully')

# read a file and store data in variable
content = open_file.read()

# print the stored data
print(content)

# close the file
open_file.close()
