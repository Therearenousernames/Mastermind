import random
import sys

def run_game():
    # step 1: generate the code 
    code = []
    tries = 12
    counter = 0
    while len(code) < 4:
        number = random.randint(1, 8)
        number = str(number)
        if number not in code:                                                                                  # making sure to append numbers that are not already in the list
            code.append(number)                                                                                 # so there is not duplication

    print("4-digit Code has been set."                                                                          # printing this string like this because of review guidelines
            " Digits in range 1 to 8. You have 12 turns to break it.")
    # step 2: Get a guess
    # step 3: Evaluate input
    # step 4: Count guesses
    while counter < tries:
        digits_correct_place = 0
        digits_not_correct_place = 0
        user_input = input("Input 4 digit code: ")

        if len(user_input) != 4 or user_input.isdigit() == False or "9" in user_input or "0" in user_input:     
            print("Please enter exactly 4 digits.")

        else:
            for element in range(len(code)):
                if code[element] == user_input[element]:
                    digits_correct_place += 1 
                
                elif user_input[element] in code:
                    digits_not_correct_place += 1
                    
            print(f"Number of correct digits in correct place:     {digits_correct_place}")
            print(f"Number of correct digits not in correct place: {digits_not_correct_place}")

            if "".join(code) != user_input:
                    tries -= 1
                    print(f"Turns left: {tries}")

            if "".join(code) == user_input:
                print("Congratulations! You are a codebreaker!")
                print(f'The code was: {"".join(code)}')
                break

if __name__ == "__main__":
    run_game()
    
    
