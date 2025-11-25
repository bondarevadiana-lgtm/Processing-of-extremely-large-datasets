from src.core.job.reducer import Reducer

class WordCountReducer(Reducer):
    def reduce(self, key, values, emit):
        # Загальний підрахунок слів
        if key in ["TOTAL_WORDS", "LONG_WORDS"]:
            emit(key, sum(values))
        elif key.startswith("LENGTH_"):
            total_vowels = 0
            total_consonants = 0
            count_words = 0
            for v_count, c_count in values:
                total_vowels += v_count
                total_consonants += c_count
                count_words += 1

            total_letters = total_vowels + total_consonants
            if total_letters > 0:
                percent_vowels = (total_vowels / total_letters) * 100
                percent_consonants = (total_consonants / total_letters) * 100
            else:
                percent_vowels = percent_consonants = 0

            emit(key, {
                "percent_vowels": round(percent_vowels, 2),
                "percent_consonants": round(percent_consonants, 2),
                "words_count": count_words
            })
