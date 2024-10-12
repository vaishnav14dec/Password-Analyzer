import re

def analyze_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*]", password):
        score += 1

    return score

password = input("Enter a password: ")
score = analyze_password(password)
if score == 5:
    print("Strong password!")
else:
    print("Weak password, consider adding more complexity.")
