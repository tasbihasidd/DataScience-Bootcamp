# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}


common_elements = set1.intersection(set2)
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements.")
