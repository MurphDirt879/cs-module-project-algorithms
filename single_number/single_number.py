'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#iterate through the list
#check to see what number only occurs onec
#retun the sing int
def single_number(arr):
    # Your code here
    singles = []

    for i in arr: 
        if i in singles: 
            singles.remove(i)
        else:
            singles.append(i)
    if len(singles) == 1:
        return singles[0]
    


    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")