import random

# --- Coin Toss Simulation ---
def simulate_coin_tosses(n=10000):
    heads = 0
    tails = 0

    for _ in range(n):
        if random.choice(['Heads', 'Tails']) == 'Heads':
            heads += 1
        else:
            tails += 1

    prob_heads = heads / n
    prob_tails = tails / n

    print("Coin Toss Simulation:")
    print(f"Total Tosses: {n}")
    print(f"Heads: {heads} ({prob_heads:.4f})")
    print(f"Tails: {tails} ({prob_tails:.4f})\n")

# --- Dice Roll Simulation ---
def simulate_dice_rolls(n=10000):
    sum_7 = 0

    for _ in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            sum_7 += 1

    prob_sum_7 = sum_7 / n

    print("Dice Roll Simulation:")
    print(f"Total Rolls: {n}")
    print(f"Sum = 7 occurred: {sum_7} times")
    print(f"Probability of sum 7: {prob_sum_7:.4f}")

# Run simulations
simulate_coin_tosses()
simulate_dice_rolls()
