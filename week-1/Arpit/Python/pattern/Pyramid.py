def pyramid(p):
  for x in range(0, p):
     for y in range(0, x):
        print("* ",end="")
     print(" ")
pyramid(15)