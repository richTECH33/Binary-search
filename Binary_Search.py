def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    
    return -1     
# Take array input from the user
arr = list(map(int, input("Enter space seperated integers: ").split()))   

#Ask for value to search
target = int (input("Enter the value to search: "))

#call binary search function
result = binary_search(arr, target)

#check for validation
if result != -1:
    print(f"Target value {target} found at index {result}. ")
else:
    print(f"Targer value {target} not found in the array.")