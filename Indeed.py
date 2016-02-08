def Qualitile(nums,q):
	num_index=-1
	index=[0]*(q-1)
	count=0
	ret=[0]*(q-1)
	for i in range(q-1):
		num_index+=nums[i][1]
		count+=nums[i][1]

	for i in range(q-1):
		index[i]=count*(i+1)/q
		j=-1
		i_sum=-1
		while index[i]>i_sum:
			i_sum+=nums[j][1]
			j+=1
		ret[i]=nums[j][0]
	print ret
	
Qualitile([(5,2),(6,2),(7,2)],3)