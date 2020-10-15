
# takes no parameters and returns nothing
def doNothing():
  return

nothingResult = doNothing()
print(nothingResult)

# takes no parameters and returns "Monkey" no matter what
def getMonkey():
  return "Monkey"

monkey = getMonkey()
print(monkey)

# takes a parameter and returns a values based on that parameter
def getChildAge(child):
  child=child.lower();
  if child == "mimi":
    return 5
  elif child == "george":
    return 9
  elif child == "junior":
    return 14
  else:
    return "Invalid input"

age = getChildAge("Dickhead")
print(age)