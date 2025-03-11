from typing import List
from collections import Counter
import string

def get_longest_diverse_words(file_path: str) -> List[str]:
    # Открываем файл и читаем его содержимое
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    
    #уникальные символы
    unique_words = [(word, len(set(word))) for word in words]
    
    #сортируем по количеству уникальных символов (по убыванию) и затем по длине слова (по убыванию)
    unique_words.sort(key=lambda x: (-x[1], -len(x[0])))
    
    #получаем 10 самых длинных слов
    return [word for word, _ in unique_words[:10]]

def get_rarest_char(file_path: str) -> str:

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    #счетчик
    char_count = Counter(text)
    
    #редкий символ (мин количество)
    rarest_char = min(char_count, key=char_count.get)
    return rarest_char

def count_punctuation_chars(file_path: str) -> int:

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    #кол-во знаков препинания
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    return punctuation_count

def count_non_ascii_chars(file_path: str) -> int:

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    #кол не-ASCII символов
    non_ascii_count = sum(1 for char in text if ord(char) > 127)
    return non_ascii_count

def get_most_common_non_ascii_char(file_path: str) -> str:

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    

    non_ascii_chars = [char for char in text if ord(char) > 127]
    if not non_ascii_chars:
        return '' 
    
    non_ascii_count = Counter(non_ascii_chars)
    
    #самый распространенный не-ascii символ
    most_common_char = non_ascii_count.most_common(1)[0][0]
    return most_common_char

longest_words = get_longest_diverse_words('data.txt')
rarest_char = get_rarest_char('data.txt')
punctuation_count = count_punctuation_chars('data.txt')
non_ascii_count = count_non_ascii_chars('data.txt')
most_common_non_ascii = get_most_common_non_ascii_char('data.txt')

print("длинные слова:")
for word in longest_words:
    print(f"- {word}")

print(f"\nредкий персонаж: {rarest_char}")
print(f"кол-во знаков препинания: {punctuation_count}")
print(f"Количество символов, не входящих в ascii: {non_ascii_count}")

if most_common_non_ascii:
    print(f"наиболее распространенный  символ: {most_common_non_ascii}")
else:
    print("не входящий в набор:")

# длинные слова:
# - Bev\u00f6lkerungsabschub,
# - unmi\u00dfverst\u00e4ndliche
# - r\u00e9sistance-Bewegungen,
# - Werkst\u00e4ttenlandschaft
# - Werkst\u00e4ttenlandschaft
# - Selbstverst\u00e4ndlich
# - Machtbewu\u00dftsein,
# - Entz\u00fcndbarkeit.
# - Br\u00fcckenschl\u00e4gen;
# - Millionenbev\u00f6lkerung

# редкий персонаж: Y
# кол-во знаков препинания: 8277
# Количество символов, не входящих в ASCII: 0
# не входящий в набор: