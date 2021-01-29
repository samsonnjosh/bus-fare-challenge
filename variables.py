# Taken day number from user
weekday = int(input("Enter weekday day number (1-7) : "))
Mon=1
Tue=2
Wen=3
Thur=4
Fri=5
Sat=6
Sun=7

if weekday == 1 :
    print("\nMon");

elif weekday == 2 :
    print("\nTue")

elif(weekday == 3) :
    print("\nWed")

elif(weekday == 4) :
    print("\nThur")

elif(weekday == 5) :
    print("\nFri")

elif(weekday == 6) :
    print("\nSat")

elif (weekday == 7) :
    print("\nSun")
# Taken day number bus fare
busFare= int(input("Enter weekday day number (Mon-San) : "))

if weekday == 1 :
    print("\nbus fare for MON =100");

elif weekday == 2 :
    print("\nbus fare for TUE =100")

elif(weekday == 3) :
    print("\nbus fare for  WEN =100")

elif(weekday == 4) :
    print("\nbus fare for THUR =100")

elif(weekday == 5) :
    print("\nbus fare for FRI =100")

elif(weekday == 6) :
    print("\nbus fare for SAT =60")

elif (weekday == 7) :
    print("\nbus fare for SUN =80")
else :
    print("\nPlease enter weekday number between 1-7.")