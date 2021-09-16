year = int(input("enter the year:"))
if (year % 4):
    if(year % 100):
        if (year % 400):
            print ("{0} the year is leap year".format(year))
        else:
            print("{0} the year is not leap year".format(year))

    else:
     print("{0} the year is a leap year".format(year))

else:
   print("{0}the year is a leap year".format(year))
