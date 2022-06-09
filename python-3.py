primes_below = int(input("Enter number primes below : "))
sum = 0
for number in range(2, primes_below + 1):
    i = 1
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break
    if i is not number:
        sum = sum + number
        print(number, end = ' ')
print("\nThe sum of prime numbers in python from 1 to ", primes_below, " is :", sum)