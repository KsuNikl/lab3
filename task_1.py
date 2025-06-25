import math

def fx(x):
    if -10 <= x < -6:
        y = -math.sqrt(4.0 - (x + 8.0) ** 2) + 2.0
    elif -6 <= x < -4:
        y = 2.0
    elif -4 <= x < 2:
        if x != 0:
            y = -0.5 * x
        else:
            y = 0.0
    elif 2 <= x <= 4:
        y = x - 3.0
    else:
        y = float('nan')
    return x, y

def main():
    x_start, x_end, step = map(float, input("Через пробел введите x начальное, x конечное и шаг x: ").split())
    print(f"{'x':>8}{'y':>10}")
    print("-------------------------")
    x = x_start
    while x <= x_end + 1e-8:
        x_val, y_val = fx(x)
        print(f"{x_val:8.2f}{y_val:10.2f}")
        x += step

if __name__ == "__main__":
    main()