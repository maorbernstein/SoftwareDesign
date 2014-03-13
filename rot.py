def rotate_word(string,num):
	 rotstring = ""
	 for char in string:
	 	charnum = ord(char)
	 	rotcharnum = charnum + num
	 	if rotcharnum>122:
	 		rotchar = chr(rotcharnum - 122 + 64)
	 	else:
	 		rotchar = chr(rotcharnum)
	 	rotstring = rotstring + rotchar
	 return rotstring