# Bagels, a deductive logic game.
# by John Banda adrielbanda4@gmail.com

import random

def guess_result(num, pos, correct_ans):
    if (correct_ans[pos] == num):
        return "Fermi"
    elif (num in correct_ans):
        return "Pico"
    else:
        return "Bagels"

def init_answer(no_of_digits):
    answer = []
    for i in range(no_of_digits):
        random.seed()
        if (i == 0):
            answer.append(random.randint(1, 9))
        else:
            answer.append(random.randint(0, 9))
    return answer


# Print the result
def validate_input(user_input, correct_answer):

    bagels_dict     = \
    {
        "Fermi":    0, 
        "Pico":     0, 
        "Bagels":   0
    }

    for i, num in enumerate(user_input):
        result = guess_result(int(num), i, correct_answer)
        bagels_dict[result] += 1

    game_won = False


    if (bagels_dict["Fermi"] == 3):
        print("You got it!")
        game_won = True
    elif (bagels_dict["Bagels"] == 3):
        print("Bagels")
    else:
        ret_str = ''
        ret_str += ("Fermi " * bagels_dict["Fermi"])
        ret_str += ("Pico " * bagels_dict["Pico"])
        print(str.strip(ret_str))

    return game_won

# Here we have to initialise the string
max_guesses  = 10
guess_no     = 1
answer_found  = False
continue_game = True

while (continue_game is True):
    guess_no = 1
    correct_answer = init_answer(3)
    print(correct_answer)

    while (answer_found is not True and guess_no <= max_guesses):
        user_input      = input("Guess #{0}: ".format(guess_no))
        answer_found    = validate_input(list(user_input), correct_answer)
        guess_no += 1
    
    print() 
    response = input("Do you want to play again? (yes or no) ")

    if ('Y' in str.upper(response)):
        continue_game = True
    else:
        continue_game = False
        if answer_found is False:
            s = ''.join(str(num) for num in correct_answer)
            print("The correct answer was: {0}".format(s))
            print()

# Game ends here
print("Thank you for playing Bagels :)")



