#My Solution

def format_name(f_name,l_name):
  full_name = f_name + " " +l_name
  return full_name.title()

print("Welcome to Name Formatter!!")
print("Enter your first & last name in whatever case you like.")
print("-------------------------------------------------------")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(f"Your formatted full name is {format_name(fname,lname)}")