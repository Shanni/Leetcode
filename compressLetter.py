def Compress(str_1):
	if len(str_1)<2:
		return str_1
	ret=str(str_1[0])
	prev=str_1[0]
	count=0
	for letter in str_1[1:]:	
		if letter!=prev:
			if count!=0:
				ret+=str(count+1)
				count=0
			ret+=letter
			prev=letter
		else:
			count+=1
	if count!=0:
		ret+=str(count+1)
	return ret
print Compress("zzzbbabcdddd")
print Compress("")
print Compress("bbaabbbaaaba")