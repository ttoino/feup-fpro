from math import log


def tfidf(documents: list):
    documents = list(map(lambda x: x.lower().split(), documents))
    return {word: [round(document.count(word) * log(len(documents)/len([doc for doc in documents if word in doc])), 3) for document in documents] for word in {w for doc in documents for w in doc}}

