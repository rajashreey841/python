# Matrix Operation

row1 = ['😀','😀','😀']
row2 = ['😀','😀','😀']
row3 = ["😀","😀","😀"]
res = [row1,row2,row3]
print(res)
index_value = input("Enter the index value: ")
row = int(index_value[0])
col = int(index_value[1])
result = res[row-1][col-1] = 'x'
print(result)

print(f" {row1} \n {row2}\n {row3}")