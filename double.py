f = open('words.txt','r')
text = f.read()
f.close()

def double_finder(text):
	words = text.split()
	print len(words)
	doubles = []
	for word in words:
		prevchar = ""
		for char in word:
			if char==prevchar:
				doubles.append(word)
				break
			prevchar = char
	print len(doubles)
	return doubles

print double_finder(text)[25000:25004]