"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string
from collections import OrderedDict

def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    lines = []
    final_lines = []

    with open(file_name, encoding="utf8") as fp:
        for line in fp:
            processed_line = line.strip()
            processed_line = processed_line.lower()
            processed_line = processed_line.split()
            lines.append(processed_line)

    for sublist in lines:
        for item in sublist:
            temp_string = ""
            for letter in range(len(item)+1):
                temp_string = temp_string + item[letter-1:letter].strip(string.punctuation)
            final_lines.append(temp_string)

    return final_lines


def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequentlyoccurring

    Examples
    --------
    >>> print(get_top_n_words("pg32325.txt", 100))
    ['and', 'the', 'i', 'to', 'a', 'it', 'was', 'of', 'he', 'in', 'you', 'that', 'but', 'so', 'on', 'for', 'all', 'we', 'up', 'out', 'me', 'him', 'they', 'says', 'got', 'then', 'no', 'with', 'there', 'his', 'as', 'them', 'she', 'said', 'see', 'had', 'down', 'well', 'at', 'when', 'about', 'by', 'my', 'if', 'what', 'would', 'do', 'or', 'come', 'be', 'one', 'is', 'her', 'didnt', 'jim', 'dont', 'get', 'time', 'could', 'this', 'right', 'aint', 'went', 'warnt', 'off', 'over', 'go', 'good', 'way', 'like', 'just', 'old', 'around', 'know', 'now', 'de', 'along', 'en', 'its', 'done', 'tom', 'because', 'couldnt', 'back', 'ever', 'your', 'some', 'man', 'why', 'little', 'any', 'never', 'say', 'more', 'how', 'two', 'have', 'again', 'away', 'too']
    """
    words = get_word_list(word_list)
    hist = dict()
    for word in words:
        hist[word] = hist.get(word, 0) + 1
    sorted_hist = OrderedDict(sorted(hist.items(), key=lambda x: x[1], reverse=True)) # I was curious about which words showed up most in the book, so I used this answer to help me sort the dictionary: https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/
    sorted_hist_list = list(sorted_hist.keys())
    return sorted_hist_list[0:n]


if __name__ == "__main__":
    import doctest
    #doctest.testmod() # Run to test this script. If everything is working as expected, you'll see no output.
    print(get_top_n_words("pg32325.txt", 100))
