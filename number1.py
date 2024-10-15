import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

file_path = "whitman-leaves.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = word_tokenize(text.lower())
print(f"Кількість слів у тексті: {len(words)}")

stop_words = set(stopwords.words('english'))
words_filtered = [word for word in words if word.isalnum() and word not in stop_words]

word_counts = Counter(words)
most_common_words = word_counts.most_common(10)

words_to_plot = [word for word, count in most_common_words]
counts_to_plot = [count for word, count in most_common_words]

plt.bar(words_to_plot, counts_to_plot)
plt.title("10 найбільш вживаних слів у тексті (до фільтрації)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

filtered_word_counts = Counter(words_filtered)
most_common_filtered_words = filtered_word_counts.most_common(10)

filtered_words_to_plot = [word for word, count in most_common_filtered_words]
filtered_counts_to_plot = [count for word, count in most_common_filtered_words]

plt.bar(filtered_words_to_plot, filtered_counts_to_plot)
plt.title("10 найбільш вживаних слів після видалення стоп-слів та пунктуації")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()
