#Write a program which continuously asks the user to enter values which are added one by one into a list.
#  When the user presses enter without typing anything, print the list.
def main():
    my_list = []  # Initialize an empty list

    while True:
        user_input = input("Enter a value (or press Enter to finish): ")
        if user_input:
            my_list.append(user_input)  # Add the value to the list
        else:
            break  # Exit the loop when the user presses Enter without typing anything

    print("Your list:", my_list)

if __name__ == "__main__":
    main()


