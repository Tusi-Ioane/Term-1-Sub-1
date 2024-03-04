#day 1 exercise
#insertion algorithm

#function for insertion
# def insertionSort(arr):

# #traverse through 1 to len(arr)
#     for i in range (1, len(arr)):
#         key = arr[i]

#         #moving elements of arr that are greater than ley to move 
#         #one position ahead of their position
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j + 1] = key

# #code to test above
#             arr = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
#             insertionSort(arr)
#             for i in range(len(arr)):
#                 print ("% d" % arr[i])


#bubble algorithm
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