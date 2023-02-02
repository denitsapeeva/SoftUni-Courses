words_file = open('words.txt', 'r')
words = words_file.readlines()

text_file = open('text.txt', 'r')
text = text_file.readlines()
new_word = []

word_count = {}
for word in words:
    word_count = {x.lower(): 0 for x in word.split()}
for tx in text:
    my_text = [x.lower() for x in tx.split()]
    for word in my_text:
        word = word.lower()
        if word in word_count.keys():
            word_count[word] = word_count[word] + 1

print(word_count)
