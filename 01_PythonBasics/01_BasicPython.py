
# # Python Programming Introduction
# ## Created for course 4460/6460 - Biological Image Analysis
# 
# @author: Pingkun Yan

# # Strings
# 
# Introduction to Python strings

#


print("Strings")

'''Empty String '''
myString = ""

'''Initialize String '''
myString = "Hello Python"  


#



''' Return a copy of the string
    with only its first character
    capitalized. '''
print(myString.capitalize())  

'''Return the lowest index in
  where substring sub is found,'''       
idx = myString.find("Python")   
print("idx: ", idx)                                  #6

'''Print sub-string '''
print(myString[idx:])                                #Python

'''Replace a sub-string '''
myStringNew = myString.replace("Python", "World")
print(myStringNew)                                   #"Hello World"
'''Concatenate strings '''
print(myString + ',' + myStringNew)


# # Introduction to tuples
# - tuple
# - list
# - dict

#


print("Tuples")

'''Initialize a tuple '''
myTuple = ("first", "second")   
print(myTuple)                   # ('first', 'second')

'''parentheses are optional '''
myTuple = "first", "second"     
print(myTuple)                   # ('first', 'second'

'''Unpack elements '''
a,b = myTuple
print("a: ", a, " b: ", b)       #a:  first  b:  second

myTuple.count("first")          #1

'''length'''
len(myTuple)                    #2

'''Get the first element '''
print(myTuple[0])                #"first"


#


'''Define a list  '''
print("LISTS:")

'''Empty list '''
xs = []
print(len(xs))   # 0

'''Creates list '''
xs = [3, 1, 2]

'''Finds and counts values '''
xs.count(1)      #1
xs.count(0)      #0

'''Add element trhee at the end of the list '''
xs.append(3)
print(xs)         #[3, 1, 2, 3]
xs.count(3)       #2
xs.remove(3)
print(xs)         #[1, 2, 3]

print(xs, xs[2])  # Prints "[1, 2, 3] 3"
print(xs[-1])     # Negative indices count from the end of the list; prints "3"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[1, 2, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints 
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [1, 2, 'foo']"


#


print("Slicing Examplies: ")

nums = list(range(5))  # range is a built-in function that creates a list of integers
print(nums)            # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])       # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])        # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])        # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])         # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print(nums[:-1])       # Slice indices can be negative; prints ["0, 1, 2, 3]"
nums[2:4] = [8,9]      # Assign a new sublist to a slice
print(nums)            # Prints "[0, 1, 8, 8, 4]"


#


'''Dictionaries '''

'''Empty Dictionary '''
myDictionary = {}  

'''Initialize Dictionary'''
myDictionary = {"One":1, "Two":2, "Three":3  }  
 
'''Get the keys '''
print(myDictionary.keys())                   #['Three', 'Two', 'One']

'''Get full content'''
print(myDictionary.items())                  #[('Three', 3), ('Two', 2), ('One', 1)]

'''Check if tuple is in dictionary'''
print(('Three', 3) in myDictionary.items())  #True

"""Get Element with key One """
print(myDictionary["One"])                   #1

"""Get Element with key One """
print(myDictionary["One"]  + myDictionary["Two"])  #3


#


"""Add a tuple """
myDictionary["Four"] = (4,"Second Element")
print(myDictionary["Four"])  # (4,"Second Element")

'''Delete the element 1 '''
del(myDictionary["One"]) 

print("One" in myDictionary) # False

'''Print and sort the dictionary ''' 
print(myDictionary)          #{'Four': (4, 'Second Element'), 'Three': 3, 'Two': 2}

print(sorted(myDictionary))  # ['Four', 'Three', 'Two']

'''Get the length '''
print(len(myDictionary))  #3


#


'''For loops use iterators!'''

'''Iterate over keys of the dictionary'''
for key in myDictionary.keys():
    print("Key is: ", key)
    print("myDictionary[key]: ", myDictionary[key])


'''
Output:

Key is:  Four
myDictionary[key]:  (4, 'Second Element')
Key is:  Three
myDictionary[key]:  3
Key is:  Two
myDictionary[key]:  2
'''    

