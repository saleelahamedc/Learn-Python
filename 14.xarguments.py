# Q1 - how can i collect all arguments into a single parameter(single variable)? (answer = prefix with *)
# Q2 - What is tuple? (something like a list)
# Q3 - A function need a ____ statement to have an output, otherwise by default a function emits none value (answer= return)

# make a function which can take many numbers and multiply together

# to make a new function we have to write def (definition short)
# find our purpose
# to multiply infinite number of arguments
# so we will make a function named multiply
# inside the multiple function parathesis we have to write as (*numbers) anything can be written after the * cause it is like a variable
# so now we have *numbers as list
# we can use a loop to go through each element from the list
# the element should be multiplied each time and store it to variable

def multiply(*numbers):
    answer = 1
    for no_to_multiply in numbers:
        answer = answer * no_to_multiply
    return answer


print(multiply(10, 20, 30))


letters = ["a", "b"],

letters = [(0, "a"), (1, "b")]
