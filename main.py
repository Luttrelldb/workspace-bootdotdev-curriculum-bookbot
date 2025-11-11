from stats import get_word_count, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    char_counts = count_characters(book_text)
    print(char_counts)

if __name__ == "__main__":
    main()