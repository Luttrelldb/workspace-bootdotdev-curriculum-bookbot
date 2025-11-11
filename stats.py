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

def sort_characters(characters):
    list_of_dicts = []
    for char, count in characters.items():
        list_of_dicts.append({"char": char, "num": count})
    return sorted(list_of_dicts, key=lambda x: x['num'], reverse=True)
