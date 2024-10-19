import random

# Simulate 200 fair coin flips
flip_results = [random.choice(["Heads", "Tails"]) for _ in range(10000000)]

# Count the occurrences of heads and tails
heads_count = flip_results.count("Heads")
tails_count = flip_results.count("Tails")

# Display the results
print(f"Heads: {heads_count}, Tails: {tails_count}")