
#Exercise #1
# with keyword arguments
def show_employee(name, salary):
    print("Steve" + salary)
#call function
show_employee(name = "Steve", salary = " 50000")


# with 2 positional arguments
def show_employee(name, salary):
    print(name, salary)
#call function
show_employee("Steve", 50000)


# with 1 positional argument
def show_employee(name, salary):
    print(name, salary)
#call function
show_employee("Steve", salary = "50000")


#Exercise #2
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)