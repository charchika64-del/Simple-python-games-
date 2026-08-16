#A simple Python game for word guessing 
import random
words=["Animal","Python","Snake","Good","Fruit","Raddish","Banana","Lemon","Balloon","Train","Ant","Dog"]
secret_word=random.choice(words).lower()
attempts=len(secret_word)
turn=0
index=0
user_word=""#For user
while turn<attempts:
    guess = input("Enter the letter: ").lower()
    if guess==secret_word[index]:
        user_word=user_word+guess#keeps adding 
        print(user_word,"_____")
        index=index+1#To prepare for next index item in secret word
        if user_word==secret_word:
            print("You win!! ")
            break
    else:
        turn=turn+1#Adds wrong attempts
        print("You guessed wrong!! No of attempts left",attempts-turn)
else:
    print("You lost")
