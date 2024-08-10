''' You have two lists:

list1 with elements [1, 2, 3]
list2 with elements [4, 5, 6].
Create a program using list method to add the elements of list2 to list1.'''

# Given lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Add elements of list2 to list1
for element in list2:
    list1.append(element)

print("Updated list1:", list1)
