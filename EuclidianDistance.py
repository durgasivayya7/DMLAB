import math
n = int(input("Enter number of data points: "))
data = []
for i in range(n):
    x, y = map(float, input(f"Enter point {i+1} (x,y): ").split(','))
    data.append([x, y])
matrix = [
    [round(math.sqrt((data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2), 2)
     for j in range(n)]
    for i in range(n)
]
print("\nDissimilarity Matrix:")
for row in matrix:
    print(row)
