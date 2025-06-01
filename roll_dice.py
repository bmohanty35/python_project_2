import random

def estimate_probability_of_six(trials=10000, rolls_per_trial=10):
    success_count = 0

    for _ in range(trials):
        found_six = False
        for _ in range(rolls_per_trial):
            if random.randint(1, 6) == 6:
                found_six = True
                break  # No need to continue this trial
        if found_six:
            success_count += 1

    probability = success_count / trials
    print(f"Estimated Probability of at least one '6' in {rolls_per_trial} rolls: {probability:.4f}")

# Run the estimation
estimate_probability_of_six()
