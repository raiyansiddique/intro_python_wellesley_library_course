# Write a program that prints the numbers from 1 to 100, with a few exceptions.

#     If the number is divisible by 3, print "Fizz" instead of the number.
#     If the number is divisible by 5, print "Buzz" instead of the number.
#     If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

# So, the first few numbers would be:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz



i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
