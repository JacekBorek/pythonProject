# odgadnij liczbę
guessnumber = 10
number = 0
while guessnumber != number:
    number = int(input("Type the number: "))

    if number == guessnumber:
        print("correct");
    elif number > guessnumber:
        print("wrong, your number is higher than target");
    elif number < guessnumber:
        print("wrong, your number is lower than target");

# try to add some clue
# set the number of attempts.
