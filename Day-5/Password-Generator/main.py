#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
pw_list =[]
for i in range(0,nr_letters):
  letter=''
  letter += random.choice(letters)
  password += letter
  pw_list.append(letter)
  
for i in range(0,nr_symbols):
  sym=''
  sym += random.choice(symbols)
  password += sym
  pw_list.append(sym)
  
for i in range(0,nr_numbers):
  nr = ''
  nr += random.choice(numbers)
  password += nr
  pw_list.append(nr)

print(f"{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_pw=''
length = len(pw_list)
for i in range(0,length):
  
  chr=''
  chr+=random.choice(pw_list)
  random_pw+=chr
  pw_list.remove(chr)

print(f"{random_pw}")
