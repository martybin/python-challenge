from termcolor import colored


def print_success(text, end='\n\n'):
    print(colored(text, 'green', attrs=['reverse']), end=end)

def print_warning(text, end=' '):
    print(colored(text, 'yellow', attrs=['reverse']), end=end)

def print_invalid(text, end=' '):
    print(colored(text, 'light_grey', attrs=['reverse']), end=end)

def print_Error(text, end='\n\n'):
    print(colored(text, 'red', attrs=['reverse']), end=end)

def print_chance(text, end=' '):
    print(colored(text, 'cyan', attrs=['reverse']), end=end)

def print_last_chance(text, end=' '):
    print(colored(text, 'light_red', attrs=['reverse']), end=end)
