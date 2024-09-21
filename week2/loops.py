# week 2 exercise - variables, conditions, loops

# exercise 1 - vowel counter

# take user input
user_string = input("enter a sentence: ").lower()

#list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#vowel counter
vowel_count = [0, 0, 0, 0, 0]

# iterate through each character in input
for each_char in user_string:
    if each_char in vowels:
        index = vowels.index(each_char)
        vowel_count[index] += 1
# display count of vowels
for i in range(len(vowels)):
    print(f'{vowels[i]} - {vowel_count[i]}')



