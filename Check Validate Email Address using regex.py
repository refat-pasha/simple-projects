
import re
email_comdition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("enter your email:")

if re.search(email_comdition,user_email):
    print("Right Email!")
else:
    print("Wrong Email!")



