import string
import locale


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
    exit(1)

sentences = text.split('.')

if len(sentences) > 0:
    first_sentence = sentences[0]
    print(f"Перше речення: {first_sentence}")

words = remove_punctuation(text).split()

ukrainian_words = [word for word in words if any(
    char.isalpha() for char in word) and all(ord(char) >= 128 for char in word)]
english_words = [word for word in words if any(
    char.isalpha() for char in word) and all(ord(char) < 128 for char in word)]


locale.setlocale(locale.LC_COLLATE, 'uk_UA.UTF-8')

ukrainian_words = sorted(ukrainian_words, key=locale.strxfrm)
english_words = sorted(english_words, key=lambda word: word.lower())

print("\nСлова в алфавітному порядку:")
for word in ukrainian_words + english_words:
    print(word)

word_count = len(words)
print(f"\nКількість слів у тексті: {word_count}")
