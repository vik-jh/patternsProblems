'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221'''

n = int(input())

row = 0
while(row < n):
    col = 0
    while(col <= row):
        if row == 0 or row == col or col == 0:
            print(1, end = ' ')
        else:
            print(row, end = ' ')
        col = col +1
    print()
    row = row + 1