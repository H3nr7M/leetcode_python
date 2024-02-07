from collections import defaultdict

def get_ngrams(text, n=3):
    sentences = text.split(".") # Split text into sentences
    ngrams = defaultdict(int)

    for w in sentences: # Iterate over sentences
        w = w.strip() # Remove leading and trailing whitespaces
        words = w.split() # Split sentence into words
        for i in range(len(words)-n+1): # Iterate with a window of size n
            ngram = " ".join(words[i:i+n]) # Join words into ngram
            ngrams[ngram] += 1 # Increment count of ngram

    return max(ngrams, key=ngrams.get) # Return ngram with highest count

# Example usage with trigrams
text = "i love the fotbol soccer. i enjoy the fotbol fast. i love the swimmiing in the pool"
trigram = get_ngrams(text, n=3)
print(trigram)  # Output: "i love the"
