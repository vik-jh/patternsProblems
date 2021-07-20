"""Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234"""

n = int(input())
row = 1
while(row <= n):
    space = 1
    while(space < ((2*n)-2)/2):
        print(" ", end = ' ')
        space = space + 1

    row1 = 1
    col = row
    while(row1 <= row):
        print(col, end = ' ')
        row1 = row1 + 1
        col = col - 1
    
    row2 = 1
    col1 = 2
    while(row2 <= row - 1):
        print(col1, end = " ")
        row2 = row2 + 1
        col1 = col1 + 1
    print()
    row = row + 1
    

"""n=int(input())
i=1
while(i<=n):
    space=1
    while(space<=n-i):
        print(" ", end='')
        space=space+1
    j=1
    k=i
    while(j<=i):
        print(k, end='')
        j=j+1
        k=k-1
    num=1
    l=2
    while(num<=i-1):
        print(l, end='')
        num=num+1
        l=l+1
    print()
    i=i+1"""



    
