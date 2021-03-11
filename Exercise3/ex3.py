"""
Numbers and Math
+ plus does addition
- minus does subtraction
/ slash does floating point division
// double-slash does integer division (this is specific to Python 3)
* asterisk does multiplication
% percent does remainder division
< less-than determines if a number is less than another number
> greater-than determines if a number is greater than another number
<= less-than-equal is less-than inclusive of the upper bound
>= greater-than-equal is greater-than inclusive of the upper bound
"""

print('I will now count my chickens:')

print('Hens', 25 + 30 // 6)
print('Roosters', 100 - 25 * 3 % 4)

print('Now I will count the eggs:')

print(3 + 2 + 1 - 5 + 4 % 2 - 1 // 4 + 6)

print('Is it true that 3 + 2 < 5 - 7?')

print(3 + 2 < 5 - 7)

print('What is 3 + 2?', 3 + 2)

print('What is 5 - 7?', 5 - 7)

print("Oh, that's why it's False.")

print('How about some more.')

print('Is it greater?', 5 > -2)
print('Is it greater or equal?', 5 >= -2)
print('Is it less or equal?', 5 <= -2)