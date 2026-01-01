import sys

from stats import word_count, character_count, sorted_list



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        
    book_text = get_book_text(sys.argv[1])
    count = word_count(book_text)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print ("----------- Word Count -----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    
    ch_sorted = sorted_list(character_count(book_text))
    for char_dict in ch_sorted:
        print (f'{char_dict["char"]}: {char_dict["count"]}')
    
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
