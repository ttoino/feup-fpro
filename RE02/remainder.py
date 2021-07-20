from datetime import datetime, timedelta

now = datetime.now()

alarm = now + timedelta(hours=8, minutes=30)

print(f"{alarm:%H:%M}")
