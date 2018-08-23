"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = int(input("Enter score: "))

if score  >= 0 and score <= 49:
    print("Bad")
elif score >= 50 and score <= 89:
    print("Passable")
elif score >= 90 and score <= 100:
    print("Excellent")
else:
    score < 0 and score > 100
    print("Invalid score")