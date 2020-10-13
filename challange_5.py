#ask user name
name = input("what is your name:")
subject = input(" what is your fav subject:")
#print that u also like it
msg = 'I also like that {} as well {}'
print(msg.format(subject, name))