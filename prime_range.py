import math
m = input()

for n in range(int(m)):
	l = int(input())
	num = 2
	count = 0
	while(count<l):
                if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
			count++
			num ++
	print("\n")
