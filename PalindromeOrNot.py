def check_palindrome(s):
    if len(s) <= 4:
        print("Error: Please enter a string with more than four letters.")
    else:
        # Remove case and spaces for palindrome check
        s_clean = s.replace(" ", "").lower()
        if s_clean == s_clean[::-1]:
            print(f'"{s}" is a palindrome.')
        else:
            print(f'"{s}" is not a palindrome.')

# Example usage
user_input = input("Enter a string: ")
check_palindrome(user_input)