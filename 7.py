# 10001 st prime number

# Given first six prime numbers

prime_list = [2, 3, 5, 7, 11, 13]

def prime_incr(prime_number):
    return prime_number + 1

def prime_check(prime_number, prime_list):
    for i in range(len(prime_list)):
        if prime_number%prime_list[i] == 0:
            #raise ValueError
            return True
    #raise IndexError
    return False

# Mainloop
count = 6
temp_prime = prime_list[-1] + 1

while count <= 10000:
    a = prime_check(temp_prime, prime_list)
    if a:
        temp_prime = prime_incr(temp_prime)
    else:
        prime_list.append(temp_prime)
        #print('Next prime number is', temp_prime)
        count += 1

print(prime_list[10000])
