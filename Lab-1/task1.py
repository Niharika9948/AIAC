def is_valid_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
text = input("Enter a string: ")
print(is_valid_palindrome(text))  # Output: True