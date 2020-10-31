import random

HANGMAN = (
    """
------
|    |
|
|
|
|
|
|
|
--------
""",
    """
------
|    |
|    0
|
|
|
|
|
|
--------
""",
    """
------
|    |
|    0
|   -+-
|
|
|
|
|
--------
""",
    """
------
|    |
|    0
|  /-+-
|
|
|
|
|
--------
""",
    """
------
|    |
|    0
|  /-+-/
|
|
|
|
|
--------
""",
    """
------
|    |
|    0
|  /-+-/
|    |
|
|
|
|
--------
""",
    """
------
|    |
|    0
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""",
    """
------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
"""
    )

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("KAJOJINKA", "OBSZTYKULTYFIKIEWICZ", "SKOMPLIKOWANY", "FARES", "BURSZTYN")
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Witaj w grze 'Szubienica'. Powodzenia!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

    guess = input("\n\nWprowadź literę: ")
    guess = guess.upper()

    while guess in used:
        print("Już wykorzystałeś literę", guess)
        guess = input("Wprowadź literę: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nTak!", guess, "znajduje się w zagadkowym słowie!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety,", guess, "nie występuje w zagadkowym słowie.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostałeś powieszony!")
else:
    print("\nOdgadłeś!")
print("\nZagadkowe słowo to", word)

input("\n\nAby zakończyć progam, naciśnij kalwisz Enter.")
