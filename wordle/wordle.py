import random
from termcolor import colored
from utils.preprocessor import (
    Generate_Words,
    print_success,
    print_warning,
    print_invalid,
    print_Error,
    print_chance,
    print_last_chance,
)


class Wordle:

    def main():
        GN = Wordle()
        words = GN.Generate_Words()
        random.seed(69)
        the_word = random.choice(words)

        try_number = 6
        success = False

        while try_number > 0:
            User_guess = input(f'Enter 5 letter word or you can exit: ')
            User_guess = User_guess.upper()
            
            if User_guess == 'EXIT':
                break
            #check length of word
            elif len(User_guess) != 5:
                print(f'Your word is not appropriate! please enter 5 letter word')
                continue
                
            if User_guess not in words:
                print_Error(f'word is not exist!!')
                continue

            the_word = the_word.upper()

            for g_letter, w_letter in zip(User_guess, the_word):
                # valid letter
                if w_letter == g_letter:
                    print_success(f' {g_letter} ', end=' ')
                
                # valid letter in incorrect place
                elif g_letter in the_word:
                    print_warning(f' {g_letter} ', end=' ')
                    
                #invalid letter
                else:
                    print_invalid(f' {g_letter} ', end=' ')

            if User_guess == the_word:
                print()
                print()
                print_success('congradulations! you could find the correct word!')
                success = True
                break

            if (try_number - 1) > 1:
                print_chance(f'you have {try_number - 1} times chance to guess the word!')
                print()
                print()

            elif (try_number - 1) == 1:
                print_last_chance(f'you have only {try_number - 1} more chance to guess the word!!')
                print()
                print()

            try_number -= 1
            continue

        if not success:
            print()
            print(f'Game over. the correct answer is {the_word}')



if __name__ == '__main__':
    main()
