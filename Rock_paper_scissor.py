import os
import random

#Check if file exists to make the variable last_score
if os.path.isfile('high_score.txt'):
    with open('high_score.txt','r') as last:
        last_score = int(last.read())  
else:
    #if it does not exist make last_score as zero
    last_score = 0
    with open('high_score.txt','w') as last:
        last.write(str(last_score)) 
    
choices = ['rock','paper','scissor']
def win(bot_guess,user_guess):
     if bot_guess != user_guess:
        #rock beats scissor
        if bot_guess == choices[0] and user_guess == choices[2]:
            return 'Bot won'
         #scissor beats paper
        elif bot_guess == choices[2] and user_guess == choices[1]:
            return 'Bot won'
         #paper beats rock
        elif bot_guess == choices[1] and user_guess == choices[0]:
            return 'Bot won'
        else:
            return 'User won'
     else:
        return 'Tie'
        
print('Game started')
print("Type 'e' to exit")
score = 0

while True:
        user_choice = input('Enter your choice: ')
        if user_choice == 'e':
            #Save if the score is higher than the last saved score
            if score > last_score:
                with open('high_score.txt','w') as high:
                    high.write(str(score))
                last_score = score
            print('You exited')
            print('Your high score', last_score)
            break
            
        elif user_choice in choices:
            bot_guess = random.choice(choices)
            print('Bot took',bot_guess)
            won = win(bot_guess,user_choice)
            if won == 'User won':
                score = score + 1
            print(won)
            
        else:
            print('Type correct bro ..')
            
