'''

Problem: FizzBuzz Variation

Write a function that prints the numbers from 1 to n. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

'''


def Fizz_Buzz(n):
    for i in range(1, n):
        if  i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i %3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Bizz")

        else:
            print(i)


Fizz_Buzz(20)
