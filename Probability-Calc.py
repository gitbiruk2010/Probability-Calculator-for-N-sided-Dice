import random
from collections import Counter

def roll_dice_once(M, N):
    """Simulates rolling M N-sided dice once and returns the sum of the outcomes."""
    if M == 0:
        return 0
    # Generate M random numbers between 1 and N, sum them up and return the total
    return sum(random.randint(1, N) for _ in range(M))

def simulate_rolls(M, N, K):
    """Simulates rolling M N-sided dice K times and records the results."""
    # Create a list of results by rolling the dice K times
    results = [roll_dice_once(M, N) for _ in range(K)]
    return results

def calculate_probability_distribution(M, N, K):
    """Calculates the probability of each possible sum when M N-sided dice are rolled K times."""
    results = simulate_rolls(M, N, K)
    count = Counter(results)  # Count the frequency of each sum
    total = len(results)
    # Calculate the probability distribution for each possible outcome
    distribution = {outcome: count.get(outcome, 0) / total for outcome in range(M, M * N + 1)}
    return distribution

def main():
    while True:
        try:
            # User input for number of sides, number of dice, and number of rolls
            N = int(input("Enter the number of sides on the dice (N): "))
            M = int(input("Enter the number of dice to roll (M): "))
            K = int(input("Enter the number of times to roll the dice (K): "))

            # Validate inputs to ensure they are positive integers
            if N <= 0 or M < 0 or K <= 0:
                print("Please enter positive values for N and K, and non-negative value for M.")
                continue

            # Calculate and display the probability distribution
            distribution = calculate_probability_distribution(M, N, K)
            print("\nProbability Distribution:")
            for outcome in sorted(distribution.keys()):
                print(f"Sum {outcome}: {distribution[outcome]:.4f}")
        except ValueError:
            # Handle invalid input
            print("Please enter valid integer values for N, M, and K.")
        
        # Ask the user if they want to continue or quit
        choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the Probability Calculator!")
            break

def test_dice_roll():
    """Tests the roll_dice_once function with normal and edge cases."""
    # Normal cases
    assert 2 <= roll_dice_once(2, 6) <= 12, "Normal Case 1 Failed"
    assert 3 <= roll_dice_once(3, 4) <= 12, "Normal Case 2 Failed"
    assert 1 <= roll_dice_once(1, 12) <= 12, "Normal Case 3 Failed"
    
    # Edge cases
    assert 1 <= roll_dice_once(1, 1) <= 1, "Edge Case 1 Failed"
    assert 10 <= roll_dice_once(10, 1) <= 10, "Edge Case 2 Failed"
    assert roll_dice_once(0, 6) == 0, "Edge Case 3 Failed"
    
    print('=' * 50)
    print("\t** Probability Calculator for N-sided Dice - AD315 **")
    print('=' * 50)
    print("Dice Roll Test Cases OK")

def test_simulate_rolls():
    """Tests the simulate_rolls function with normal and edge cases."""
    # Normal cases
    results = simulate_rolls(2, 6, 100)
    assert len(results) == 100, "Normal Case 1 Failed"
    assert all(2 <= result <= 12 for result in results), "Normal Case 2 Failed"
    
    results = simulate_rolls(3, 4, 50)
    assert len(results) == 50, "Normal Case 3 Failed"
    assert all(3 <= result <= 12 for result in results), "Normal Case 4 Failed"
    
    # Edge cases
    results = simulate_rolls(1, 1, 10)
    assert len(results) == 10, "Edge Case 1 Failed"
    assert all(result == 1 for result in results), "Edge Case 2 Failed"
    
    results = simulate_rolls(10, 1, 10)
    assert len(results) == 10, "Edge Case 3 Failed"
    assert all(result == 10 for result in results), "Edge Case 4 Failed"
    
    results = simulate_rolls(0, 6, 10)
    assert len(results) == 10, "Edge Case 5 Failed"
    assert all(result == 0 for result in results), "Edge Case 6 Failed"
    
    print("Simulate Rolls Test Cases OK")

def test_probability_distribution():
    """Tests the calculate_probability_distribution function with normal and edge cases."""
    # Normal cases
    distribution = calculate_probability_distribution(2, 6, 10000)
    assert abs(distribution[2] - 1 / 36) < 0.01, "Normal Case 1 Failed"
    assert abs(distribution[7] - 6 / 36) < 0.01, "Normal Case 2 Failed"
    assert abs(distribution[12] - 1 / 36) < 0.01, "Normal Case 3 Failed"
    
    # Edge cases
    distribution = calculate_probability_distribution(1, 1, 10000)
    assert abs(distribution[1] - 1.0) < 0.01, "Edge Case 1 Failed"
    
    distribution = calculate_probability_distribution(10, 1, 10000)
    assert abs(distribution[10] - 1.0) < 0.01, "Edge Case 2 Failed"
    
    distribution = calculate_probability_distribution(0, 6, 10000)
    assert abs(distribution[0] - 1.0) < 0.01, "Edge Case 3 Failed"
    
    print("Probability Distribution Test Cases OK")
    print('=' * 50)

if __name__ == "__main__":
    # Run test cases first
    test_dice_roll()
    test_simulate_rolls()
    test_probability_distribution()
    
    # Run the main program
    main()
