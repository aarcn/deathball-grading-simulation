from collections import Counter
import random

grading_chances = {"No Grade": (0.2, "A"),
                   "A": (0.25, "A+"),
                   "A+": (0.3333, "S")}

num_simulations = 1000000


def sim_til_s_grade():
    attempts = 0
    successful_upgrade = False

    while not successful_upgrade:
        current_grade = "No Grade"
        while current_grade != "S":
            attempts += 1
            chance, next_grade = grading_chances[current_grade]

            success = random.random() < chance
            if success:
                current_grade = next_grade
            else:
                break
        if current_grade == "S":
            successful_upgrade = True

    return attempts


def freq_table(num_of_simulations):
    results = [sim_til_s_grade() for _ in range(num_of_simulations)]
    frequency_table = Counter(results)

    print(f"Frequency table after {num_of_simulations} simulations:")
    print("Attempts | Frequency | Percentage")
    print("----------------------------------")
    cumulative_percentage = 0
    for attempts, frequency in sorted(frequency_table.items()):
        percentage = (frequency / num_of_simulations) * 100
        print(f"{attempts:<5} | {frequency:<9} | {percentage:.5f}%")

        if attempts <= 59:
            cumulative_percentage += percentage

    print("\nCumulative percentage (1 to 59):", f"{cumulative_percentage:.5f}%")


freq_table(num_simulations)
