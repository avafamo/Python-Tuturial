

# print(list(range(1, 10)))  
# print(list(range(10)))  
# print(list(range(0, 15, 2)))  
# print(list(range(10, 0, -2)))  

# for num in range(1, 10):
#     print("*" * num)


for num in range(1, 10):
    if num % 2 == 1:
        for star in range(1, 6): 
            print("*" * star)
    else:
        for star in range(5, 0, -1):  
            print("*" * star)
