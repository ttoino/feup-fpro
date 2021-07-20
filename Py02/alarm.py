from datetime import datetime, date, time, timedelta

hour = int(input())
minute = int(input())

date = date.today()
time = time(hour, minute)
now = datetime.combine(date, time)

alarm = now + timedelta(hours=6, minutes=51)

print(f"{alarm:%H:%M}")