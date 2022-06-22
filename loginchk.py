user = input("Enter your name\t")

print("Welcome to interface !!")

username = input("Enter user name\t")

# Function for password verification
def pwdchk (pwd):
  if len(pwd)>4:
    return True

if username == user:
  pwd = input("Create a password (lenth of password should be > 4)\t")
  if pwdchk(pwd) == True:
      name = input("Enter your name\t")
      age = int(input("Enter your age\t"))
      gender = input("Enter your gender\t")
  elif pwdchk(pwd) != True:
      print("Password not correct please re-enter\t")
      pwd = input("Create a password (lenth of password should be > 4)\t")
      if pwdchk(pwd) == True:
        name = input("Enter your name\t")
        age = int(input("Enter your age\t"))
        gender = input("Enter your gender\t")
      else:
        print("Maximum limit reached, Account locked\t")
elif username != user:
  print("Incorrect Username, Re-Enter\t")
  username = input("Enter user name\t")
  if username == user:
    pwd = input("Create a password (should contain at least 1 uppper and 1 digit)\t")
    if pwdchk(pwd) == True:
      name = input("Enter your name\t")
      age = int(input("Enter your age\t"))
      gender = input("Enter your gender\t")
    elif pwdchk(pwd) != True:
      print("Password not correct please re-enter\t")
      pwd = input("Create a password (lenth of password should be > 4)\t")
      if pwdchk(pwd) == True:
        name = input("Enter your name\t")
        age = int(input("Enter your age\t"))
        gender = input("Enter your gender\t")
      else:
        print("Maximum limit reached, Account locked\t")
  else:
    print("Maximum limit reached, Account locked\t")
else:
  name = input("Enter your name\t")
  age = int(input("Enter your age\t"))
  gender = input("Enter your gender\t")
