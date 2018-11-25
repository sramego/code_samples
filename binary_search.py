# Binary Search complexity: O(Log n) with sorted array

def find(arr, start, end, item):
    if end > 0:
        mid = start + (end-1) / 2
        if arr[mid] == x:
	    return mid
        elif arr[mid] > x:
	    return find(arr,start,mid-1,x)
	else:
	    return find(arr,mid+1,end,x)
    elif end < 0:
	return -1
    else:
	if arr[end] == x:
	    return end

arr = [2, 3, 4, 10, 40]
x = 10
  
# Function call 
result = find(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index %d" % result 
else: 
    print "Element is not present in array"

