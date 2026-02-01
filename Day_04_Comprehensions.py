def main():
    # 1. Comparing sequences
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(f"Is a == b? {a == b}")

    # 2. List Comprehension
    odds = [x for x in range(20) if x % 2 != 0]
    print(f"Odds: {odds}")

    # 3. Set Comprehension
    # String එකක ඇති අකුරු වලින් vowels පමණක් unique ලෙස ගැනීම
    s = "advanced python is awesome"
    vowels = {char for char in s if char in 'aeiou'}
    print(f"Vowels: {vowels}")

    # 4. Dictionary Comprehension
    # Celsius අගයන් Fahrenheit වලට හැරවීම
    temp_c = [0, 10, 20, 30]
    temp_f = {t: (t*9/5) + 32 for t in temp_c}
    print(f"Temp_c: {temp_c}")
    print(f"Temp_f: {temp_f}")



if __name__ == "__main__":
    main()