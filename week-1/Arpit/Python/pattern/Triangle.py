len = 10
a = (2 * len) - 2
for x in range(0, len):
 for y in range(0, a):
    print(end=" ")
 a = a - 1
 for y in range(0, x + 1):
    print("*", end=' ')
 print(" ")
