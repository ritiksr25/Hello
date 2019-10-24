import math
t = int(input())
    
for i in range(t):
    ab,bc,ac = input().split(' ')
    p = 0.52532198881 * int(ab)
    print(math.ceil(p))
