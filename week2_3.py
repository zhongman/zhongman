import datetime
import time
d1=datetime.date(2017,4,14)
print(d1)
message=input("days:")
a=int(message)
if a<2 or a>10:
    pass
else:
    d=datetime.timedelta(a)
    d2=d1+d
    print(d2)
