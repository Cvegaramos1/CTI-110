
# Carlos Vega

# 7/11/2024

# P4HW1

# The program will use a loop to collect each score

# and display a letter grade for the calculated average.

score_num = int(input("How many scores do you want to enter? "))

print()
scores = []

for num in range(1, score_num + 1):
    score = float(input("Enter score #" + str(num) + ": "))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) + " again: "))
    scores.append(score)


lowest = min(scores)
scores_modified = scores
scores_modified.remove(lowest)
avg = sum(scores_modified)/ len(scores_modified)

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print("\n--------------Results-----------")
print("Lowest Score  : {}".format(lowest))
print("Modified List : {}".format(scores_modified))
print("Scores Average: {:.2f}".format(avg))
print("Grade         : {}".format(grade))
print("----------------------------------")







