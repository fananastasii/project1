def big_fibonacci(n):
	num1 = 1
	num2 = 1
	num3 = num1 + num2
	while(len(str(num3))<n):
		num1 = num2
		num2 = num3
		num3 = num1 + num2
	return(num3)
	
