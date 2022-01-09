import nltk
import sys
import os
import math
import string

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for text in os.listdir(directory):
        path = os.path.join(directory, text)
        f = open(path, 'rt', encoding='UTF8')
        files[text] = f.read()
        f.close()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = nltk.word_tokenize(document.lower())
    words_return = []
    for word in words:
        if word not in nltk.corpus.stopwords.words("english"):
            copy = ""
            for c in word:
                if c not in string.punctuation:
                    copy += c
            if copy:
                words_return.append(copy)
    return words_return


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    words = set()
    total = len(documents)
    for document in documents:
        for word in documents[document]:
            words.add(word)
    for word in words:
        counter = sum(word in documents[document] for document in documents)
        idfs[word] = math.log(total/counter)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tfidfs = dict()
    ranked_list = []
    for document in files:
        tfidfs[document] = 0
        for word in query:
            tf = files[document].count(word)
            tfidf = tf*idfs[word]
            tfidfs[document] += tfidf
    ranked = sorted(tfidfs.items(), key=(lambda x: x[1]), reverse=True)
    for item in ranked:
        ranked_list.append(item[0])
    return ranked_list[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sent_idf = dict()
    answer = []
    for sentence in sentences:
        sum_idf = 0
        sum_density = 0
        for word in query:
            if word in sentences[sentence]:
                sum_idf += idfs[word]
            sum_density += sentences[sentence].count(word)
        sent_idf[sentence] = (sum_idf, sum_density/len(sentences[sentence]))
    ranked = sorted(sent_idf.items(), key=(lambda x: (x[1][0], x[1][1])), reverse=True)
    for sentence in ranked:
        answer.append(sentence[0])
    return answer[:n]


if __name__ == "__main__":
    main()
