# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Update set1 by adding items from set2, except common items
set1.update(set2 - set1)

# Display the updated set1
print("Updated set1:", set1)
