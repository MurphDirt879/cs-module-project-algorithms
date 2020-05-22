'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    a = 0
    b = k
    
    finalArray = [0] * (len(nums) - (k - 1))

    for i in range(0, len(finalArray)):
        max = None
        for num in nums[a:b]:
            if max is None:
                max = nums[a]
            elif num > max:
                max = num
        finalArray[i] = max
        
        a += 1
        b += 1

    return finalArray




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
