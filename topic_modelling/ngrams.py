import os
import pdfplumber
from preprocessing import preprocess_text_list
from collections import Counter
from nltk import ngrams

# The path of the data (chapters)
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def read_pdf_directory(directory):
    """
    Reads the pdf files and turns them into string.
    :param directory: The data directory
    :return: A string as a result of reading the files
    """
    corpus = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):  # More file extensions can be added if preferred.
            filepath = os.path.join(directory, filename)
            with pdfplumber.open(filepath) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                corpus.append(text)
    return corpus


# Our corpus as a string
corpus = read_pdf_directory(data_dir)

# Preprocessing
prepared_corpus = preprocess_text_list(corpus)

def extract_ngrams(corpus, n, top_n):

    # Tokenize each paragraph
    tokenized_paragraphs = [text.split() for text in prepared_corpus]

    # Generate n-grams
    ngrams_list = [ngrams(tokens, n) for tokens in tokenized_paragraphs]
    flattened_ngrams = [ng for ngrams in ngrams_list for ng in ngrams]

    # Count the frequency of n-grams
    ngrams_freq = Counter(flattened_ngrams)

    # Get the top n most frequent n-grams
    top_ngrams = ngrams_freq.most_common(top_n)

    return top_ngrams

# Example usage
unigrams = extract_ngrams(prepared_corpus, 1, 50)  # Top 50 most frequent unigrams
bigrams = extract_ngrams(prepared_corpus, 2, 50)  # Top 50 most frequent bigrams
trigrams = extract_ngrams(prepared_corpus, 3, 50)  # Top 50 most frequent trigrams

print("Top 50 Unigrams:", unigrams)
print("Top 50 Bigrams:", bigrams)
print("Top 50 Trigrams:", trigrams)