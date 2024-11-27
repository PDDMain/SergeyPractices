def process_numbers(numbers):
    result = 0
    for num in numbers:
        # Set a breakpoint here
        result += num
    return result

def main():
    numbers = [1, 2, 3, 4, 5]
    result = process_numbers(numbers)
    print(f"Sum of numbers is {result}")

if __name__ == "__main__":
    main()
