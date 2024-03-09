# import inflect
import time

start_time = time.time()
#======================================================================
# making a dictionary for numbers

main_dict = {1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine',
             10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             17: 'seventeen',
             18: 'eighteen',
             19: 'ninteen',
             20: 'twenty'}

units = {1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

tens = {1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'}


def unit_function(unit):
    if int(unit) != 0:
        return units.get(int(unit))
    else:
        return ''

def tens_function(ten):
    if int(ten) != 0:
        return tens.get(int(ten))
    else:
        return ''

def hundred_function(hund, next):
    # next is the sum of the next two digits
    if int(hund)!= 0:
        if int(next)!= 0:
            return units.get(int(hund)) + ' hundred and '
        else:
            return units.get(int(hund)) + ' hundred'
    else:
        return ''
    
def thousand_function(thousand):
    if len(thousand) == 2:
        if int(thousand) > 10 and int(thousand) < 20:
            return main_dict(int(thousand))
        else:
            return tens_function(thousand[0]) + unit_function(thousand[1])
    else:
        return unit_function(thousand[0])
    
def last_two(digits):
    digits_int = int(digits)
    if digits_int == 0:
        return ''
    elif digits_int > 10 and digits_int < 20:
        return main_dict.get(digits_int)
    else:
        return tens_function(digits[-2]) + unit_function(digits[-1])

def number_dictionary(max_value, main_dict):

    for i in range(21, max_value + 1):
        number = str(i)

        l = len(number)

        if l == 2:
            main_dict[int(number)] = last_two(number[-2:])
        elif l == 3:
            main_dict[int(number)] = hundred_function(number[-3], number[-2:]) + last_two(number[-2:])
        elif l == 4 or l == 5:
            main_dict[int(number)] = thousand_function(number[:-3]) + ' thousand' + hundred_function(number[-3], number[-2:]) + last_two(number[-2:])
        else:
            raise ValueError('The input value is higher than 99999')
        
    return main_dict


dict = number_dictionary(1000, main_dict)

def number_of_char(a):
    words = a.split(' ')
    temp = 0
    for i in words:
        temp += len(i)
    return temp

total_total = 0
for i in range(1, 1001):
    number_total = number_of_char(dict.get(i))
    total_total += number_total
end_time = time.time()
print(total_total)
print('The run time is ', end_time - start_time)


raise SystemExit