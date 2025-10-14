"""
Word Occurrences
Estimate: 10 mins
Actual: 16 mins
"""
text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] = word_to_count[word] + 1
longest_word = max(len(word) for word in list(word_to_count.keys()))
for word, count in sorted(word_to_count.items()):
    print(f"{word:{longest_word}} : {count}")
