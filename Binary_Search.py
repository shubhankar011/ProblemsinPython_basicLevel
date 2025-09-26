# #Binary Search Algorithm
l = 90000
a = int(input("Enter the number between 0 to 90000: "))
i = 0
steps = 0
while i < 90000:

    mid = i  + (l - i) // 2
    if i == a:
        print(f"Hello, world!, steps taken are {steps}")
        break

    elif mid > a:
        l = mid - 1
        print(f"It is on {i}")
        steps = steps + 1
    elif mid < a:
        i = mid + 1 
        print(f"It is on {i}")
        
        steps = steps + 1
    else:
        print(f"It is on {i}")
        
        steps = steps + 1
# The pyhtonic approach

# def binary_search(target, max_range):
#     low = 0
#     high = max_range
#     steps = 0
    
#     while low <= high:
#         steps += 1
#         mid = low + (high - low) // 2
        
#         if mid == target:
#             return mid, steps
#         elif mid > target:
#             high = mid - 1
#             print(f"Searching in range {low} to {high}")
#         else:
#             low = mid + 1
#             print(f"Searching in range {low} to {high}")
            
#     return -1, steps

# # Maximum range
# max_range = 90000

# # Get input
# try:
#     target = int(input(f"Enter the number between 0 to {max_range}: "))
    
#     if 0 <= target <= max_range:
#         result, steps = binary_search(target, max_range)
        
#         if result != -1:
#             print(f"\nNumber {target} found!")
#             print(f"Total steps taken: {steps}")
#         else:
#             print(f"\nNumber {target} not found in range")
#     else:
#         print(f"Please enter a number between 0 and {max_range}")
        
# except ValueError:
#     print("Please enter a valid integer")