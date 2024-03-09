import time

start_time = time.time()
prime_list = [2, 3, 5, 7, 11, 13]
big_prime_list = prime_list.copy()

def prime_incr(prime_number):
    return prime_number + 1

def prime_check(prime_number, prime_list):
    for i in range(len(prime_list)):
        if prime_number%prime_list[i] == 0:
            return False
    return True

# Mainloop
count = 6
temp_prime = prime_list[-1] + 1

limit = 100

while temp_prime <= limit:
    is_prime = prime_check(temp_prime, prime_list)
    if is_prime:
        prime_list.append(temp_prime)
        count += 1
    else:
        temp_prime = prime_incr(temp_prime)
end_time = time.time()


# n^2 + a*n + b needs to provide prime values. n + a needs to be not a multiple of b. Hence b is always a prime.
# The value of a can change from -b to b with only primes. 

big_prime_list = prime_list.copy()
prime_list = prime_list[::-1]

temp_prime = big_prime_list[-1] + 1

while temp_prime <= 2*limit**2 + limit:
    is_prime = prime_check(temp_prime, big_prime_list)
    if is_prime:
        big_prime_list.append(temp_prime)
        count += 1
    else:
        temp_prime = prime_incr(temp_prime)

print('The prime dictionary is complete')

big_prime_list_set = set(big_prime_list)

def all_prime(temp_list):
    if set(temp_list).issubset(big_prime_list_set) == True:
        return True
    else:
        return False

negative_prime_list = [[prime, -prime] for prime in prime_list]
negative_prime_list = sum(negative_prime_list, [])

count = 0
for temp_a in negative_prime_list:
    count += 1
    if count == 100:
        raise IndexError('Too many possibilities have been run')
    for temp_b in prime_list:
        trial_list = [i*2 + temp_a*i + temp_b for i in range(abs(temp_a))]
        is_prime = all_prime(trial_list)
        if is_prime == True:
            print(trial_list)
            print(temp_a, temp_b)
            raise ValueError('Some output found')
        

# print('The total run time is ', end_time - start_time)