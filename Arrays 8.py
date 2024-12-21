# Create a toy box (array) with some toys
toys = ["ball","truck","doll","robot","airplane"]

# Print the unsorted toy box
print("Unsorted toys:", toys)

# Loop through each toy (except the last one)
for i in range(len(toys) - 1):
  # Compare the current toy with the next one
  for j in range(i + 1, len(toys)):
    # Swap toys if the current one comes alphabetically after the next
    if toys[i] > toys[j]:
      temp = toys[i] # Temporarily store the current toy
      toys[i] = toys[j]
      toys[j] = temp # Update the current and next toy positions

# Print the sorted toy box
print("Sorted toys:", toys)
