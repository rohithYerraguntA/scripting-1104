# week 2 exercise - variables, conditions, loops

# exercise 1 - vowel counter

# take user input
user_string = input("enter a sentence: ")

#list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#vowel counter
vowel_count = [0, 0, 0, 0, 0]

# iterate through each character in input
for each_char in user_string:
    if each_char in vowels:
        index = vowels.index(each_char)
        vowel_count[index] += 1

print(vowel_count)


