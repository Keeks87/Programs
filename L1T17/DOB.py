#Write a program that reads the data from the text file called DOB.txt and prints it out in
#two different sections in the format displayed below:
#Name
#Orville Wright
#Rogelio Holloway
#Marjorie Figueroa
#…etc
#Birthdate
#21 July 1988
#13 September 1988
#9 October 1988
#…etc

#Open file
with open("DOB.txt") as f:
    #Read the lines of the file into a list
    lines = f.readlines()

#Initialize lists to store names and birthdates
names = []
dates = []

# Iterate over the lines and add the name and birthdate to the appropriate list
for line in lines:
    name, surname, day, month, year = line.strip().split()
    full_name = name + " " + surname
    date = day + " " + month + " " + year
    names.append(full_name)
    dates.append(date)

#Print the names and dates
print("Name")
for name in names:
    print(name)
print("Birthdate")
for date in dates:
    print(date)

f.close()