import random
from utils import (
    print_success,
    print_warning,
    print_invalid,
    print_Error,
    print_chance,
    print_last_chance,
    )


class Wordle:

    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000):
        self.word_len = word_len
        self.words = self.Generate_Words(file_path, word_len, limit)

    def Generate_Words(self, file_path: str, word_len: int, limit: int):
        """
        Generate top words (top `limit` words) that have word_len letters.

        :param file_path: Words frequency data txt file
        :param word_len: Word length (M)
        :param limit: Top N words
        :return: List of words
        """
        words_freqs = []
        # extracting the words and frequencies from file path
        with open(file_path) as f:
            for line in f:         
                word, frequency = line.split(',')
                frequency = int(frequency)
                words_freqs.append((word, frequency))

        # limit my list for only 1000 first words and frequencies
        words_freqs = words_freqs[:limit]
        
        # sorting the list from most popular to less one
        w_freq = sorted(words_freqs, key=lambda freq: freq[1], reverse=True)

        # seprating words from frequencies
        seprated_words = [word.upper() for word, frequencies in w_freq]
        
        # select top 1000, 5 letters words
        words = list(filter(lambda w: len(w) == word_len, seprated_words))
        
        return words

    def check_word(self, User_guess: str, the_word: str):

        for w_letter, g_letter in zip(the_word, User_guess):
            # valid letter
            if w_letter == g_letter:
                print_success(f' {g_letter} ', end=' ')
                print(' ', end='')
    
            # valid letter in incorrect place
            elif g_letter in the_word:
                print_warning(f' {g_letter} ', end=' ')
                print(' ', end='')

            #invalid letter
            else:
                print_invalid(f' {g_letter} ', end=' ')
                print(' ', end='')

    def run(self, ):
        # Random Word
        random.seed(random.randint(1, 100_000))
        the_word = random.choice(self.words)
        the_word = the_word.upper()

        # Start Game
        try_number = 6
        success = False

        while try_number > 0:
            User_guess = input(f'Enter 5 letter word or you can exit: ')
            User_guess = User_guess.upper()
            
            if User_guess == 'EXIT':
                break
            
            #check length of word
            elif len(User_guess) != 5:
                print(f'Your word length is longer than the allowed limit! Please enter a word with 5 letters.')
                print()
                continue

            # check the word validity
            if User_guess not in self.words:
                print_Error(f'word is not exist!!')
                continue

            self.check_word(User_guess, the_word)

            # Check if the user guess is correct
            if User_guess == the_word:
                print()
                print()
                print_success('congradulations! you could find the correct word!')
                success = True
                break

            # Provide feedback on the user's guess
            if (try_number - 1) > 1:
                print_chance(f'you have {try_number - 1} times chance to guess the word!')
                print()
                print()

            elif (try_number - 1) == 1:
                print_last_chance(f'you have only {try_number - 1} more chance to guess the word!!')
                print()
                print()

            try_number -= 1

        if not success:
            print(end='\n\n')
            print(f'Game over. the correct answer is {the_word}')
            print(end='\n')
