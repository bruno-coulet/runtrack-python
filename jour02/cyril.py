from math import sqrt

def PrimalList( n ):
  Max = n + 1
  last = int(sqrt(Max))
  t = [True] * Max
  for i in range(2, last):
    if t[i]:
      for j in range(i*i, Max, i):
        t[j]=False
  return [i for i in range(2, Max) if t[i]]

print(PrimalList(1000))
