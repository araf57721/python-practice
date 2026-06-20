m = int(input("Enter some number:"))
print(m)
count = 0
for i in range(1,m+1):
    if(i%2 == 0):
        count = count + 1
        print("This is a even number" ,i)
    else:
        print("This is a odd number" , i)

print(count)