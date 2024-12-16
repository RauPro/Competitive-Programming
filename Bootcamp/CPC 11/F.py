import datetime
#from datetime import _is_leap

def _is_leap(year):
    "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

t = int(input())
res = []
for _ in range(t):
    mapper = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
              "September": 9, "October": 10, "November": 11, "December": 12}
    s1 = input()
    s2 = input()
    date0 = s1.split(",")
    date1 = s2.split(",")
    #print(date0, date1)
    date0_month = date0[0].split(" ")[0]
    date0_day = date0[0].split(" ")[1]
    date0_year = date0[1]
    #print(datetime.date(int(date0_year), mapper[date0_month], int(date0_day)))
    date1_month = date1[0].split(" ")[0]
    date1_day = date1[0].split(" ")[1]
    date1_year = date1[1]
    date0_day = int(date0_day)
    date0_year = int(date0_year)
    date1_day = int(date1_day)
    date1_year = int(date1_year)
    date0_month_int = mapper[date0_month]
    date1_month_int = mapper[date1_month]
    if date0_year < date1_year or (date0_year == date1_year and date0_month_int < date1_month_int) or (
            date0_year == date1_year and date0_month_int == date1_month_int and date0_day < date1_day):
        first_date = [date0_year, date0_month_int, date0_day]
        second_date = [date1_year, date1_month_int, date1_day]
    else:
        first_date = [date1_year, date1_month_int, date1_day]
        second_date = [date0_year, date0_month_int, date0_day]
    ans = 0
    if first_date[1] > 2:
        first_date[0] += 1

    if second_date[1] < 2 or (
            second_date[1] == 2 and second_date[2] < 29):
        second_date[0] -= 1
    #di
    first_date[0] -= 1
    ans += second_date[0] // 4 - second_date[0] // 100 + second_date[0] // 400
    ans -= first_date[0] // 4 - first_date[0] // 100 + first_date[0] // 400
    res.append(f"Case {_+1}: {ans}")
print("\n".join(res))