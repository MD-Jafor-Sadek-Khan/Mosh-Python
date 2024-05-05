"""exercise"""

sentence = "This is a common interview question"


# initial solution
count = 0
most_repeated_letter = ""

for letter in sentence:
    check_count = sentence.count(letter)
    if check_count > count:
        count = check_count
        most_repeated_letter = letter
print((most_repeated_letter, count))

# optimized solution
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_frequency = sorted(char_frequency.items(),
                          key=lambda pair: pair[1], reverse=True)

print(sorted_frequency[0])
