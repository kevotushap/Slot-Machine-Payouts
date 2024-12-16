import random

# Function to simulate the outcome of a single spin and calculate the payout
def spin_result():
    # Symbols available on each wheel
    symbols = ["BAR", "BELL", "LEMON", "CHERRY"]
    
    # Simulate a spin: randomly pick a symbol for each wheel
    wheel_outcome = [random.choice(symbols) for _ in range(3)]
    
    # Print the outcome for clarity (optional, can be removed in the final version)
    # print(f"Spin outcome: {wheel_outcome}")
    
    # Calculate the payout based on the outcome
    if wheel_outcome == ["BAR", "BAR", "BAR"]:
        return 20  # BAR BAR BAR pays 20 coins
    elif wheel_outcome == ["LEMON", "LEMON", "LEMON"]:
        return 15  # LEMON LEMON LEMON pays 15 coins
    elif wheel_outcome == ["BELL", "BELL", "BELL"]:
        return 5   # BELL BELL BELL pays 5 coins
    elif wheel_outcome == ["CHERRY", "CHERRY", "CHERRY"]:
        return 3   # CHERRY CHERRY CHERRY pays 3 coins
    elif wheel_outcome[0] == "CHERRY" and wheel_outcome[1] == "CHERRY":
        return 2   # CHERRY CHERRY ? pays 2 coins (only the first two wheels matter)
    elif wheel_outcome[0] == "CHERRY":
        return 1   # CHERRY ? ? pays 1 coin (only the first wheel matters)
    else:
        return 0   # No payout for any other combination

# Function to simulate John's day at the slot machine
def simulate_john_day(starting_coins=10):
    coins = starting_coins
    spins = 0
    
    # John plays until he runs out of coins or spins 50 times
    while coins > 0 and spins < 50:
        coins -= 1  # One coin per spin
        coins += spin_result()  # Add any winnings from the spin
        spins += 1
    
    # Return True if John comes home with more than 10 coins, False otherwise
    return coins > starting_coins

# Function to simulate John's month (30 days)
def simulate_john_month(num_days=30):
    successful_days = 0
    
    # Simulate 30 days of John's gameplay
    for _ in range(num_days):
        if simulate_john_day():
            successful_days += 1
    
    # Return the number of days he ends up with more than 10 coins
    return successful_days

# Function to simulate the results over multiple simulations
def simulate_multiple_simulations(num_simulations=10000):
    total_successful_days = 0
    
    # Simulate multiple months
    for _ in range(num_simulations):
        total_successful_days += simulate_john_month()
    
    # Calculate and return the average number of successful days over all simulations
    return total_successful_days / num_simulations

# Running the simulation
num_simulations = 10000
average_successful_days = simulate_multiple_simulations(num_simulations)

print(f"On average, John comes home with more than 10 coins on {average_successful_days:.2f} days out of 30.")

