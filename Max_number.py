# program to find maximum number from from a list of numbers.

number = input("Enter the list of numbers: ")
result = number.split()
for i in range(0,len(result)-1):
    if int(result[i]) > int(result[i+1]):
        result[i+1] = result[i]
print("Maximum number :", result[i+1])