import random

flip_results = [random.choice(["Heads", "Tails"]) for _ in range(8000)]
heads_count = flip_results.count("Heads")
tails_count = flip_results.count("Tails")
print(f"Heads: {heads_count}, Tails: {tails_count}")
print(round((heads_count * 100) / 8000, 4))
print(round((tails_count * 100) / 8000, 4))