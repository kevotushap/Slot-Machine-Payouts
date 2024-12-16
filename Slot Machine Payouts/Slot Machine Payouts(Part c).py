import random
import statistics

# Function to simulate a single slot machine spin outcome
def spin_result():
    outcome = [random.choice(['BAR', 'BELL', 'LEMON', 'CHERRY']) for _ in range(3)]  # Simulate 3 independent wheels
    
    # Determine payout based on the outcome
    if outcome == ['BAR', 'BAR', 'BAR']:
        return 20  # 20 coins for BAR BAR BAR
    elif outcome == ['LEMON', 'LEMON', 'LEMON']:
        return 15  # 15 coins for LEMON LEMON LEMON
    elif outcome == ['BELL', 'BELL', 'BELL']:
        return 5  # 5 coins for BELL BELL BELL
    elif outcome == ['CHERRY', 'CHERRY', 'CHERRY']:
        return 3  # 3 coins for CHERRY CHERRY CHERRY
    elif outcome[:2] == ['CHERRY', 'CHERRY']:
        return 2  # 2 coins for CHERRY CHERRY ?
    elif outcome[0] == 'CHERRY':
        return 1  # 1 coin for CHERRY ? ?
    else:
        return 0  # No payout

# Function to simulate until coins drop to zero
def simulate_until_zero(starting_coins=15):
    coins = starting_coins
    spins = 0  # Track number of spins
    
    while coins > 0:
        spins += 1
        coins -= 1  # Deduct 1 coin per spin
        payout = spin_result()  # Get payout based on the spin result
        coins += payout  # Add payout to the coins balance
    
    return spins

# Function to run multiple simulations and collect results
def simulate_spins_till_zero(num_simulations=10000, starting_coins=15):
    results = []
    
    for _ in range(num_simulations):
        spins = simulate_until_zero(starting_coins)
        results.append(spins)
    
    # Calculate mean and median
    mean_spins = sum(results) / len(results)
    median_spins = statistics.median(results)
    
    return mean_spins, median_spins, results

# Running the simulation
mean_spins, median_spins, results = simulate_spins_till_zero()

# Displaying the mean and median
print(f"Mean number of spins until coins drop to zero: {mean_spins}")
print(f"Median number of spins until coins drop to zero: {median_spins}")

# Optional: Show a sample of the first few results for verification
print(f"First 10 results: {results[:10]}")
