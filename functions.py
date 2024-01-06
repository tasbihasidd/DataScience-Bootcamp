def find_max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

maximum_value = find_max_of_three(15, 27, 10)
print(f"The maximum number is: {maximum_value}")
