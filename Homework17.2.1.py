# Exercise #1

# Assume you have the list xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#1 Write a loop that prints each of the numbers on a new line.

#2 Write a loop that prints each number and its square on a new line.

#3 Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.

#4 Print the product of all the numbers in the list. (product means all multiplied together)

xs =[12, 10, 32, 3, 66, 17, 42, 99, 20]

#1
print("Printing the numbers..")

for num in xs:
    print(num)

#2
print("Number and its square")

for num in xs:
    print(num, num ** 2)

#3
print("Printing the total:")

    total = 0
    for num in xs:
        total += num
    print("Total:", total)

#4
print("Printing the product:")

product = 1
for num in xs:
    product *= num
print("Product", product)
