#password genetrator 
import random
specials=["#","₹","%","&","@","*","+","_",":","|","<",">","$","€","!",";","-","="]
digits = ["0","1","2","3","4","5","6","7","8","9"]
char_num=int(input("Enter no. of characters you want im your password:  "))
#No. of characters user wants
if char_num%2==0:
    half_characters=char_num/2
    #needs half digits and half specials
else:#for odd input
    half_characters=(char_num+1)/2#making even  
    #suppose char_num=5
    #then half char is 3
    #it will give 6 characters in password 
    #because 3 are specials and digits
    
half_characters=int(half_characters)
#There should be half no. of special characters and half no. of digits
password_specials=[]
password_digits=[]
count=0
#>= i have not used that because there is one extra iteraton with that. 
#Suppose if half char is 2 then the loop runs 3 times by comparing (0,1,2) <= 2(0 is also compared not 1 and 2 only)
#By using > only it's true for only (0,1) not 2>2.
while count<half_characters:
    count=count+1
    random_special=random.choice(specials)
    random_digits=random.choice(digits)
    password_specials.append(random_special)
    password_digits.append(random_digits)
   
password=password_specials+password_digits
random.shuffle(password)
if char_num%2!=0:
    removed_char=random.choice(password)
    password.remove(removed_char)
    #one char needs to be removed 

generated_password="".join(password)
print(generated_password)
