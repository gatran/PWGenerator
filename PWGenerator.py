#Shoutout to https://www.101computing.net/random-password-generator/ for the idea and sample code!
#Debugs: https://stackoverflow.com/a/28041598 Putting this in console is helping deal with some unicode issues
#Current bug: Unicode issue not saving the entire password to the text file

import random

#A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

print("Welcome to Password Generator")
print("If you would like a general password - including at least 1 Uppercase letter, 1 Lowercase letter, 1 Number, 1 Punctuation, and 1 Special Character, with a length of 8")

gen = input("Type Yes or No to make changes \n")

#Values found from the website with an ASCII chart
pun_values = [128, 163, 165, 36, 169, 153, 176, 152, 161, 191]
sc_values = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 145, 146, 147, 148, 149, 152]
ucL = chr(random.randint(65,90))
lcL = chr(random.randint(97,122))
n = chr(random.randint(48,57))
p = chr(random.choice(pun_values))
sc = chr(random.choice(sc_values))
curr = ucL + lcL + n + p + sc
#For the other three values, find a new value for each parameter and choose 1 at random [Probably a more efficient way of doing this!!]
for x in range(3):
        ucL = chr(random.randint(65,90))
        lcL = chr(random.randint(97,122))
        n = chr(random.randint(48,57))
        p = chr(random.choice(pun_values))
        sc = chr(random.randint(65,90))
        curr += random.choice([ucL, lcL, n, p, sc])
pw = shuffle(str(curr))

if gen == "Yes":
    print("Here's your default password!")
    print(pw)
    print("Would you like to save your new password in a txt file? - u -")
    print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
    save = input("Type Yes or No \n")
    if save == "Yes":
        #Either create or overwrite the file with a password
        with open("NewPW.txt", "w", encoding="utf-8") as text_file:
            text_file.write(pw)
        print("Your new password can be found in the notepad document titled 'NewPW.txt'")
    print("Enjoy your new password! :)")
elif gen == "No":
    print("Reminder: Only input integers for the next prompts! (Ex: 1 or 2, not 1.5 or 2.288)")
    print("The prompts with the choice of 0 means the final password will not contain any from that choice (Ex. 0 for special characters means no uppercases at all!)")
    try:
        gen_uc = int(input("How many random uppercase letters would you like? (Choose from the numbers 1 to 3) \n"))
        gen_lc = int(input("How many random lowercase letters would you like? (Choose from the numbers 1 to 3) \n"))
        gen_n = int(input("How many random numbers would you like? (Choose from the numbers 1 to 3) \n"))
        gen_p = int(input("How many random punctuations would you like? (Choose from the numbers 0 to 3) \n"))
        gen_sc = int(input("How many random special characters would you like? (Choose from the numbers 0 to 3) \n"))
        gen_len = int(input("How long do you want your password to be? (Choose a length between 8 and 16) \n"))

        if (gen_uc < 1 or gen_uc > 4) or (gen_lc < 1 or gen_lc > 4) or (gen_n < 1 or gen_n > 4) or (gen_p < 0 or gen_p > 4) or (gen_sc <0 or gen_sc > 4) or (gen_len < 8 or gen_len > 16):
            raise Exception()
        if (gen_uc + gen_lc + gen_n + gen_p + gen_sc == 0):
            print("Nice Try!! >:)")
            print("Take this default password!")
            print(pw)
            print("Would you like to save your new password in a txt file? . _ .")
            print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
            save = input("Type Yes or No \n")
            if save == "Yes":
                with open("NewPW.txt", "w") as text_file:
                    text_file.write(pw)
                print("Your new password can be found in the notepad document titled 'NewPW.txt'")
            print("Enjoy your new password! :/ ... rebel")
    except ValueError: 
        print(">:o follow rules, not an integer input!")
        print("Take this default password!")
        print(pw)
        print("Would you like to save your new password in a txt file? . _ .")
        print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
        save = input("Type Yes or No \n")
        if save == "Yes":
            with open("NewPW.txt", "w") as text_file:
                text_file.write(pw)
            print("Your new password can be found in the notepad document titled 'NewPW.txt'")
        print("Enjoy your new password! :/ ... rebel")
    except Exception:
        print(">:o follow da rules!")
        print("Take this default password!")
        print(pw)
        print("Would you like to save your new password in a txt file? . _ .")
        print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
        save = input("Type Yes or No \n")
        if save == "Yes":
            with open("NewPW.txt", "w") as text_file:
                text_file.write(pw)
            print("Your new password can be found in the notepad document titled 'NewPW.txt'")
        print("Enjoy your new password! (rebel!)")
    
    #Generating the user input values
    ucL = chr(random.randint(65,90))
    lcL = chr(random.randint(97,122))
    n = chr(random.randint(48,57))
    p = chr(random.choice(pun_values))
    sc = chr(random.choice(sc_values))
    for x in range(gen_uc):
        ucL += chr(random.randint(65,90))
    for x in range(gen_lc):
        lcL += chr(random.randint(97,122))
    for x in range(gen_n):
        n += chr(random.randint(48,57))
    for x in range(gen_p):
        p += chr(random.choice(pun_values))
    for x in range(gen_sc):
        sc += chr(random.choice(sc_values))
    #Get the current generated values
    curr = ucL[1:] + lcL[1:] + n[1:] + p[1:] + sc[1:]

    #Find how many more characters we will need
    rndm_to_gen = gen_len - len(curr)

    #Generate the rest of the characters
    if p[1:] == '' and sc[1:] == '':
        for x in range(rndm_to_gen):
            ucL = chr(random.randint(65,90))
            lcL = chr(random.randint(97,122))
            n = chr(random.randint(48,57))
            curr += random.choice([ucL, lcL, n])
    elif p[1:] == '':
        for x in range(rndm_to_gen):
            ucL = chr(random.randint(65,90))
            lcL = chr(random.randint(97,122))
            n = chr(random.randint(48,57))
            p = chr(random.choice(pun_values))
            curr += random.choice([ucL, lcL, n, p])
    else:
        for x in range(rndm_to_gen):
            ucL = chr(random.randint(65,90))
            lcL = chr(random.randint(97,122))
            n = chr(random.randint(48,57))
            sc = chr(random.choice(sc_values))
            curr += random.choice([ucL, lcL, n, sc])

    pw = shuffle(str(curr))
    print("Here's your unique password!")
    print(pw)
    print("Would you like to save your new password in a txt file? - u -")
    print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
    save = input("Type Yes or No \n")
    if save == "Yes":
        with open("NewPW.txt", "w") as text_file:
            text_file.write(pw)
        print("Your new password can be found in the notepad document titled 'NewPW.txt'")
    print("Enjoy your new password! :)")
    
else:
    #If the input is not Yes or No for the initial question
    print("why u no follow rules :(")
    print("me no like u!")
    print("take ur default password!")
    print(pw)
    print("Would you like to save your new password in a txt file? . _ .")
    print("Caution: If a previous password is saved in the NewPW.txt file, it will be overwritten! Be careful!")
    save = input("Type Yes or No \n")
    if save == "Yes":
        with open("NewPW.txt", "w", errors="ignore") as text_file:
            text_file.write(pw)
        print("Your new password can be found in the notepad document titled 'NewPW.txt'")
    print("Enjoy your new password! (rebel!)")
