def selection_sort(arr):
   n=len(arr)
   for i in range(n):
       min_index=i
       for j in range(i+1,n):
           if arr[j]<arr[min_index]:
               min_index=j
               arr[i],arr[min_index]=arr[min_index],arr[i]


my_num=[2,4,1,5,3]
print("List: ",my_num)

selection_sort(my_num)
print("Sorted list: ",my_num)


