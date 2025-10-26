def get_book_words(filepath):
	with open(filepath) as f:
		return f.read()

def get_word_count(filepath):
	words = get_book_words(filepath)
	return f"Found {len(words.split())} total words"

def char_counts(filepath) -> dict[str, int]:
	counts = {}
	s = get_book_words(filepath)
	for ch in s.lower():
        	counts[ch] = counts.get(ch, 0) + 1
	return counts

def sort_dict(filepath):
	diction = char_counts(filepath)
	dict_list = []
	for key, value in diction.items():
		dict_list.append({"char": key, "num": value})
	dict_list.sort(reverse=True, key=lambda d: d["num"])
	return dict_list
