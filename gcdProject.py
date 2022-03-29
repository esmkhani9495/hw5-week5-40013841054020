a = int(input("Please Enter a: "))
b = int(input("Please Enter b: "))
if(a>b):
	for j in range(b , 0 , -1):
		if(a%j==0 and b%j==0):
			print(j)
			break
elif(a<b):
	for j in range(a , 0 , -1):
		if(a%j==0 and b%j==0):
			print(j)
			break

