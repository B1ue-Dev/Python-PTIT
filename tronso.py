def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def reverse_number(num):
    return int(str(num)[::-1])

def find_emirp_numbers(limit, is_prime):
    emirp_numbers = []
    for num in range(2, limit):
        if is_prime[num]:
            reversed_num = reverse_number(num)
            if reversed_num != num and reversed_num < limit and is_prime[reversed_num]:
                emirp_numbers.append(num)
    return emirp_numbers

# Đọc số test cases
T = int(input())
test_cases = [int(input()) for _ in range(T)]

# Tạo danh sách các số nguyên tố
MAX_N = 10**6
is_prime = sieve_of_eratosthenes(MAX_N)

# Tìm các số Emirp nhỏ hơn MAX_N
emirp_numbers = find_emirp_numbers(MAX_N, is_prime)

# Xử lý từng test case
for N in test_cases:
    result = [str(num) for num in emirp_numbers if num < N]
    print(" ".join(result))
