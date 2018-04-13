def binary_search(my_list, item):
	lo = 0
	hi = len(my_list) - 1

	while(lo <= hi):
		mid = (lo + hi) / 2
		guess = my_list[mid]

		if(guess == item):
			return mid
		elif(guess < item):
			lo = mid +1
		else:
			hi = mid -1


my_list = [1, 4, 9, 14, 25, 98]
x = input("Enter the number to be searched")
print binary_search(my_list, x)
