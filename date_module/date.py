import datetime

inputDate = input("Input release date in this format: dd/mm/yyyy\n")
inputDate = datetime.datetime.strptime(inputDate, "%d/%m/%Y").date()

current = datetime.date.today()
delta = current - inputDate

print(delta.days)

# %A day of the week
# %d day
# %b %B month
# %y %Y year

# currentdate.strftime('%d %b, %Y)
# datetime.datetime.str.strptime("turns string to date").date()