import mymodule1
import mymodule2

print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )
print("My name is", __name__)
#the name that is show was "__main__" because this is the main thread where the program is taking place.
#The name for the program that is imoirted s its program name
#the module1 shows the if statement because it is run in that program but in theis program it wont show because it is imported
#wnat to tell it to run from the progarm thats importing it