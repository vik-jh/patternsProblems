"""Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1"""

n = int(input())
row = n
while(row > 0):
    col = 1
    while(col <= row):
        print(col, end = ' ')
        col = col + 1
    print()
    row = row - 1