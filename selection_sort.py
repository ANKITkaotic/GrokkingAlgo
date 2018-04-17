arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
	min_indx = i
	for j in range(i+1, len(arr)):
		if(arr[min_indx] > arr[j]):
			min_indx = j
	arr[i], arr[min_indx] = arr[min_indx], arr[i]
	
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i]),

