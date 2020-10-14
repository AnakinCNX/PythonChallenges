#ask user name
# Remember to make your inputs nice for the user
# Use proper caps
# Use spaces at the end of the line
name = input("what is your name:")
subject = input("what is your fav subject:")
#print that u also like it
# Don't need "that"
msg = 'I also like that {} as well {}'
print(msg.format(subject, name))