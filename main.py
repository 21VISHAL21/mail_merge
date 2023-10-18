#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    new_names = names.readlines()
with open("./Input/Letters/starting_letter.txt") as data:
    content = data.read()
    for name in new_names:
        temp = name.strip()
        new_data = content.replace("[name]",f"{temp}")
        with open(f"./Output/ReadyToSend/letter_for_{temp}.txt",mode="w") as mail:
            mail.write(new_data)




#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp