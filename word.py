def sort_letters(word):
    vowels = "аеєиіїоуюяaeiouy"
    consonants = "бвгґджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"

    # Розділяємо голосні та приголосні
    vowels_in_word = [char for char in word if char.lower() in vowels]
    consonants_in_word = [char for char in word if char.lower() in consonants]

    # Виводимо голосні
    print("Голосні:")
    for vowel in vowels_in_word:
        print(vowel)

    # Виводимо приголосні
    print("Приголосні:")
    for consonant in consonants_in_word:
        print(consonant)


# Введіть слово
word = input("Введіть слово: ")
sort_letters(word)
