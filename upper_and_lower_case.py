def count_upper_lower_case(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
sample_string = 'The quick Brow Fox'
upper, lower = count_upper_lower_case(sample_string)

print(f"Number of upper case letters: {upper}")
print(f"Number of lower case letters: {lower}")
