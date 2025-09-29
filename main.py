from stats import get_num_words, times_each_char, sorted_list
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()  
    
def main():
   if len(sys.argv) != 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   book_location = sys.argv[1] # specify book location here
   book_text = get_book_text(book_location)  # get text
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_location}...")
   print("----------- Word Count ----------")
   print(f"Found {get_num_words(book_text)} total words")  # pass text into function
   print("--------- Character Count -------")
   chars = times_each_char(book_text)
   sorted_chars = sorted_list(chars)
   for entry in sorted_chars:
       ch = entry["char"]
       if ch.isalpha():  # only print letters
           print(f"{ch}: {entry['num']}")
   
main()