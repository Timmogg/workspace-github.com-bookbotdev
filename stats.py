def get_word_count(text):
        words = text.split()
        return len(words)
def count_characters(text):
	text = text.lower()
	counts = {}
	for ch in text:
		counts[ch] = counts.get(ch, 0) + 1
	return counts
def sorted_list(counts):
	def sort_on(item):
		return item["num"]
	sort_list = []
	for ch, cnt in counts.items():
		sort_list.append({"char": ch, "num": cnt})
	sort_list.sort(reverse=True, key=sort_on)
	return sort_list
	
