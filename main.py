from stats import get_word_count, count_characters, sort_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    book_text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()