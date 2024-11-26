# program to calculate average height from a list of heights:

heights = input("Enter the Heights: ")
res = heights.split()
s = 0
count =0 
for i in res:
    count = count+1
print(count)
for j in res:
    s += int(j)
print("Average Height:" ,s//count)

