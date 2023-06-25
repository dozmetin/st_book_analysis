# Replication Package for Topic Analysis on Popular Software Testing Books (CSE3000 TU Delft)
This package includes our popular software testing books data, our manual inspection data and LDA implementation for topic modelling. 


### Topic Modelling
To run LDA, create a new virtual environment in Python 3.9 or newer and install the requirements from requirements.txt.
- `ngrams.py` can be used to output the top ngrams (uni, bi, tri) of the corpus. 
- `preprocesing.py` is used to apply preprocessing before the application of LDA.
- `lda_gensim.py` includes our implementation of LDA. The book chapters to be analysed should be included in the 'data' 
folder. By default, the book chapters need to be in PDF format.


### Book Manual Inspections
The metadata regarding the books, our topic coverage matrix, framework and content delivery results can be found in
`book_metadata_content.xlsx`. The labels we assigned to the chapters of each book as a result of our manual inspection are available in`per-book_chapter_labeling.xlsx`.



