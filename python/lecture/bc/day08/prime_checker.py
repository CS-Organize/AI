def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("\033[0;32mIt's a prime")
    else:
        print("\033[0;31mIt's not a prime")

n = input("Check this number: ")
prime_checker(int(n))
