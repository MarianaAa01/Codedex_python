import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 9, 3)

days_away = (next_birthday - today).days

if(days_away == 0):
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')