def clean_text(text):
    return text.lower()

def word_count(text):
    words = text.split()
    return len(words)

def most_common_word(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    return max(counts, key=counts.get)