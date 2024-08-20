"""PROBLEM 10

Define a function which counts vowels and consonants in a word.

Test case 1
Input : pythonlobby
Output :  
vowel : 2 
Consonants: 9

Test case:2
Input : sabudhfoundation
Output : 
vowel : 7
Constants: 9 """


def count_vowels_consonants(s):
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count, consonant_count


word = input()
print(f"vowel : {count_vowels_consonants(word)[0]}")
print(f"Consonants : {count_vowels_consonants(word)[1]}")
