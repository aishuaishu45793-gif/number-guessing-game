# 🎮 Number Guessing Game & Word Counter

## 📌 Project Overview

The **Number Guessing Game & Word Counter** is a Python-based utility application that combines two interactive features in one program.

1. **Number Guessing Game:** The computer randomly selects a number between 1 and 100. The user must guess the number within 10 attempts. The program provides hints such as "Too High!" or "Too Low!" and calculates the final score.

2. **Word Counter:** The user can provide a text file, and the program analyzes its contents to display the total number of words, unique words, and the 10 most frequently used words.

This project demonstrates Python fundamentals, including loops, conditional statements, functions, file handling, exception handling, and built-in modules.

## ✨ Features

### 🎯 Number Guessing Game
- Generates a random number between 1 and 100.
- Provides a maximum of 10 attempts.
- Displays hints when the guess is too high or too low.
- Deducts 10 points for every incorrect valid guess.
- Displays the final score.
- Tracks the best score during the current program session.
- Allows users to play multiple rounds.

### 📊 Word Counter
- Reads text from a `.txt` file.
- Converts text to lowercase.
- Removes punctuation.
- Counts total words and unique words.
- Displays the top 10 most frequently used words.
- Handles missing files and invalid file access.

### 🖥️ Main Menu
- Simple menu-driven interface.
- Allows users to select either feature.
- Provides an option to exit the application.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Modules:**
  - `random` – Generates random numbers.
  - `string` – Handles punctuation removal.
  - `collections.Counter` – Counts word frequencies.

## 📂 Project Structure

```text
Number-Guessing-Word-Counter/
│
├── main.py
├── sample.txt
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/aishuaishu45793-gif/number-guessing-game.git
```

### Step 2: Open the Project Folder

```bash
cd number-guessing-game
```

### Step 3: Run the Python Program

```bash
python main.py
```

No external libraries are required because the project uses Python's built-in modules.

## ▶️ How to Use

1. Run `main.py`.
2. Select an option from the main menu:

   - Enter `1` to play the Number Guessing Game.
   - Enter `2` to use the Word Counter.
   - Enter `3` to exit.

3. Follow the instructions displayed on the screen.

### Example: Number Guessing Game

```text
I have selected a number between 1 and 100.
You have 10 attempts to guess it!

Enter your guess: 50
Too Low!
Remaining Attempts: 9

Enter your guess: 75
Too High!
Remaining Attempts: 8

Enter your guess: 63
Congratulations! You guessed correctly!

Attempts Used: 3
Your Final Score: 80
```

### Example: Word Counter

```text
Enter the filename (default: sample.txt):

====================================
          WORD COUNT RESULTS
====================================

Total Words: 30
Unique Words: 20

Top 10 Most Common Words
------------------------------------
Word                 Frequency
------------------------------------
python                       5
programming                  3
is                            3
learning                      2
```

*Note: The example output is illustrative; actual results depend on the input file and random guesses.*

## 🧠 Python Concepts Demonstrated

- Variables and data types
- Functions
- Conditional statements
- Loops
- Random number generation
- File handling
- Exception handling
- String manipulation
- Lists and dictionaries
- Word frequency analysis
- Python standard library modules

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building interactive Python applications.
- Implementing game logic and scoring systems.
- Reading and processing text files.
- Analyzing word frequency using `Counter`.
- Handling invalid user inputs and file errors.
- Organizing code using functions and a menu-driven structure.

## 👩‍💻 Author

**Aishwarya**

GitHub: [aishuaishu45793-gif](https://github.com/aishuaishu45793-gif)

## 🔗 Project Repository

[Number Guessing Game & Word Counter](https://github.com/aishuaishu45793-gif/number-guessing-game)

---

⭐ If you find this project useful, feel free to explore the repository!
