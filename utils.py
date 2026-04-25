import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = text.split(' ')
    return text


def word_count(text):
    words = text
    return len(words)

def most_common_word(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    max_word = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return max_word[0][0]