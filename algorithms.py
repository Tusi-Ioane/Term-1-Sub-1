#day 1 exercise
#insertion algorithm

#function for insertion
def insertionSort(arr):

# traverse through 1 to len(arr)
for i in range (1, len(arr)):
        key = arr[i]

        #moving elements of arr that are greater than ley to move 
        #one position ahead of their position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j + 1] = key

# # #code to test above
# arr = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
# insertionSort(arr)
# for i in range(len(arr)):
#                 print ("% d" % arr[i])


#INSERTION SORT
# creating a function for insertion  
def insertion_sort(list1):  
  
        # Outer loop to traverse through 1 to len(list1)  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            # Move elements of list1[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        return list1  
            # Driver code to test above  
  
list1 = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]  
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1))  

# #SELECTION SORT
# def selectionSort(array, size):
    
#     for ind in range(size):
#         min_index = ind
 
#         for j in range(ind + 1, size):
#             if array[j] < array[min_index]:
#                 min_index = j
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
 
# arr = pd.read_csv('C:\Users\tusii\OneDrive\Desktop\Pabds\BirthWeight.csv')
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)

# #MERGE SORT
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#     L = [0] * (n1)
#     R = [0] * (n2)
#     for i in range(0, n1):
#         L[i] = arr[l + i]
 
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]   
#         i = 0    
#         j = 0   
#         k = l 
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
# def mergeSort(arr, l, r):
#     if l < r:
#         m = l+(r-l)//2
 

#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m, r)
 
 
# # Driver code to test above
# arr = pd.read_csv('C:\Users\tusii\OneDrive\Desktop\Pabds\BirthWeight.csv')
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")
 
# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")
