#Create a new Python file in this folder called combined.py
#Create a text file called numbers1.txt that contains Integers which are sorted from smallest to largest.
#Create another text file called numbers2.txt which also contains Integers that are sorted from smallest to largest.
#Write the numbers from both files to a third file called all_numbers.txt
#All the numbers in all_numbers.txt should be sorted from smallest to largest.

#Open the first file in read mode
with open("numbers1.txt", "r") as file1:
    #Read all the lines from the file
    lines1 = file1.readlines()

#Open the second file in read mode
with open("numbers2.txt", "r") as file2:
    #Read all the lines from the file
    lines2 = file2.readlines()

#Convert the lines to integers and merge the two lists of lines
lines1 = [int(line) for line in lines1]
lines2 = [int(line) for line in lines2]
lines = lines1 + lines2

#Sort the list of lines
lines.sort()

#Open the third file in write mode
with open("all_numbers.txt", "w") as file3:
    #Write the sorted lines to the file
    file3.writelines([str(line) + "\n" for line in lines])

print("All numbers have been written to the file all_numbers.txt.")
