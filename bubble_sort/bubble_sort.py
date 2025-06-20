def bubble_sort(arr,n):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

my_num=[5,13,6,2,12,9,15,8]
print("LIst: ",my_num)

bubble_sort(my_num,len(my_num))
print("Sorted list: ",my_num)







