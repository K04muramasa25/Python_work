#日付の取得

import datatime

today = datatime.date.today()
todaydetail = datatime.datatime.today()
#今日の日付
print('-------------------------------------')
print(today)
print(todaydetail)

#今日に日付：それぞれの値
print('-------------------------------------')
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

#日付のフォーマット
print('-------------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))


#日付の計算
import datatime

today = datatime.datatime.today()

#今日の日付
print(today)

#明日の日付
print(today + datatime.timedelta(days=1))
newyear = datatime.datatime(2010, 1, 1)

#2010年1月1日の一週間後
print(newyear + datatime.timedelta(days=7))

#2010年1月1日から今日までの日数
calc = today - newyear
#結果の戻り値は「timedelta」
print(calc.days)

#うるう年の判定
import calender

print(calender.isleap(2015))
print(calender.isleap(2016))
print(calender.isleap(2017))

print(calender.leapdays(2010, 2020))





