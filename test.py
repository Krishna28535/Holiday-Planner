from exception.exception import HolidayPlannerException
try:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    print(a/b)
except ValueError as e:
    raise HolidayPlannerException(e)