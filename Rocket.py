# Exercise #2

# Write a class Rocket - a simulator for a rocket ship in a game. The __init__() method doesn't take any arguments but sets the x and y positions to zero.

# Rocket class has 5 methods:

#move_up() - will increment y position by 1
#move_right() - will increment x position by 1
#mode_down() - will decrement y position by 1
#move_left() - will decrement x position by 1
#current_postition() - will print the  current position of the Rocket

class Rocket():

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the parameters given.
        # Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        self.x -= x_decrement
        self.y -= y_decrement

    def move_up(self):
        self.y += 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def current_position(self):
        curent_position

my_rocket = Rocket()
print("current_position:", my_rocket)

my_rocket.move_up()
print("current_position:", my_rocket)

my_rocket.move_right()
print("current_position:", my_rocket)

my_rocket.move_down()
print("current_position:", my_rocket)

my_rocket.move_left()
print("current_position:", my_rocket)