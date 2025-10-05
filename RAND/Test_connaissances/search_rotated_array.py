class solution:
    def search_rotated_array(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == target:
                return mid
            
            if arr[left] <= arr[mid]: # left side is sorted
                if arr[left] <= target < arr[mid]:
                    right = mid -1
                else : 
                    left = mid +1
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid +1
                else:
                    right = right -1
            return -1


