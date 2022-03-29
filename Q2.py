x0 = float(0)
e = float(input("Tolerable Error: "))
step = 1
flag = 1
condition = True

while condition:
    if (3*x0**2 - 5) == 0.0:
        break
    x1 = x0 - ((x03 - 5*x0 - 9)/(3*x02 - 5))
    print("Iteration-%d, x1 = %0.6f and f(x1) = %0.6f" % (step, x1, (x1**3 - 5*x1 - 9)))
    x0 = x1
    step = step + 1
    
    if step > 10:
        flag = 0
        break
    
    condition = abs((x1**3 - 5*x1 - 9)) > e

if flag==1:
    print("\nRequired root is: %0.8f" % x1)
else:
    print("\nNot Convergent.")
