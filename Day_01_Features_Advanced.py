import pprint


def my_function():
    """මෙය පරීක්ෂණ function එකකි.
    Docstrings වල වැදගත්කම මෙහි පෙන්වයි."""
    return True


def main():
    # 1. Docstrings
    print(my_function.__doc__)

    # 2. Special Variables
    print(f"Current File: {__file__}")
    print(f"Module Name: {__name__}")

    # 3. Walrus Operator (Assignment Expression)
    # අගයක් assign කරමින්ම පරීක්ෂා කිරීම
    if (n := len([1, 2, 3, 4, 5])) > 3:
        print(f"List is too long with {n} elements")

    # 4. pprint vs print
    data = {
        "id": 1, "name": "Joe Marini",
        "courses": ["Python", "C#", "C++", "Java"],
        "metadata": {"status": "active", "level": "advanced"}
    }

    print("\n--- Normal Print ---")
    print(data)

    print("\n--- Pretty Print ---")
    pprint.pprint(data)


if __name__ == "__main__":
    main()