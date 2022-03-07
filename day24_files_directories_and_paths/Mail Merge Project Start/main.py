#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt","r") as name_file:
    Names = []
    for name in name_file:
        Names.append(name.strip())

count = 0

while count != len(Names):
    replacement = ""
    file = open("Input/Letters/starting_letter.txt", "r")
    for line in file:
        line = line.strip()
        changes = line.replace("[name]", Names[count])
        replacement = replacement + changes + "\n"
    with open(f"Output/ReadyToSend/letter_for_{Names[count]}.txt","w") as fout:
        fout.write(replacement)
    file.close()
    count += 1


