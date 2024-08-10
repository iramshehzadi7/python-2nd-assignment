'''Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the
triangle (the sum of all of the side lengths).'''

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

# Get input from the user
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

perimeter = calculate_perimeter(side_a, side_b, side_c)
print(f"The perimeter of the triangle is {perimeter:.2f} units.")
