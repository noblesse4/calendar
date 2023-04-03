n = input("enter the time frame in this format: mm-yyyy ")

weekDays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
months = ["January", "Fabuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
bm = ["January", "March", "May", "July", "August", "October", "December"]

month=int(n.split("-")[0])
year= int(n.split("-")[1])

nameMon=months[month-1]

print("     {} {}      ".format(nameMon,year))

for i in weekDays:
    if not i.__eq__("Su"):
        print(i, end=" ")
    else:
        print(i)

def Zellers_congruence(day,month, year):
    if (month == 1):
        month = 13
        year = year - 1

    if (month == 2):
        month = 14
        year = year - 1
    z = (day + 13 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7
    return z
z=Zellers_congruence(1,month,year)
if z!=2:
    print("   "*((z+5)%7),end="")

k=[]
if nameMon in bm:
    k=range(1,32)
elif nameMon.__eq__("Febuary"):
    k=range(1,29)
else:
    k=range(1,31)
for i in k:
    z = Zellers_congruence(i,month,year)
    if z == 1:
        print(i)
    elif 0<i<10:
        print(i,end="  ")
    else:
        print(i,end=" ")