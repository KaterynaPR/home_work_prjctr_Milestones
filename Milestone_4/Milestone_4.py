from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    for i in range(len(li)): #Iterate through all possible pairs of items
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return (i, j)

print(find_sum(5, [1, 2, 3, 4, 5]))  #Possible outputs: (0, 3) or (1, 2) 
#time complexity - O(n^2), where n is the number of elements in the list li and space complexity - O(1), since we do not use additional memory that depends on the size of the input data

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}  #Dictionary for storing numbers and their indices
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

print(find_sum_fast(5, [1, 2, 3, 4, 5]))  #Possible outputs: (0, 3) or (1, 2) 
#time complexity - O(n), where n is the number of elements in the list li, becouse we go through the list only once and space complexity - O(n), since in the worst case we can store all the items in the dictionary.
