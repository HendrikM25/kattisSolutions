while True:
    n = int(input())
    tVor = 0
    m = 0
    if n == -1:
        break
    for _ in range(n):
        s, t = input().split()
        s = int(s); t = int(t)
        m += (t-tVor)*s
        tVor = t
    print(m, "miles")
