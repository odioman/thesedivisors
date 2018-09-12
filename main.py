num = int(input('Enter a number'))
newlist = []
for x in range(1, num + 1):
  if num % x == 0:
    newlist.append(x)
  print(newlist)
