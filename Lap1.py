# Ask for user input
# def get_score(subject):
#     while True:
#         try:
#             score = float(input(f"Enter {subject} score (0-100): "))
#             if 0 <= score <= 100:
#                 return score
#             else:
#                 print("❌ Score must be between 0 and 100. Try again.")
#         except ValueError:
#             print("⚠️ Please enter a valid number.")

def score(score):
    while True:
        try:
            score = float(input(f"Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("❌ Score must be between 0 and 100. Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def grand(total):
    if total >= 90:
        return "A"
    elif total >= 80:
        return "B"
    elif total >= 70:
        return "C"
    elif total >= 60:
        return "D"
    else:
        return "F"

name = input("Enter your name: ")
math = score("Math")
physics = score("Physics ")
history = score("History")
khmer = score("Khmer")


total = math + physics + history + khmer
average = total / 4
# print("Your Grade is : " + grand(average))
print(f"Hello {name}, your total score is {total} and your average score is {average:.2f}.")



