import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

initial_text = """The Toyota Chaser is a mid-size car produced by Toyota in Japan. It was primarily aimed at the domestic market 
and was known for its rear-wheel drive layout and sporty characteristics. The Chaser shared many of its components with other 
Toyota models, like the Cresta and the Mark II. Many enthusiasts appreciate the Chaser for its turbocharged engines and its 
ability to be tuned for high performance. Some versions of the Chaser became highly popular in the drift racing scene due to 
their balance and power delivery."""
file_path = "initial_text.txt"
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(initial_text)

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

words = word_tokenize(text.lower())

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in words]

stop_words = set(stopwords.words('english'))
words_filtered = [word for word in stemmed_words if word not in stop_words]

words_cleaned = [word for word in words_filtered if word.isalnum()]

processed_text = ' '.join(words_cleaned)
output_file_path = "processed_text.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(processed_text)

print(f"Оброблений текст записано у файл: {output_file_path}")
