# program to calculate average height from a list of heights:

heights = input("Enter the Heights: ")
res = heights.split()
s = 0
count =0 
for j in res:
    count = count+1
print(count)
for i in res:
    s += int(i)
print("Average Height:" ,s//count)

