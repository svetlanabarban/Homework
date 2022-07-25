# Exercise #1

# Create a program that will output everything in lowercase whatever the user will input. The program should run until the client enters the word “STOP”.

user_input = ("Please Enter words or sentences:")
print("", user_input.lower())
word=list()
while True:
  words=input("")
  if words == "STOP":
    break
  else:
    word.append(words)
print(": ")
for words in word:
  print(words.lower())


# Exercise #2

# You have a dictionary {'Jake': '$100K', 'Anand': '$120K'}. Using the string formatting print what salaries every person has.

data = {'Jake': '$100K', 'Anand': '$120K'}

emp_name = "Anand"
emp_sal = '$120K'

# option1
print("Employee Name is {0}, Salary is {1}.".format("Jake", '$100K'))
# option2
print("Employee Name is {1}, Salary is {0}.".format(emp_sal, emp_name))


# Exercise #3

# Given a 5 element tuple: (4, 30, 2017, 2, 27). Using the string formating print: '2 27 2017 4 30'
# Hint! use index numbers to specify positions.

tuple = ("4, 30, 2017, 2, 27")
print("{} , {}, {}, {}, {}, ".format(2, 27, 2017, 4, 30))

# First value
print(tuple[13])
# Second value
print(tuple[16:18])
# Third value
print(tuple[7:11])
# Fourth value
print(tuple[0])
# Fifth value
print(tuple[3:5])