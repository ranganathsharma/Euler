# 10001 st prime number

# Given first six prime numbers
import time

start_time = time.time()
prime_list = [2, 3, 5, 7, 11, 13]

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

while count <= 10000:
    is_prime = prime_check(temp_prime, prime_list)
    if is_prime:
        prime_list.append(temp_prime)
        count += 1
    else:
        temp_prime = prime_incr(temp_prime)
        #print('Next prime number is', temp_prime)
end_time = time.time()

print(prime_list[10000])
print('The total run time is ', end_time - start_time)