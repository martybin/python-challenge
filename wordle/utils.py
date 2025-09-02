from termcolor import colored

class preprocessor:
    
    def __init__(self, file_path):
        self.file_path = 'words_freq.txt'

    def Generate_Words(self, limit=10000, word_len=5):

        words_freqs = []
        # extracting the words and frequencies from file path
        with open(self.file_path) as f:
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

    def print_success(text, end=' '):
        print(colored(text, 'green', attrs=['reverse']), end=end)

    def print_warning(text, end=' '):
        print(colored(text, 'yellow', attrs=['reverse']), end=end)

    def print_invalid(text, end=' '):
        print(colored(text, 'grey', attrs=['reverse']), end=end)

    def print_Error(text, end=' '):
        print(colored(text, 'red', attrs=['reverse']), end=end)

    def print_chance(text, end=' '):
        print(colored(text, 'cyan', attrs=['reverse']), end=end)

    def print_last_chance(text, end=' '):
        print(colored(text, 'light_red', attrs=['reverse']), end=end)
