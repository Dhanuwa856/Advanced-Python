import itertools

def main():
    # 1. Basic Iterator
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    i = iter(days)
    print(next(i)) # Sun
    print(next(i)) # Mon

    # 2. Itertools: count
    print("\n--- Count ---")
    for n in itertools.count(10, 2):
        print(n)
        if n >= 16: break

    # 3. Itertools: accumulate
    print("\n--- Accumulate ---")
    nums = [10, 20, 30, 40, 50]
    acc = itertools.accumulate(nums)
    print(list(acc)) # [10, 30, 60, 100, 150]

    # 4. Itertools: chain
    print("\n--- Chain ---")
    combined = itertools.chain("ABC", "123")
    print(list(combined)) # ['A', 'B', 'C', '1', '2', '3']

if __name__ == "__main__":
    main()