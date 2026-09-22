import random
low_limit=0
high_limit=25
print("Welcome to guess game.")
print("Think of a number between 0 and 25")
print("Then,i will read your mind")
print("Say hello friend")
greet=input("Enter your greeting ")
print(f"Hello, {greet}! let's play")
while True:
     #for invalied range(26,25)
    if low_limit > high_limit:
         print("Hmm, those answers don't add up.")
         break
    bot_choice=random.randint(low_limit,high_limit)
    print(f"is it {bot_choice}?")
    user_input=input("Enter yes or no: ").lower()
    if "no" in user_input:
        print("Is it high or low than this number? ")
        user_input=input("High or Low ").lower()
        if "high" in user_input:
            low_limit=bot_choice+1
        elif "low" in user_input:
            high_limit=bot_choice-1
            #make the high limit low
            #by making bot_choice the high limit-1
        else:
            print("Enter something valid.")
        continue
    elif "yes" in user_input:
        print(" I did it!!!!")
        print("So, its actually",bot_choice)
        break
    else:
        print("Type yes or no")
        continue
        
print("Game ended")

#The game is simple.If the user thinks of 12.
#The bot guesses 4..The user types high.So,it can't be 4 or below like 3,2
#It can lie in range(5,26).So,the high input updates by setting the lower limit to bot_choice(4)+1
#The number can lie in the possible range of(5,26)
