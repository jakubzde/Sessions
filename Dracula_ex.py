word_freq = {}
punctuation = ".,!?\n"
with open ("Dracula.txt", "r", encoding="utf-8") as file:
    for line in file:
        #We have all the lines in the file
        for p in punctuation:
            line = line.replace(p, "")
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if len(word) < 5:
                continue
            #if word in word_frequency:
            #    word_freq[word] += 1
            #else:
            #    word_freq[word] = 1
            word_freq[word] = word_freq.get(word, 0) + 1 #This is the same as the four above lines

top_freq = list(word_freq.values())
top_freq.sort(reverse=True)
top_freq = top_freq[:10]

#Print top words by frequency
for top_word in top_freq:
    for key in word_freq:
        if word_freq[key] == top_word:
            print(f"{key} : {top_word}")
            del word_freq[key]
            break