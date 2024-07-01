import re

def load_cuss_words():
    # Predefined list of cuss words
    # This list can be extended or modified
    cuss_words = ["badword1", "badword2", "badword3"]
    return set(cuss_words)

def censor_text(text, cuss_words):
    # Create a regex pattern that matches any cuss word
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in cuss_words) + r')\b', re.IGNORECASE)
    # Replace each cuss word with asterisks
    censored_text = pattern.sub(lambda match: '*' * len(match.group()), text)
    return censored_text

# Example usage
cuss_words = load_cuss_words()
text = "This is a text with badword1 and some other badword2."
censored_text = censor_text(text, cuss_words)
print(censored_text)

