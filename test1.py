
scores = []

# Loop 4 times to collect 4 student scores
for i in range(4):
    score = float(input(f"Enter score {i + 1}: "))
    scores.append(score)



print("Scores list:", scores)
print("Data type:", type(scores))
print("Total count:", len(scores))


# ==========================================
# Task 3: Linear Search Implementation
# ==========================================
target = float(input("Enter target score to search: "))

found = False

for i in range(len(scores)):
    if scores[i] == target:
        print("Score found at index", i)
        found = True
        break

if not found:
    print("Score not found")