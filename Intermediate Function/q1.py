# Create a function that takes a list of numbers and returns the largest number
def big_num():
    ele = int(input("enter total num of element: "))
    l = []
    for i in range(ele):
        x = int(input("enter element: "))
        l.append(x)
    l.sort()
    print("largest num",l[-1])    
big_num() 
# max function cn be replaced by sort but it gives us min max both by using index   