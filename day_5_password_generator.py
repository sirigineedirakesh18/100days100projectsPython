#create a password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("welcome to the Password Generator")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))
password=[]
our_password=''
for char in range(0,nr_letters):
  password.append(random.choice(letters))
for char in range(0,nr_symbols):
  password.append(random.choice(symbols))
for char in range(0,nr_numbers):
  password.append(random.choice(numbers))
random.shuffle(password)
for char in password:
  our_password+=char
print(f"Your password is: {our_password}")
#This code generates a random password based on user input for the number of letters, symbols, and numbers. 
