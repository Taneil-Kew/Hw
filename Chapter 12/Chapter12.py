import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2018)                   # What happens here?

#C
cal = calendar.TextCalendar(6)
cal.prmonth(2018, 4)

#D
d= calendar.LocaleTextcalendar(6, "Greek")
d.pryar(2012)

#E
print(calendar.isleap(8))
#it expects a year
#it returns true or false
#boolean


#E2
#leo section F

#A
#there are 47 functions for math
#B
import math
myvar = math.floor(78.89)
print(myvar)
mvar = math.ceil(78.89)
print(myvar)
#floor rounds down cell round up
#C
#have been using the exponete with x**.5, which would give the square root because its a fraction
x**.5
#D
#there are 5 constrants for math
math.pi
math.e
math.tau
math.inf
math.nan
#math.inf and math.nan were made by mark dickinson.  The inf function does not need an negative sign. math.tau was created by Lisa Roach.

#E3
#Copy
#shallow copy doesn't copy references in the lists, the refs stay the same. For example in one list if the variable changes then the copied variable will cahnged aswell. In a deep copy, the refrences are copied as well, so to simila objects will still have their nesscary differences.
#in excersise 3 from chapter 11 deep copy would have been resourceful

#E4
#namespace_test
import mymodule1.py
import mymodule2.py
print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )
print("My name is", __name__)
