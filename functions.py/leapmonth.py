# year=int(input("which year do you want to check?"))
def is_leap(year):
    leap1=(year%4)
    # print(leap1)
    if year% 4==0 :
        if year%100==0 :
            if year%400==0:
                return True
            else:
                return False
        else :
            return True
    else:
        return False

def days_in_month(year, month):
     month_days =[31,28,31,30,31,30,31,30,31,30,31,30]
     if  is_leap(year) and month==2:
        return 29
     return month_days[month-1]
year=int(input("enter a year:"))
month=int(input("enter a month:"))
days=days_in_month(year,month)
print(days)