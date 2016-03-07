def Euler1():
    sum = 0
    for x in range(1000):
        if x%3==0 or x%5==0:
            sum += x
    print sum

def Euler2():
    sum = 0
    n1 = 1
    n2 = 2
    while n2 < 4000000:
        if n2%2==0:
            sum += n2
        t = n1 + n2
        n1 = n2
        n2 = t
    print sum
    
