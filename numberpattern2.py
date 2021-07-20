"""
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
"""

n = int(input())

row = 0
while(row < n):
    col = 0
    while(col <= row):

        if row == 0: 
            print(1, end = ' ')
        elif row == col or col == 0:
            print(row, end = ' ')
        else:
            print(0, end = ' ')
        col = col+1
    print()
    row = row + 1