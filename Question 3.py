def facto(num):
    if num==1:
        return 1
    
    return facto(num-1)*num

n=int(input("enter a number: "))
print(f"the factorial of {n} is {facto(n)}")