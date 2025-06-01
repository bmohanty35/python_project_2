import random

def simulate_bag_draws(trials=1000):
    bag = ['Red'] * 5 + ['Green'] * 7 + ['Blue'] * 8
    draws = [random.choice(bag) for _ in range(trials)]

    count_prev_blue = 0
    count_red_given_prev_blue = 0
    count_red = 0
    count_prev_blue_given_red = 0

    for i in range(1, trials):
        prev, curr = draws[i-1], draws[i]

        if prev == 'Blue':
            count_prev_blue += 1
            if curr == 'Red':
                count_red_given_prev_blue += 1

        if curr == 'Red':
            count_red += 1
            if prev == 'Blue':
                count_prev_blue_given_red += 1

    # Estimated probabilities from simulation
    p_red_given_prev_blue = count_red_given_prev_blue / count_prev_blue if count_prev_blue else 0
    p_red = count_red / (trials - 1)
    p_prev_blue = count_prev_blue / (trials - 1)
    p_prev_blue_given_red = count_prev_blue_given_red / count_red if count_red else 0

    # Bayes' Theorem calculation
    bayes_p_red_given_prev_blue = (p_prev_blue_given_red * p_red) / p_prev_blue if p_prev_blue else 0

    # Results
    print(f"Simulation Results (from {trials} draws):")
    print(f"P(Red | Previous = Blue) ≈ {p_red_given_prev_blue:.4f}")
    print(f"Using Bayes' Theorem:         ≈ {bayes_p_red_given_prev_blue:.4f}")
    print(f"\nAdditional Stats:")
    print(f"P(Red):                       ≈ {p_red:.4f}")
    print(f"P(Previous = Blue):          ≈ {p_prev_blue:.4f}")
    print(f"P(Previous = Blue | Red):    ≈ {p_prev_blue_given_red:.4f}")

# Run simulation
simulate_bag_draws()
