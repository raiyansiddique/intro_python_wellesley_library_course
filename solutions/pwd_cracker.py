# Write a Python script that uses the random library to generate 
# random character combinations and simulate keyboard inputs. 
# The script prompts the user for a password, and then uses a while loop to 
# generate random character combinations until the correct password is found. 
# The generated password is compared to the user's input password using a list comparison,
# and if a match is found, the script prints the password to the console.

import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
chars_list = list(chars)

password = pyautogui.password("Enter A Password: ")
#password = input("Enter a password: ")
guess_password = ""

while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print(guess_password)

	if(guess_password == list(password)):
		print("Your Password Is: " + "".join(guess_password))
		input()
		break
