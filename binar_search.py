
def binar_search(arr,key):
   left = 0
   right = arr[len(arr)-1]
   while (left<=right):
       mid = (right - left)//2 + left
       if mid > key:
           right = mid - 1
       if mid < key:
           left = mid + 1
       if mid == key:
           break

   return mid


