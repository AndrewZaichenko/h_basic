
# counts a quantity of unique words in text
def text_to_unique_words(text: str) -> dict:
    text_formated = text.replace(".", " ").replace(",", " ").replace("-", "").replace('"', '').replace("?", " ").lower()
    text_splitted = text_formated.split()
    words_count = {}
    for word in set(text_splitted):
        words_count[word] = text_splitted.count(word)
    return words_count
