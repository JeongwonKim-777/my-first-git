# i > 1 ~ 50
# i is times of 3, "fast"
# i is times of 5, "campus"
# rest, i


for i in range(1, 51):

	if i % 3 == 0:
		print("fast")
	elif i % 5 == 0:
		print("campus")
	else:
		print(i)

