import random
print("Welcome! to python's guess game. Guess a number between 11 to 60")
num = random.randint(11,60)
user_guess = int(input("Attempt 1: "))
count = 1
while num != user_guess:
	if user_guess not in range(11,61):
		print("Please, guess a number between 11 and 60")
	count += 1
	if num > user_guess:
		print("Too low")
	elif num < user_guess:
		print("Too high")
	else:
		print()
	user_guess= int(input(f"Attempt {count}: "))
	if num==user_guess:
	    print(f"Great! You guessed it correctly it's {num}")
	if num != user_guess and count == 6:
		print(f"Only 6 attempts not more that that.The number is {num}")
		break

