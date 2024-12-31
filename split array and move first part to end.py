#split array and move first part to end
 
arr = [36, 8, 12, 52, 38, 22, 10]
n = len(arr)
position = 3
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
    print(i, end=" ")