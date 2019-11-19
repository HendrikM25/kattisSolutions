n = int(input()) 
qaly = 0

for _ in range(n):
    q, p = input().split()
    qaly += float(q) * float(p)

print(qaly)
