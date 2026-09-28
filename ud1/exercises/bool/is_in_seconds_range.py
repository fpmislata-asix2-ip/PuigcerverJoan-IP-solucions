n = int(input())

is_in_range = n >= 0 and n <= 59 # A and B
is_in_range = not (n < 0 or n > 59) # !(!A or !B)

print(is_in_range)