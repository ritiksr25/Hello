t = int(input())
def n_prime(n):
  count = 0
  num = 2
  k=0
  while count < n:
    for i in range(1,num-1):
        if num % i == 0:
            k = 1
        else:
            k = 0
    if k == 0:
        count += 1
        num += 1
  return num

for _ in range(t):
    inp = int(input())
    print(n_prime(inp))
