def ab_plus_c(a,b,c):
    if a==0:
        return c
    return b+ab_plus_c(a-1,b,c)
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(ab_plus_c(a,b,c))
