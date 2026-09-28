n = int(input())
is_valid_banknote = n == 5 \
    or n == 10 \
    or n == 20 \
    or n == 50 \
    or n == 100 \
    or n == 200 \
    or n == 500

print(is_valid_banknote)