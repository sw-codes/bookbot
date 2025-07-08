from stats import count_words, count_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    sorted_dictionary = sort_dictionary(count_characters(get_book_text(sys.argv[1])))
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}...\n"
        "----------- Word Count ----------\n"
        f"Found {count_words(get_book_text(sys.argv[1]))} total words\n"
        "--------- Character Count -------"
    )
    for item in sorted_dictionary:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()