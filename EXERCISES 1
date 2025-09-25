# -----------------------------
# Project: Sports Team Selector
# -----------------------------

# 1. Integers Section
# Let's say these are player scores or performance ratings
player_scores = [12, 18, 25, 10, 15]

total = sum(player_scores)
average = total / len(player_scores)
minimum = min(player_scores)
maximum = max(player_scores)

print("---- Integers ----")
print(f"Total Score: {total}")
print(f"Average Score: {average}")
print(f"Minimum Score: {minimum}")
print(f"Maximum Score: {maximum}")
print()

# 2. Strings Section
report = (
    f"The Sports Team Selector recorded a total of {total} points.\n"
    f"The average score per player is {average:.2f}."
)
print("---- Strings ----")
print(report)
print()

# 3. Booleans Section
# Threshold condition (let’s set it to 15)
threshold = 15

print("---- Booleans ----")
if average > threshold and maximum > 20:   # compound condition
    print("Above Standard")
else:
    print("Below Standard")
print()

# 4. Lists Section
print("---- Lists ----")
team_players = ["Alice", "Bob", "Charlie", "David"]

print("Original team:", team_players)

# Add a new player
team_players.append("Eva")
print("After adding Eva:", team_players)

# Remove one player based on a condition (remove if name starts with 'B')
for player in team_players:
    if player.startswith("Bob"):
        team_players.remove(player)
        break

print("After removing Bob:", team_players)

# Sort the list
team_players.sort()
print("Sorted team:", team_players)
print()

# 5. Arrays Section
import array

print("---- Arrays ----")
# Creating a numeric array with the same scores
score_array = array.array("i", player_scores)

# Compute sum
array_sum = sum(score_array)
list_sum = sum(player_scores)

print("Sum of array:", array_sum)
print("Sum of list :", list_sum)

if array_sum == list_sum:
    print("Array sum and List sum are equal.")
else:
    print("Array sum and List sum are NOT equal.")
print()

# 6. Dictionaries Section
print("---- Dictionaries ----")
players_data = [
    {"id": 1, "name": "Alice", "value": 12},
    {"id": 2, "name": "Bob", "value": 18},
    {"id": 3, "name": "Charlie", "value": 25},
]

print("Original records:", players_data)

# Update one record (change Bob's value to 20)
for record in players_data:
    if record["name"] == "Bob":
        record["value"] = 20

# Delete another (remove Charlie)
players_data = [record for record in players_data if record["name"] != "Charlie"]

# Compute total of values
total_value = sum(record["value"] for record in players_data)

print("Updated records:", players_data)
print("Total value after update:", total_value)
