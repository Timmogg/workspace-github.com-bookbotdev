import sys
from stats import get_word_count
from stats import count_characters
from stats import sorted_list

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]

	text = get_book_text(book_path)
	book_word_count = get_word_count(text)
	character_count = count_characters(text)
	list_sorted = sorted_list(character_count)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print("Found", book_word_count, "total words")
	print("--------- Character Count -------")
	for item in list_sorted:
		ch = item["char"]; n = item["num"]
		if not ch.isalpha():
			continue
		print(f"{ch}: {n}")
	print("============= END ===============")
main()


