diners = int(input())

is_valid = diners == 5 \
    or diners == 10 \
    or diners == 20 \
    or diners == 50 \
    or diners == 100 \
    or diners == 200 \
    or diners == 500

print(is_valid)