# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    var_loop = int(input("How many times?"))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(var_loop):
       # Print each number in the range
       print(str (x+1))

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")