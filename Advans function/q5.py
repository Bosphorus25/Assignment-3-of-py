# Write a function that takes a list and removes all duplicate elements
def o_list():
    ele = int(input("enter total num of element: "))
    l = []
    for i in range(ele):
        x = input("enter element: ")
        l.append(x)
    non_dupli = set(l)
    print(non_dupli)
o_list()
o_list()