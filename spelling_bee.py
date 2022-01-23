''' New York Times Spelling Bee solver

Gets the letters from user console input, compiles the letters into a regex and
then reads through a word list file, comparing each word to the regex and
displays words that match the regex. (Disclaimer: Word list does not match
NYT's word list. NYT excludes many words for being too "obscene" or "obscure").
'''
import re


WORD_LIST = r'./wordlists/twl06.txt'


def get_letters(total_letters: int = 7) -> tuple[str, str]:
    ''' Get letters from user input
    '''
    required_letter = ""
    optional_letters = ""

    # get the required letter
    while True:
        print("Required letter: ")
        required_letter = input()

        if len(required_letter) == 1:
            break
        print("Invalid input. Expecting 1 letter.")

    # get optional letters
    while True:
        print("Optional letters: ")
        optional_letters = input()

        if len(optional_letters) == total_letters - 1:
            break
        print(f"Invalid input. Expecting {total_letters-1} letters.")

    return required_letter, optional_letters


def compile_regex(required_letter: str,
                  optional_letters: str) -> re.Pattern:
    ''' Compile the letters into a regex pattern
    '''
    return re.compile(
        f"^([{optional_letters}]*{required_letter}+[{optional_letters}]*)+$",
        re.RegexFlag.IGNORECASE
    )


def check_is_valid(word: str,
                   pattern: re.Pattern,
                   min_length: int = 4) -> bool:
    ''' Check if the given word is valid

    Args:
        word:           The word to be checked
        pattern:        Compiled regex pattern that the word must match
        min_length:     Minimum length for a word to be valid
    '''
    if len(word) < min_length:
        return False

    m = re.match(pattern, word)
    return m is not None


def main():
    ''' NYT Spelling Bee Solver
    '''
    required_letter, optional_letters = get_letters()
    pattern = compile_regex(required_letter, optional_letters)

    print("\nMatching words:")
    count = 0
    with open(WORD_LIST) as f:
        # read file, word by word
        for line in f:
            word = line.strip()  # trim whitespace
            if check_is_valid(word, pattern):
                print(word)
                count += 1

    print(f"{count} word(s) found.")


if __name__ == '__main__':
    main()
