'''
if temp is greater than 30
    it is a hot day
otherwise if it is less than 10
 its a cold day 
otherwise
   it is neither hot nor cold
'''

temp = 30
if temp > 30:
    print("it is a hot day")
else:
    print(" its a cold day ")

'''
=
==
<=
>=
!=
'''  


#example


name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long.")
else:
    print("Name looks good!")
