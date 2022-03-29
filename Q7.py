min = 0
max = 0
sum = 0
ave = 0
for i in range(21):
    x = float(input("Please Enter number: "))
    if x < min :
        min = x
    if x > max :
        max = x
    sum += x
ave = sum / 20
print("Average of you'r entered numbers = " , ave)
print("Sum of you'r entered numbers = " , sum)
print("Max of you'r entered numbers = " , max)
print("Min of you'r entered numbers = " , min)
