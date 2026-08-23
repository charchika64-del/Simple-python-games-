print("Create a strong password.")
print("Password must be in the range of 8 to 12 characters.")
print("It must have 4 different special characters.")
special=["#","₹","%","&","@","*","+","_",":","|","<",">","$","€","!",";","-","="]
password=input("Enter password: ")
length=len(password) 
char_count=0
spec_count=0
set_of_chars=set()
not_done=True
while not_done:
    #Check length first
    if length not in range(8,13):
        if length < 8:
            print(f"There should be {8-length} more characters.")
            password=input("Enter password: ")
            #Reset all according to the new password
            length=len(password)
            char_count=0
            set_of_chars=set()
            spec_count=0  
            continue      
            #STOP!! if the password is wrong 
            #Start again
        else:
            print(f"There should be {length-12} less characters.")
            #Reset all according to the new password
            password=input("Enter password: ")
            length=len(password)
            char_count=0
            set_of_chars=set()
            spec_count=0  
            continue      
  #Count special characters if the length is in range  
    for character in password:
        if character in special:
            char_count=char_count+1
            set_of_chars.add(character)
    spec_count=len(set_of_chars)
    
    #Check if specual chracters are 4 or not
    if char_count<4:
        #Same here
        print("Please need more special characters.")
        password=input("Enter password: ")
        length=len(password)
        char_count=0
        set_of_chars=set()
        spec_count=0  
        continue      
        #Back to loop if there are not enough less special characters
        
    #Give message if there is repitition
    repeated=char_count-spec_count
    if repeated>0:
        print(f"{repeated} characters were repeated")
        password=input("Enter password: ")
        length=len(password)
        char_count=0
        set_of_chars=set()
        spec_count=0  
        continue      
    #Check conditions if password has 8 to 12 chars.Special characters are 4 or not.
    if length in range(8,13) and spec_count>=4:
        print("Well done!!")
        not_done=False
