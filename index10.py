# Fill out the function get_last_element(lst) which takes in a list lst as a 
# parameter and prints the last element in the list. The list is guaranteed 
# to be non-empty, but there are no guarantees on its length.


def get_last_element(lst):
    if lst:
        print("Last element:", lst[-1])
    else:
        print("The list is empty.")

# Example usage
my_list = [10, 20, 30, 40]
get_last_element(my_list)
