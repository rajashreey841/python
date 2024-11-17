# program to calculate average height from a list of heights:

heights = input("Enter the Heights: ")
res = heights.split()
sum = 0
for i in res:
    sum += int(i)
print("Average Height:" ,sum//len(res))

