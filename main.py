def next_question():
    print("\nLet's continue with you next question:")

    print("""Someone who strongly asserts a position is often said to be "putting his" what down?
A: Foot
B: Head
C: VCR remote
D: Money """)

    answer = "A"

    choice = input("You choice: ").upper()

    if answer == choice:
        print("\nCongratulation you won 10 000$")
    else:
        try_again()


def try_again():
    print("""\nYou lose!\nDo you want to restart the game?
    Type 'Y' for yes
    Type anything you want for EXIT
    """)
