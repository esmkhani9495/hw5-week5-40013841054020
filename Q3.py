x = int(input("Please Enter x: "))
y = int(input("Please Enter y: "))
while(y>0):
	temp = x%y
	x = y
	y = temp
