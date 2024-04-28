import time
import numpy as np

init_time = time.time()
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

while count <= 10**3:
    is_prime = prime_check(temp_prime, prime_list)
    if is_prime:
        prime_list.append(temp_prime)
        count += 1
    else:
        temp_prime = prime_incr(temp_prime)

print('The highest reached prime number is ',prime_list[-1])

h = int(input('Should the simulation continue? '))
if h != 1:
    raise SystemExit('The simulation was stopped by you')

prime_list_big = prime_list.copy()
b_list = [x for x in prime_list if x <= 1000]
del prime_list
b_list = list(-np.array(b_list))+b_list

n_dict = {'40': (1, 41)}

for b in b_list:
    for a in range(-b,b):
        for n in range(0, b):
            n_high = int(list(n_dict.keys())[-1])
            temp_val = n**2 + a*n + b
            
            if temp_val in prime_list_big:
                pass
            else:
                if n >= n_high:
                    n_dict[str(n)] = (a, b)
                break
final_time = time.time()
print(final_time - init_time)           
print(n_dict)