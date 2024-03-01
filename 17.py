import inflect
import time


start_time = time.time()
def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

def number_of_char(a):
    words = a.split(' ')
    last_two = words[-1].split('-')
    final = words[:-1]+last_two
    temp = 0
    for i in final:
        temp += len(i)

    return temp

# main loop

number_total = 0
total_total = 0

for i in range(1, 1001):
    number_total = number_of_char(number_to_words(i))
    total_total += number_total
end_time = time.time()
print(total_total)
print('The run time is ', end_time - start_time)