def build_vocabulary(segmented_document):
    vocabulary = []
    for word in segmented_document.split(' '):
        if word not in vocabulary:
            vocabulary.append(word)

    return vocabulary


def is_a_synonym(word):

    return word[0].isupper() and word.__len__() < 4


def split_sentences(document):

    document = document.split(' ')
    start_of_sentence = "<s>"
    end_of_sentance = "</s>"

    segmented_document = [start_of_sentence]
    for word in document:
        if '?' in word or '!' in word or ':' in word:
            segmented_document.append(word[:-1] + end_of_sentance)
        elif '.' in word:
            if not is_a_synonym(word):
                segmented_document.append(word[:-1] + end_of_sentance)
        else:
            segmented_document.append(word + ' ')
    return "".join(segmented_document)


