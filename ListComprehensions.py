x = int(input())
y = int(input())
z = int(input())
n = int(input())
my_list = []
for el in range(x + 1):
    for el1 in range(y + 1):
        for el2 in range(z + 1):
            if ((el + el1 + el2) != n):
                list_elements = ([el, el1, el2])
                my_list.append(list_elements)

print(my_list)
