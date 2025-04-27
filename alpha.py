
# Method 1: Using lowercase ASCII values
for letter_code in range(ord('a'), ord('z')+1):
    print(chr(letter_code), end=' ')
print()  # For newline after completion

# Method 2: Using string module
import string
for letter in string.ascii_lowercase:
    print(letter, end=' ')
print()

# Method 3: List comprehension (single-line version)
print(' '.join([chr(i) for i in range(ord('a'), ord('z')+1)]))

