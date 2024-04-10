anagrams = {}
with open("words.txt", 'r') as file:
    for word in file:
        word = word.strip()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
with open("anagrams.txt", 'w') as file:
    for group in anagrams.values():
        file.write(' '.join(group) + '\n')
