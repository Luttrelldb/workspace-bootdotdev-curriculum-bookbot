from stats import get_word_count, count_characters, sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()