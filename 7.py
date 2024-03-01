# 10001 st prime number

# Given first six prime numbers

prime_list = [2, 3, 5, 7, 11, 13]

def prime_incr(prime_number):
    return prime_number + 1

def prime_check(prime_number, prime_list):
    for i in range(len(prime_list)):
        if temp_prime%prime_list[i] == 0:
            raise ValueError
    raise IndexError


# Mainloop
count = 6
temp_prime = prime_list[-1] + 1

while count <= 10000:
    try:
        prime_check(temp_prime, prime_list)
    except ValueError:
        temp_prime += 1
    except IndexError:
        prime_list.append(temp_prime)
