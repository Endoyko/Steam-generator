import random
import string

def generate_random_code():
    """Generate a random code with three segments."""
    code = ''
    for _ in range(3):
        segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(4, 6)))
        code += segment + '-'
    return code[:-1]  # remove the last '-' character

def generate_multiple_codes(num_codes):
    """Generate multiple random codes."""
    codes = []
    for _ in range(num_codes):
        code = generate_random_code()
        codes.append(code)
    return codes

if __name__ == "__main__":
    num_codes = int(input("Enter the number of codes to generate: "))

    codes = generate_multiple_codes(num_codes)

    print("Generated Codes:", ', '.join(codes))
    print("Made by endoyko")
