import random  
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()
def play(word):
    word_completion = "_" * len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("Spēlējam karātavas!")
    print(display_hangman(tries))
    new_func(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Mini vienu burtu vai vārdu: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Jau minēji šo burtu:", guess)
            elif guess not in word:
                print(guess, "nav vārdā.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Malacis,", guess, "ir vārdā!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(guess, "ir vārds, kuru jau minēji.")
            elif guess != word:
                print(guess, "nav šis vārds.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Nav pareizs minējums.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Malacis, tu uzminēji vārdu!")
    else:
        print("Tu neuzminēji. Vārds bija " + word + ". Varbūt nākamreiz!")

def new_func(word_completion):
    print(word_completion)

def display_hangman(tries):
    stages = [
        """
              -------------
              |            |
              |            O
              |           \|/
              |            |
              |           / \\
              |
             / \\
        """,
        """
              -------------
              |            |
              |            O
              |           \|/
              |            |
              |           / 
              |
             / \\
        """,
        """
              -------------
              |            |
              |            O
              |           \|/
              |            |
              |            
              |
             / \\
        """,
        """
              -------------
              |            |
              |            O
              |           \|/
              |            
              |            
              |
             / \\
        """,
        """
              -------------
              |            |
              |            O
              |            |
              |            
              |            
              |
             / \\
        """,
        """
              -------------
              |            |
              |            O
              |            
              |            
              |            
              |
             / \\
        """,
        """
              -------------
              |            |
              |            
              |            
              |            
              |            
              |
             / \\
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Vēlies mēģināt vēlreiz? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
