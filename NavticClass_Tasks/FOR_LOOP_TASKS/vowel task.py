
user_word=input("enter the word:")
user_word=user_word.upper()
without_vowel_words = ""
vowel_word="AEIOU"
for letter in user_word:
    if letter in vowel_word:
       continue

    without_vowel_words+=letter
print(without_vowel_words)


