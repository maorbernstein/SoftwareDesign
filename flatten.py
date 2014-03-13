def flatten(s):
	out = []
	for element in s:
		if isinstance(element,list):
			out.extend(element)
		else:
			out.append(element)
	return out

print flatten([1, [2, [4,5]] , 3])