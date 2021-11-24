# 날짜 및 시간 관련 처리 모듈
# import datetime
# datetime.date()
# datetime.time()
# datetime.datetime()
import datetime

set_day = datetime.date(2019, 3, 1)
print(set_day)
# 2019-03-01

print('{0}/{1}/{2}'.format(set_day.year, set_day.month, set_day.day))
# 2019/3/1

day1 = datetime.date(2021, 11, 23)
day2 = datetime.date(2022, 2, 25)
diff_day = day2 - day1
print(diff_day)
# 94 days, 0:00:00

print(type(day1))
# <class 'datetime.date'>
print(type(diff_day))
# <class 'datetime.timedelta'>


print(datetime.date.today())
# 2021-11-23

today = datetime.date.today()
special_day = datetime.date(2021, 12, 25)
print(special_day - today)
# 32 days, 0:00:00


set_time = datetime.time(15, 30, 45)
print(set_time)
# 15:30:45

print('{0}:{1}:{2}'.format(set_time.hour, set_time.minute, set_time.second))
# 15:30:45

set_dt = datetime.datetime(2018, 10, 9, 10, 20, 0)
print(set_dt)
# 2018-10-09 10:20:00

print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
# 날짜 2018/10/9
print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))
# 시각 10:20:0

now = datetime.datetime.now()
print(now)
# 2021-11-23 11:06:59.840638

print("Date & Time: {:%Y-%m-%d, %H:%M:%S}".format(now))
# Date & Time: 2021-11-23, 11:08:12

print("Date: {:%Y, %m, %d}".format(now))
print("Time: {:%H/%M/%S}".format(now))
'''
Date: 2021, 11, 23
Time: 11/10/05
'''

set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)
print("현재 날짜 및 시각:", now)
print("차이:", set_dt - now)
# 차이: -1453 days, 1:19:11.595265

from datetime import date, time, datetime

print(date(2019,7,1))
# 2019-07-01

print(date.today())
print(time(15,30,45))
print(datetime(2020,2,14,18,10,50))
print(datetime.now())
'''
2021-11-23
15:30:45
2020-02-14 18:10:50
2021-11-23 11:13:22.355113
'''