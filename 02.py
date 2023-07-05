# Find the sum of all even-valued values in the Fibonacci sequence whose values do not exceed four million.

prev_no = 1
current_no = 2
next_no = 0
sum = 2 # even numbers only

while current_no < 4000000:
    next_no = current_no + prev_no
    prev_no = current_no
    current_no = next_no
    print(current_no)
    if current_no % 2 == 0 and current_no <= 4000000:
        sum += current_no

print('The sum is {}.'.format(sum))