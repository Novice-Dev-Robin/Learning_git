import random

def generate_random_numbers(n, lower_bound, upper_bound):
    random_numbers = []
    for _ in range(n):
        num = random.randint(lower_bound, upper_bound)
        random_numbers.append(num)
    return random_numbers

print(generate_random_numbers(1,1,2))
if generate_random_numbers(1,1,4) == [1]:
    print("옷 입어라 나가게.")
else:
    print("얌전히 집에 박혀 있어.")