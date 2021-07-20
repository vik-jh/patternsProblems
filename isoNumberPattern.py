"""Print the following pattern for n number of rows.
For eg. N = 5

1                1
12            21
123        321
1234    4321
1234554321"""


n = int(input())
row = 1
while(row <= n):
    col = 1
    while(col <= row):
        print(col, end = ' ')
        col = col + 1

    space = 1
    while(space <= (2*n - 2*row)):
        print(" ", end = " ")
        space = space + 1
    
    row1 = row
    col1 = 1
    while(col1 <= row):
        print(row1, end = ' ')
        col1 = col1 + 1
        row1 = row1 - 1
    print()
    row = row + 1


