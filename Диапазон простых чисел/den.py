import sys
n=input("Enter the integer number:")
if (not n.isdigit()) | (n=='0'):
  print("Integer, btch!")
  sys.exit()
n=int(n)

number=3
print("1 is hard number")
print("2 is hard number")
hard=[1,2]
while number<=n:
  div=2
  b=0
  while div<number:
    if number%div==0:
      print(number, "is simple number")
      b=1
      break
    if div+1==number:
      if b==0:
        print(number, "is hard number")
        hard += [number]
    div += 1
  number += 1
print(hard)