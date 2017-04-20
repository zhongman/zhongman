import datetime
import time
d1=datetime.date.today()
print(d1)
message=input("days:")
a=int(message)
b=2**10
if a>0 and a<b:
    d=datetime.timedelta(a)
    d2=d1+d
    print(d2)
