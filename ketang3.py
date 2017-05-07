def is_prime(n):
    def f(i):
        if i>=n:
            print("yes")
        elif n%i!=0:
            return f(i+1)
        else:
            print("no")

    return f(2)
c=int(input("a number:"))
is_prime(c)
