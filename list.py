num=[1,2,3,"Hari","Shyam","Gita"]
print(num)
a=(20,70,3,50,40,80,300,35,10,25,5)
print(a[0],)
print(sum(a))
print(sorted(a))


def sort_list(lst):
    lst.sort()
    return lst

numbers = [5, 2, 9, 1, 7]
print(sort_list(numbers))
 
def sort_list(lst):
    return sorted(lst)

numbers = [5, 2, 9, 1, 7]
print(sort_list(numbers))

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = [5, 2, 9, 1, 7]
print(bubble_sort(numbers))

 

