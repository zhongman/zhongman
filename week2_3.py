import datetime
import time
d1=datetime.date.today()
print(d1)
message=input("days:")
a=int(message)
list=range(2,10)
while a in list:
    d=datetime.timedelta(a)
    d2=d1+d
    print(d2)
    break
