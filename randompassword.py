#Cod soft Task3-Password generator
"password generator application by using python"
#importing two modules

import string
import random

"creating a variable for storing length of the password"
lengthofpassword=int(input("Enter a password length: "))

# given variable contains lowercase alphabets
lower_case_letter_=string.ascii_lowercase

#given variable contains uppercase alphabets
upper_case_letter=string.ascii_uppercase

#given variable contains numbers
numbers=string.digits

#given variable contains punctuations
punctuations=string.punctuation

"combination of all characters"
combination=lower_case_letter_+upper_case_letter+numbers+punctuations

#sample() function produces characters in form of list
list=random.sample(combination,lengthofpassword)

#converting list in to string
password=" "
for char in list:
    password+=char
print("The random password:",password)
