# Question 1
# Problem: '15151515' is printed because the chairs variable is text instead of a number
# Solution: Convert the chairs variable from text to number
chairs = '15' # <- this is a string (text) rather than an int (number)
nails = 4
total_nails = int(chairs) * nails # <- convert string to int by wrapping it in the int() function
message = 'I need to buy {} nails'.format(total_nails)
print(message)

#my solution

nails = 4
chairs = 15
total_nails = nails * chairs
message = "I _need _to _buy" + str (total_nails) +"nails"
print(message)

# Question 2
# Problem: When the code is run, we get a error: 'NameError: name 'Penelope' is not defined'
#          this is because Python is interpreting Penelope as a variable, rather than a string
# Solution: To store text, it needs to be enclosed in either '{text}' or "{text}"
my_name = 'Penelope' # <- store the name as text by enclosing in single or double quotes
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#my solution
my_name = "Penelope"
my_age = 29
message = (my_name, my_age)
print(message)

# Question 3
# Task: I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
#       Write a program to calculate this.
#       Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
#       able to easily change these values if I want. The output should say something like "You can make 9
#       omelettes with 6 boxes of eggs".
boxes = 7
eggs_per_box = 6
eggs_per_omelette = 4
total_number_of_eggs = boxes * eggs_per_box
# Calculate whole number of omelettes
number_of_whole_omelettes = total_number_of_eggs // eggs_per_omelette
left_over_eggs = total_number_of_eggs % eggs_per_omelette
message = 'Using {} boxes of eggs, you can make {} whole omelettes, with {} eggs left over.'
print(message.format(boxes, number_of_whole_omelettes, left_over_eggs))
# Calculate number of omelettes (as a decimal)
number_of_decimal_omelettes = total_number_of_eggs / eggs_per_omelette
message = 'Using {} boxes of  eggs, you can make {} omelettes.'
print(message.format(boxes, number_of_decimal_omelettes))
