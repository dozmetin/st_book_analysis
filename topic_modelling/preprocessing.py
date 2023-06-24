from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

# Initialize tokenizer
tokenizer = RegexpTokenizer(r'\w+')


def preprocess_text_list(string_list):
    """
    Takes a list of strings and preprocesses them.
    :param text_list: List of strings
    :return: Preprocessed strings as a list
    """
    preprocessed_string_list = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english')) # Common stop words in English

    # Our additions of stopwords
    stop_words.update(['being', 'page', 'clause', 'may', 'one', 'ieee', 'example', 'method', 'value',
                       'false', 'true', 'test', "testing", 'testing', 'month', 'figure', 'also', 'taylor', 'francis',
                       'team', 'string', 'int', 'expected', 'return', 'day', 'year', 'chapter', 'void', 'private',
                       'public', 'best', 'def', 'new', 'customer', 'need', 'work', 'two', 'isleap', 'else', 'use',
                       'triangle', 'make', 'sure', 'actual', 'thing', 'might', 'can', 'not', 'var', 'job', 'sale',
                       'time', 'null', 'review', 'meeting', 'www', 'ebooks', 'none', 'student', 'tester', 'using',
                       'many', 'get', 'good', 'way', 'rather', 'able', 'must', 'play', 'name', 'would', 'could', 'like',
                       'used', 'see', 'try', 'think', 'however', 'well', 'take', 'find', 'know', 'people', 'thus',
                       'first', 'run', 'different', 'help', 'pre', 'software', 'learned', 'number', 'per', 'often',
                       'every', 'much', 'facing', 'want', 'definition', 'made', 'look', 'another', 'given', 'book',
                       'hence', 'char', 'three', 'range', 'iff', 'forexample', 'rule', 'code', 'case', 'change',
                       'program', 'answers', 'quiz', 'questions', 'even', 'though', 'appendix', 'answer', 'provided',
                       'question', 'wikipedia', 'date', 'org', 'age', 'invalid', 'txt', 'case', 'iis', 'something', 'win',
                       'whether', 'net', 'month', 'port', 'commission', 'yes', 'grammar', 'bank'])

    for string in string_list:

        # Lemmatize the strings
        tokens = [lemmatizer.lemmatize(token) for token in tokenizer.tokenize(string)]

        # Convert tokens to lowercase
        tokens = [token.lower() for token in tokens]

        # Remove any punctuation marks and numbers
        tokens = [token for token in tokens if token.isalpha()]

        # Remove all the stop words
        tokens = [token for token in tokens if token not in stop_words]

        # Filter out tokens that has a length of 2 or less
        tokens = [token for token in tokens if len(token) > 2]

        # Combine tokens back into a string
        preprocessed_text = ' '.join(tokens)

        # Add string to preprocessed list
        preprocessed_string_list.append(preprocessed_text)

    return preprocessed_string_list

