import random

def want_to_play():
    decision = int(input(f"You want to Continue Press(1/0) 1 for play , 0 for Quit : "))
    if decision == 1 :
        Guess_Number()
    
    elif decision == 0 :
        print(f"Thank You !! Quiting .........")
    
    else :
        print("Incorrect choice !")
        want_to_play()

def Guess_Number():
    attempts =  0
    Number = random.randint(1, 100)

    while(True):
        guess = int(input("Guess the Number Between 1 to 100 : "))
        attempts += 1

        if guess == Number:
            print(f"Congratulations you Guess it right in {attempts} attempts\n")
            break
        
        elif guess > Number:
            print("OOPS !! It's too High , Smaller Number please \n")

        else :
            print("OOPS !! It's too small , Larger Number please \n")
    
    want_to_play()

Guess_Number()

        
