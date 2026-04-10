import random

def generate_random_numbers(n, lower_bound, upper_bound):
    for _ in range(n):
        num = random.randint(lower_bound, upper_bound)
    return num

if generate_random_numbers(1,1,50) % 2 == 0:
    print("옷 입어라 나가게.")
else:
    print("얌전히 집에 박혀 있어.")