# Sample set
my_set = {1, 2, 3, 4, 5}

# Item to be removed
item_to_remove = 3

# Check if the item is present in the set
if item_to_remove in my_set:
    # Remove the item
    my_set.remove(item_to_remove)
    print(f"{item_to_remove} removed from the set.")
else:
    print(f"{item_to_remove} is not present in the set.")

# Display the updated set
print("Updated set:", my_set)
