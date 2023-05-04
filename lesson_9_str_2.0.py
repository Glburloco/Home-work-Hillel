#task_1
word = input("Enter a word: ")
print("+" if word == word[::-1] else "-")

#task_2
text = input("Enter your text: ")
word = input("Enter a search term: ")
result = "YES" if word in text else "NO"
print(result)

#task_3
string = input("Enter your text: ")
result = string.replace("abc", "www") if string.startswith("abc") else string + "qqq"
print(result)

#task_4
text = input("Enter your text: ")
new_text = "".join(char for char in text if not char.isdigit())
print(new_text)

#task_5
email = input("Enter your email: ")
result = "YES" if "@" in email and "." in email else "NO"
print(result)

