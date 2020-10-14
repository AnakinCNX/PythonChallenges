# ask the user to name one olympic values
# better User experiece needed here
msg = input("name one ov:")
#if correctly name say that's correctly

# mind your spelling
# use lower(method on input to make sure that what the user enters will match these valse)

# You are assigning three things to ov
ov = 'respect'
ov = 'excllence'
ov = 'friendship'
# ov will be friendship at this point, as it's the last assignment

# what are you comparing?
# if msg = "respect" <== like this!

if ov == msg:
    print("That is correct")
else:
    print("that not correct")