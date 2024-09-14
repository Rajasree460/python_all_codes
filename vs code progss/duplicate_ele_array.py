#duplicate elements( Return true if any value appears at least twice in the array, and return false if every element is distinct)
def test_duplicate(array_num):
 nums_set = set(array_num) #set is a func
 return len(array_num) != len(nums_set) 
#main function
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4,4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))
