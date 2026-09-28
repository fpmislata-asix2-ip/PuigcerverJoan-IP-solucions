a = int(input())
b = int(input())
c = int(input())

es_a_major_bc = a < b + c
es_b_major_ac = b < a + c
es_c_major_ab = c < a + b

es_valid = es_a_major_bc and es_b_major_ac and es_c_major_ab

print(es_valid)