"""Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000"""

n = int(input())
row = 1
end = 2 * n + 1
mid = n + 1

while(row <= n):
    col = 1
    while(col <= (2*n+1)):
        if row == col or col == mid or col == end:
            print("*",  end = " ")
        else:
            print(0, end = " ")
        col = col + 1

    print()
    row = row + 1