# Probability Calculator for N-sided Dice

## Overview
This Python program calculates the probability distribution when rolling M number of N-sided dice. It simulates rolling the dice multiple times and calculates the probability of each possible sum. The program includes a user interface for inputting values and displaying the results, as well as test functions to ensure correct functionality.

## Features
- Simulates rolling M N-sided dice once and returns the sum of the outcomes.
- Simulates rolling M N-sided dice K times and records the results.
- Calculates the probability of each possible sum when M N-sided dice are rolled K times.
- Provides a user interface for inputting values and displaying the probability distribution.
- Option to continue or quit the program after each calculation.

## Installation
1. Ensure you have Python installed on your system.
2. Clone this repository or download the source code.
3. Navigate to the directory containing the source code.

## Usage
1. Run the script using the following command:
    ```bash
    python probability_calc.py
    ```
2. Follow the prompts to input the number of sides on the dice (N), the number of dice to roll (M), and the number of times to roll the dice (K).
3. The program will display the probability distribution of the possible sums.
4. After the results are displayed, you will be prompted to perform another calculation or quit the program.

## Examples
### Normal Cases
#### Case 1
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

#### Case 2
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

#### Case 3
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

### Edge Cases
#### Case 1
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

#### Case 2
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

#### Case 3
- **Input:**
  - Number of sides on the dice (N): *enter number*
  - Number of dice to roll (M): *enter number*
  - Number of times to roll the dice (K): *enter number*

## Testing
The script includes several test functions to verify the correctness of the program:
- `test_dice_roll()`: Tests the `roll_dice_once` function with normal and edge cases.
- `test_simulate_rolls()`: Tests the `simulate_rolls` function with normal and edge cases.
- `test_probability_distribution()`: Tests the `calculate_probability_distribution` function with normal and edge cases.

These tests are automatically run when you execute the script.