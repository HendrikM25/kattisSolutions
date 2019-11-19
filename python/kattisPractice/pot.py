n = int(input())
s = 0
i = 0

for i in range(n):
    p = int(input())
    pot = p/10 - int(p/10)
    pot = round(pot, 1)
    p = int(p/10)
    s += p**(pot*10)

print(int(s)) 
