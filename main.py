import random
import string
from collections import Counter


# ==========================================
# PROJECT: NUMBER GUESSING GAME & WORD COUNTER
# ==========================================


# ------------------------------------------
# FUNCTION 1: NUMBER GUESSING GAME
# ------------------------------------------

best_score = 0


def number_guessing_game():

    global best_score

    while True:

        print("\n====================================")
        print("         NUMBER GUESSING GAME")
        print("====================================")

        print("\nI have selected a number between 1 and 100.")
        print("You have 10 attempts to guess it!")
        print("You will lose 10 points for each wrong guess.")

        # Generate random number
        secret_number = random.randint(1, 100)

        # Initialize variables
        attempts = 10
        score = 100
        guess_count = 0

        # Guessing loop
        while attempts > 0:

            try:

                guess = int(input("\nEnter your guess: "))

                # Validate number range
                if guess < 1 or guess > 100:

                    print("Please enter a number between 1 and 100.")
                    continue

                guess_count += 1
                attempts -= 1

                # Check the guess
                if guess == secret_number:

                    print("\nCongratulations! You guessed correctly!")
                    print("Secret Number:", secret_number)
                    print("Attempts Used:", guess_count)
                    print("Your Final Score:", score)

                    # Update best score
                    if score > best_score:
                        best_score = score

                    print("Best Score:", best_score)

                    break

                elif guess > secret_number:

                    print("Too High!")
                    score -= 10

                else:

                    print("Too Low!")
                    score -= 10

                print("Remaining Attempts:", attempts)

            except ValueError:

                print("Invalid input! Please enter a valid number.")

        else:

            print("\nGAME OVER!")
            print("The correct number was:", secret_number)
            print("Your Final Score:", score)

        # Replay option
        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower().strip()

        if play_again not in ["yes", "y"]:
            break


# ------------------------------------------
# FUNCTION 2: WORD COUNTER
# ------------------------------------------

def word_counter():

    print("\n====================================")
    print("             WORD COUNTER")
    print("====================================")

    filename = input(
        "\nEnter the filename (default: sample.txt): "
    ).strip()

    if filename == "":
        filename = "sample.txt"

    try:

        # Read text file
        with open(filename, "r", encoding="utf-8") as file:

            text = file.read()

        # Convert text into lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        # Split text into words
        words = text.split()

        # Count word frequency
        word_counts = Counter(words)

        # Display results
        print("\n====================================")
        print("          WORD COUNT RESULTS")
        print("====================================")

        print("\nTotal Words:", len(words))

        print("Unique Words:", len(word_counts))

        if not words:

            print("\nThe file is empty.")

        else:

            print("\nTop 10 Most Common Words")
            print("------------------------------------")

            print(f"{'Word':<20}{'Frequency':>10}")
            print("------------------------------------")

            for word, count in word_counts.most_common(10):

                print(f"{word:<20}{count:>10}")

        print("------------------------------------")

    except FileNotFoundError:

        print("\nError: File not found!")
        print("Please check the filename and try again.")

    except PermissionError:

        print("\nError: Permission denied while reading the file.")

    except Exception as e:

        print("\nAn unexpected error occurred:", e)


# ------------------------------------------
# FUNCTION 3: MAIN MENU
# ------------------------------------------

def main():

    while True:

        print("\n========================================")
        print("       PYTHON UTILITY APPLICATION")
        print("========================================")

        print("\n1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        print("\n========================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            number_guessing_game()

        elif choice == "2":

            word_counter()

        elif choice == "3":

            print("\nThank you for using Python Utility Application!")

            print("Have a great day!")

            break

        else:

            print("\nInvalid choice!")
            print("Please select 1, 2, or 3.")


# ------------------------------------------
# START THE APPLICATION
# ------------------------------------------

if __name__ == "__main__":

    main()