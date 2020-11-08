# asks the user for the distance (in metres)

# the above says 'meters" and you are asking for cm...
cm = int(input("Please enter a distance in cm: "))

# asks the user for the time in seconds that a journey was completed in
time = int(input("Please enter the time will it take to reach there in seconds: "))

# calculates and outputs the average speed using a function

# I see no function here...

# You are looking to solve seconds per meter here.
# Think about your math, because the calculation below is incorrect.
# If if takes 10 seconds to move 10 meters, how many meters per second is what you are trying to solve for

print(cm, '/', time, '=', time/cm)
