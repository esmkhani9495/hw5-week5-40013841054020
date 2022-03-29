str = input("Please Enter your sentence: ")
x = int(input("Please Enter x: "))
for i in str:
    temp = ord(i) + x
    print(chr(temp) , end = "")
