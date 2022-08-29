day=int(input("enter any day"))
month=int(input("enter any month"))
year=int(input("enter any year"))

if month==1:
    if day==31:
        month=2
        day=1
    else:
        day=day+1
elif month==2:
    if day==28:
        month=3
        day=1
elif month==3:
    if day==31:
        month=4
        day=1
    else:
        day=day+1
elif month==4:
    if day==30:
        month=5
        day=1
    else:
        day=day+1
elif month==5:
    if day==31:
        month=6
        day=1
    else:
        day=day+1
elif month==6:
    if day==30:
        month=7
        day=1
    else:
        day=day+1
elif month==7:
    if day==31:
        month=8
        day=1
    else:
        day=day+1
elif month==8:
    if month==31:
        month=9
        day=1
    else:
        day+=1
elif month==9:
    if day==30:
        month=10
        day=1
    else:
        day+=1
elif month==10:
    if day==31:
        month=10
        day=1
    else:
        day+=1
elif month==11:
    if day==30:
        month=11
        day=1
    else:
        day+=1
elif month==12:
    if day==31:
        month=1
        day=1
    else:
        day+=1
    year=year+1

print(day,month,year)

