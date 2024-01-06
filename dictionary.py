# Given dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
combined_dict = {}

# Iterate through keys in d1 and d2
for key in set(d1.keys()) | set(d2.keys()):
    combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

# Display the combined dictionary
print("Combined Dictionary:", combined_dict)
