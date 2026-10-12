# Personal Information Manager

## Project Description

The Personal Information Manager is a beginner-level Python project that stores personal information, collects user preferences, and displays everything in a readable format.

## Project Objectives

- Learn how to use variables and data types.
- Understand Python input and output.
- Practice string formatting using f-strings.
- Validate user input.
- Perform basic calculations.

## Technologies Used

- Python 3
- Visual Studio Code or any Python editor
- Git and GitHub

## Project Structure

```text
week1-personal-info/
├── personal_info.py
├── README.md
├── test_inputs.txt
└── .gitignore
```

## Features

1. Stores name, age, city, and hobby.
2. Collects favorite food and favorite color.
3. Rejects empty user input.
4. Formats text using Python string methods.
5. Calculates age in months.
6. Displays information with clear separators.
7. Shows a welcome message and a goodbye message.

## Installation and Setup

1. Install Python 3 from https://www.python.org/downloads/.
2. Create a folder named `week1-personal-info`.
3. Create the `personal_info.py` file and add the program.
4. Open a terminal in the project folder.
5. Run the program using:

```bash
python personal_info.py
```

On some systems, use:

```bash
python3 personal_info.py
```

## Concepts Learned

- **Variables:** Store personal information.
- **Data types:** Use strings and integers.
- **Input/output:** Collect information using `input()` and display it using `print()`.
- **String formatting:** Display values using f-strings.
- **String methods:** Use `strip()`, `title()`, and `capitalize()`.
- **Loops:** Repeat input requests until valid information is entered.
- **Functions:** Reuse the input validation logic.
- **Arithmetic:** Calculate age in months using multiplication.

## Testing

The program should be tested with normal inputs, empty inputs, and inputs containing extra spaces.

Refer to `test_inputs.txt` for test scenarios.

## Challenges and Solutions

**Challenge 1: Empty input**

Solution: Used a `while` loop to ask the user again when the input is empty.

**Challenge 2: Inconsistent capitalization**

Solution: Used string methods to format names and preferences.

**Challenge 3: Displaying information clearly**

Solution: Used f-strings and separator lines.

## Expected Result

The program displays the stored personal information and the user's favorite food and color, along with the calculated age in months.

## Future Enhancements

- Allow the user to enter their name, age, city, and hobby dynamically.
- Validate age as a positive integer.
- Save the information to a text file.
- Add a menu for viewing or updating information.

## Author

VALLURUPALLI KEERTHANA