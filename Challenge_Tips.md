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

## Methods

There are a ton of methods for strings. Learn them [here](https://www.w3schools.com/python/python_ref_string.asp) and keep this list handy.

Sometimes there's not a string method for what you want to do. In these cases, you can sometimes convert the string to a `List` and then use one or more list methods. Learn them [here](https://www.w3schools.com/python/python_ref_list.asp).

For example, there's not really a good method for counting the number of words in a string, so you split the string, like below:

```python
str = "Now is the time for all good men to come to the aid of their country."
# split() will default to " " (whitespace) as the 'delimeter', so you will get a `List` of words as the result
words = str.split()
# then you can use the len() function (not a method) to return the number of entries in the list
number_of_words = len(words)
# number of words will be 16

## Testing your code

If the program does not run, read the error message closely. It will usually tell you the line where the error is and what the problem is.
```
