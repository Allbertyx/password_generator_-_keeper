import random 

exit = True

password_to_save = ""

def generateNewPassword():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = list('!@#$%^&*()-_=+[]{}|;:",.<>?/`~')
    numbers = ["0","1","2","3","4","5","6","7","8","9"]

    password = ""

    for i in range(8):
        random_for_selection = random.randint(1, 3)
        if random_for_selection == 1:
            random_for_lower_or_upper = random.randint(0,1)
            if random_for_lower_or_upper == 0:
                password += str(random.choice(alphabet).lower())
            else:
                password += str(random.choice(alphabet).upper())
        elif random_for_selection == 2:
            password += str(random.choice(special_characters))
        else:
            password += str(random.choice(numbers))
    print("Your password is:", password)
    return(password)

def savePassword(password_generated_to_save):
    platform_pass = str(input("For what platform is your password  "))
    
    archive = open("passwords.txt", "a")
    
    string_to_save_in_rachive = str(platform_pass + ": " + password_generated_to_save + "\n")
    print(string_to_save_in_rachive)

    archive.write(string_to_save_in_rachive)

    archive.close()

def seePasswords():
    print("-------------This are your passwords-------------")
    archive = open("passwords.txt")
    print(archive.read())
    archive.close()

while(exit):
    print("-------------Select your action-------------")
    print("1-Generate new password\n2-Save Password\n3-See passwords\nQ-Exit")
    userSelection = str(input())
    if userSelection == "1":
        password_to_save = generateNewPassword()
    elif userSelection == "2":
        savePassword(password_to_save)
    elif userSelection == "q" or userSelection == "Q":
        exit = False
        print("See you next time!")
    elif userSelection =="3":
        seePasswords()
    else:
        print("Select a correct option")


