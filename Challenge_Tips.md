# 🐍 Tips on how to approach challenges 🏋🏽

## Get organized

### Understand the challenge.

What is it asking you to do?

### Break it down

Think about how the challenge can be broken down into small pieces.

- What are the inputs?
- Are there more than one input? How many?
- What will you do to the inputs?
- What methods might help you do that?
- What is the output?

Write out the challenge steps using comments **before** you start to code. For example:

```python
# get user input and assign to variable X
# use lower method to prevent matching problems
# do validation on X if necessary

# get second input from user and assign it to Y
# do validation on Y if necessary

# use Y to modify X
# for example:  replace any occurance of input Y in input X

# print output
```

Under each comment write out what you think you'll code if you don't know what code you'll right yet. For example:

```python
# get user input and assign to variable X
X = input("Please enter a sentance: ").lower()
# do validation on X

# get second input from user and assign it to Y
# do validation on Y
# how can I do this?

# use Y to modify X
# are there any methods that might help me do this?  search the docs

# print output
```

## Testing your code

If the program does not run, read the error message closely. It will usually tell you the line where the error is and what the problem is.
