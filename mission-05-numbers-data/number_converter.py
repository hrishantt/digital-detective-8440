"""
Mission 5: Number Converter
Author: Hrishant (USN ends in 8440)
Description: Prompts the user for a decimal integer, validates input,
and outputs its binary and hexadecimal representations.
"""

def main():
    print("=" * 35)
    print("       DIGITAL NUMBER CONVERTER      ")
    print("=" * 35)
    user_input = input("Enter a positive decimal integer: ").strip()

    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Error: Please enter a positive decimal integer (>= 0).")
            return

        # Built-in conversions
        binary_val = bin(decimal_val)       # returns string like '0b1101'
        hex_val = hex(decimal_val).upper()  # returns string like '0XD' or '0X1F'
        # Format cleanly with uppercase hex letters and lowercase '0x' prefix
        clean_hex = "0x" + hex(decimal_val)[2:].upper()

        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10):     {decimal_val}")
        print(f"Binary (Base 2):       {binary_val}")
        print(f"Hexadecimal (Base 16): {clean_hex}")
        print("=" * 35)

    except ValueError:
        print("Error: Invalid input. Please enter a valid decimal integer.")


if __name__ == "__main__":
    main()
