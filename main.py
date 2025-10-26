from stats import get_word_count, char_counts, sort_dict
import sys


def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print(get_word_count(sys.argv[1]))
	sorted_list = sort_dict(sys.argv[1])
	for diction in sorted_list:
		if diction["char"].isalpha():
			print(diction["char"] + ":", diction["num"])

main()
