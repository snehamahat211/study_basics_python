def  prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i == 0:
            is_prime=False
    if is_prime:
        print("its a prime number")
    else:
        print("its a non-prime number")

n=int(input("check this number"))
prime_checker(number=n)
