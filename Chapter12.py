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
#B
import math
myvar = math.floor(78.89)
print(myvar)
mvar = math.ceil(78.89)
print(myvar)
#floor rounds down cell round up

#E3
caop makes a shallow copy - the refs stay the same 