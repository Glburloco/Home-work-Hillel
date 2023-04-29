password = input("Enter you password: ")

score = 0
recommendation = []

if len(password) >= 8:
    score += 1
else:
    recommendation.append("The minimum password length is 8")

if any(char.isdigit() for char in password):
    score += 1
else:
    recommendation.append("Use digits")

if any(char.isupper() for char in password):
    score += 1
else:
    recommendation.append("Use capital letters")

if any(char.islower() for char in password):
    score += 1
else:
    recommendation.append("Use lowercase letters")

spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*",
              "(", ")", "-", "+", "=", "/", "?", ".",
              ",", "_"]
if any(char in spec_chars for char in password):
    score += 1
else:
    recommendation.append("Use special characters")

print("Password score:{score}"" in 5")
if recommendation:
    print("Recommendation:\n"+"\n".join(recommendation))
