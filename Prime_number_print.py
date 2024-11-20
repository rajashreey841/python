# Prime Number print:

def prime_number(num):
    for i in range(num):
        if i >0:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
number = int(input("Enter the Value:"))               
prime_number(number)