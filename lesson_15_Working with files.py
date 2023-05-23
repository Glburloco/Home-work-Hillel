# Task_1
import re
import random
import string

filename = 'text_file.txt'
def generate_random_text_with_numbers(length, num_digits):
    text = ''.join(random.choices(string.ascii_lowercase, k=length))
    digit_positions = random.sample(range(length), num_digits)

    for pos in digit_positions:
        text = text[:pos] + random.choice(string.digits) + text[pos+1:]

    return text

random_text = generate_random_text_with_numbers(50, 10)

with open(filename, 'w') as file:
    file.write(random_text)

numbers = []
with open(filename, 'r') as file:
    text = file.read()
    numbers = re.findall(r'\d+', text)

print("Random text with numbers:", random_text)
print("Found numbers:", numbers)

# Task_2

file_name = 'data.txt'

text = input("Enter you text: ")
with open(file_name, 'w') as file:
    file.write(text)

print("The file", file_name, "was created successfully.")


#Task_3
N = int(input("Enter the number of numbers: "))
numbers = []
for i in range(N):
    number = input(f"Enter number {i+1}: ")
    numbers.append(number)

filename = 'numbers.txt'
with open(filename, 'w') as file:
    file.write(' '.join(numbers))

# Task_4
import random

numbers = [str(random.randint(1, 1000)) for _ in range(100)]
filename = 'random_numbers.txt'
with open(filename, 'w') as file:
    file.write('\n'.join(numbers))

# Task_5
ftext = input("Enter you text: ")

with open('example.txt', 'w') as file:
    file.write(ftext)

with open('example.txt', 'r') as file:
    ftext = file.read()
    word_count = len(ftext.split())

print("Number of words in the text:", word_count)

# Task_6
def sum_numbers_in_file(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        text = file.read()
        numbers = text.split()
        for number in numbers:
            total_sum += int(number)
    return total_sum

filename = 'numbers.txt'
sum_of_numbers = sum_numbers_in_file(filename)
print("Sum of numbers:", sum_of_numbers)

# Task_7
from collections import Counter

filename = 'text_file.txt'

with open(filename, 'r') as file:
    text = file.read()

words = text.split()

counter = Counter(words)

top_words = counter.most_common(5)
for word, count in top_words:
    print(f"'{word}' - {count} разів")




