import time
import _datetime
#a=time.ctime()
#print(time.time())
#print(time.ctime(1595290192.9759343))
#print(time.gmtime())
#print(time.asctime())
#print(time.localtime())
#help(time.strftime)
#print(time.strftime("%m/%d/%Y"))
#b="20 August 2020"
#print(time.strptime(b,"%d%B%Y"))

'''print(_datetime.datetime(2020,8,21,12,30,50,757))
print(_datetime.datetime.today())
print(_datetime.datetime.now().month)
print(_datetime.datetime.today().hour)
print(_datetime.datetime.today().year)'''

print(_datetime.date(2019,7,5))
print(_datetime.time(12,3,23))

c=_datetime.timedelta(days=20,hours=12,minutes=25,seconds=51)
d=_datetime.timedelta(days=30,hours=3,minutes=40,seconds=25)
e=c-d
print(e)
