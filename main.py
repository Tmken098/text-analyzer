from utils import clean_text, word_count, most_common_word

text = input('Enter text: ')

text = clean_text(text)
print('Word count:', word_count(text))


result = most_common_word(text)
print('Most common word:', result)
