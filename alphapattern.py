"""Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC"""

n = int(input())
row = 1
while(row <= n):
     col = 1
     while(col <= row):
         charP = chr(ord('A') + row - 1)
         print(charP, end = ' ')
         col = col + 1
     print()
     row = row + 1

