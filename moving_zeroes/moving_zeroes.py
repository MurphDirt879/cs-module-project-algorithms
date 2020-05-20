'''
Input: a List of integers
Returns: a List of integers
'''



def moving_zeroes(arr):
    # Your code here
    zeros = 0 

    for n in arr:
        if n == 0:
            arr.remove(n)
            arr.append(n)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")