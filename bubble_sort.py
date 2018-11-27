# Array bubble sort O(n^2) worst case and O(n) best case

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
	    if arr[i] > arr[j]:
		arr[i] = arr[i] + arr[j]
		arr[j] = arr[i] - arr[j]
		arr[i] = arr[i] - arr[j]

    return arr

if __name__ == '__main__':
    print bubble_sort([5, 1, 4, 2, 8])
