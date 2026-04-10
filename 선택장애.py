import random

def generate_random_numbers(n, lower_bound, upper_bound):
    random_numbers = []
    for _ in range(n):
        num = random.randint(lower_bound, upper_bound)
        random_numbers.append(num)
    return random_numbers

print(generate_random_numbers(3,1,10))