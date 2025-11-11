def get_word_count(text):
    return len(text.split())

def count_characters(text):
    text_lower = text.lower()
    characters = {}
    for char in text_lower:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters