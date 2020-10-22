import datetime

year = 1989
month = 11
day = 26

birthday = datetime.date(year, month, day)
today = datetime.date.today()

from_birth_days.days = today - birthday


days_in_year_list = []
for x in range(year + 1, today.year):
    first_day = datetime.date(x, 1, 1)
    last_day = datetime.date(x, 12, 31)
    days_in_year = last_day - first_day
    days_in_year_list.append(days_in_year.days)

after_years_out = from_birth_days.days - sum(days_in_year_list)

print(f"Years: {len(days_in_year_list)}")
print(f"days: {after_years_out}")
