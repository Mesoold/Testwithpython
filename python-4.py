n_number = int(input("How many number do you have? : "))
min = 200000000
max = -200000000
for i in range (n_number):
    number = int(input(""))
    if number < min:
        min = number
    if number > max:
        max = number
print("Your min number is {}".format(min))
print("Your max number is {}".format(max))
