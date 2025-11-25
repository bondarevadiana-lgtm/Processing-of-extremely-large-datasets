from src.core.job.mapper import Mapper
import string

VOWELS = "aeiouаеєиіїоуюя"

class WordCountMapper(Mapper):
    def map(self, record, emit):
        # Видаляємо розділові знаки
        record = record.translate(str.maketrans("", "", string.punctuation))
        for token in str(record).split():
            token = token.lower()
            emit("TOTAL_WORDS", 1)  # для загального підрахунку слів
            if len(token) > 5:
                emit("LONG_WORDS", 1)  # для слів довжиною > 5

            # Обчислюємо кількість голосних і приголосних
            vowels_count = sum(1 for c in token if c in VOWELS)
            consonants_count = len(token) - vowels_count

            # Відправляємо ключ як довжину слова
            emit(f"LENGTH_{len(token)}", (vowels_count, consonants_count))
