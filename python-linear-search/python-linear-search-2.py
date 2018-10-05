def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1
arr = [int(x) for x in input().split()]
x = int(input("Enter number to search: "))
i = search(arr,x)
if i>-1:
    print("Found")
else:
    print("Not Found")
