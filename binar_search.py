import time
users = []

for number in range(1000000):
    new_user = {int(number),'user_' + str(number)}
    users.append(new_user)




inp = input()
key = int(inp)
array = range(len(users)+1)

def binar_search(arr):
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

print(users[binar_search(array)])
