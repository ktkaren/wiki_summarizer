__doc__ = """This file contains the function for summarizing the text."""

from nltk.stem import WordNetLemmatizer
from services.keyword_extraction import extract_keywords
from services.rank_sentence import rank_sentences
from services.order_sentence import order_sentences


def summarize(text, number_of_sentence):
    """
    Summarize the text to given number_of_sentence.

    :param text: string
    :param number_of_sentence: integer
    :return: string (the summary)
    """

    # extract keywords from text and create keyword-score mapping
    LEMMATIZER = WordNetLemmatizer()
    keywords_mapping = extract_keywords(text, LEMMATIZER)

    # rank sentences based on the occurrence of keywords
    ranked_sents = rank_sentences(text, LEMMATIZER, keywords_mapping)

    # select sentences based on the numebr of sentences wanted
    cutoff = number_of_sentence
    if number_of_sentence > len(ranked_sents):
        cutoff = len(ranked_sents) - 1
    selected_sents = ranked_sents[:cutoff]

    # order the selected sentence based on their order of occurrence in the text.
    ordered_sents = order_sentences(text, selected_sents)

    summary = ' '.join(ordered_sents)

    return summary
