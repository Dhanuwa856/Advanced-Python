import string

def main():
    test_str = 'The quick brown fox jumps over the lazy dog.'

    # 1. Built-in String Constants
    print("--- constants ---")
    print(f"Punctuation: {string.punctuation}")
    print(f"digits: {string.digits}")

    # 2. String Searching
    print("\n--- Searching ---")
    print(f"Count of 'the': {test_str.lower().count('the')}")
    print(f"Strat with 'The': {test_str.startswith('The')}")

    # 3. String Manipulation
    print("\n--- Manipulation ---")
    # Punctuation ඉවත් කිරීමේ දියුණු ක්‍රමය (translate)
    sample = "Hello! User, how's it going?"
    table = str.maketrans("","",string.punctuation)
    print(f"Cleaned String: {sample.translate(table)}")

    # 4. String Formatting
    print("\n--- Formatting ---")
    name = "Dhanushka"
    status = "Learning"
    print("User {0} is currently {1}".format(name, status))


if __name__ == "__main__":
    main()