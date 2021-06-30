# A Python program to print all
# permutations using library function


# Get all permutations of [1, 2, 3]
i=int(input())
j=int(input())
k=int(input())
n=int(input())
my_list=[]
for el in range(i+1):
    for el1 in range(j+1):
        for el2 in range(k+1):
            if((el+el1+el2)!=n):
                list_elements=([el,el1,el2])
                my_list.append(list_elements)


print(my_list)
