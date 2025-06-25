import math
import sys

def gcd(n1, n2):
    """Вычисляет наибольший общий делитель двух чисел."""
    n1 = abs(n1)
    n2 = abs(n2)
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def power(base, exp):
    """Быстрое возведение в степень для целых чисел."""
    if exp == 0:
        return 1
    if base == 0:
        return 0
    
    result = 1
    current_base = base
    current_exp = exp
    
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_exp //= 2
        if current_exp > 0:
            current_base *= current_base
    return result

def compute_eulerian(max_n):
    """Вычисляет числа Эйлера до заданного порядка."""
    A = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    A[0][0] = 1
    
    for n in range(1, max_n + 1):
        for k in range(0, n):
            term1 = (n - k) * A[n - 1][k - 1] if k > 0 else 0
            term2 = (k + 1) * A[n - 1][k]
            A[n][k] = term1 + term2
    return A

def main():
    # Чтение входных данных
    try:
        data = input().split()
        if len(data) < 2:
            raise ValueError("Недостаточно входных данных")
        
        a = int(data[0])
        b = int(data[1])
    except Exception as e:
        print(f"Ошибка чтения ввода: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Проверка диапазона
    if a < 1 or a > 10 or b < 1 or b > 10:
        print("Входные значения должны быть от 1 до 10.", file=sys.stderr)
        sys.exit(1)
    
    # Обработка специального случая
    if b == 1:
        print("infinity")
        return
    
    # Вычисление чисел Эйлера
    eulerian_numbers = compute_eulerian(a)
    
    # Вычисление числителя
    numerator = 0
    for j in range(a):
        term_power = power(b, a - j)
        term_product = eulerian_numbers[a][j] * term_power
        numerator += term_product
    
    # Вычисление знаменателя
    denominator = power(b - 1, a + 1)
    
    # Проверка знаменателя
    if denominator <= 0:
        print("Внутренняя ошибка: Вычисление знаменателя не удалось или результат неположительный.", file=sys.stderr)
        sys.exit(1)
    
    # Сокращение дроби
    common = gcd(numerator, denominator)
    p = numerator // common
    q = denominator // common
    
    print(f"{p}/{q}")

if __name__ == "__main__":
    main()