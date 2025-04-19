# Write Python code to:

# Print this exact triangle using for loops:


# *
# * *
# * * *
# * * * *
# * * * * *

# Then write the same triangle in reverse.

for x in range(6):
    for _ in range(x):
        print("* " * x)
        break

print('\n')
# In reverse
y = 6
z = 6
