def countword(text):
    words = text.split()
    return len(words)

text = input('Type some word')

word_count = countword(text)

print(f'Word Count:, {word_count}')