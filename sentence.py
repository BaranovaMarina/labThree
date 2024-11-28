def count_letters_in_words(sentence):
    # Розділяємо речення на слова
    words = sentence.split()

    # Перебираємо слова і рахуємо кількість літер у кожному
    word_lengths = {word: len([char for char in word if char.isalpha()]) for word in words}

    # Виводимо результати
    print("Кількість літер у кожному слові:")
    for word, length in word_lengths.items():
        print(f"{word}: {length}")


# Введіть речення
sentence = input("Введіть речення: ")
count_letters_in_words(sentence)
