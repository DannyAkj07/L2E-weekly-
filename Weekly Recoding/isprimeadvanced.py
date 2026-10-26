def is_prime(num: int) -> bool:
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def sum_prime_num(num: int):
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")

    prime_nums = []
    sum_prime = 0
    i = 2
    while i <= num:
        if is_prime(i):
            prime_nums.append(i)
            sum_prime += i
        i += 1
    
        
    print(f"Primes up to {num}: {prime_nums}")
    print(f"Sum of primes: {sum_prime}")


sum_prime_num(10)
