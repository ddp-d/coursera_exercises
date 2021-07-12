# 1. Provided is a string saved to the variable name sentence. 
# Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. 
# Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

words_list = sentence.split()
word_counts = {}

for c in words_list:
    if c not in word_counts:
        word_counts[c] = 0
    word_counts[c] = word_counts[c] + 1
    
print(word_counts)


# 2. Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"

char_d = {}

for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] = char_d[c] + 1
print(char_d)
