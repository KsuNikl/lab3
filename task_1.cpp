#include <cmath>
#include <utility>
#include <iostream>
#include <iomanip>
using namespace std;

pair<float, float> fx(float x)
{
    float y;

    if (x >= -10 && x < -6)
    {
        // -10 <= x < -6: (x + 8)^2 - (y+2)^2 = 4  => y = -sqrt(4 - (x + 8)^2) + 2
        y = -sqrtf(4.0f - (x + 8.0f) * (x + 8.0f)) + 2.0f;
    }
    else if (x >= -6 && x < -4)
    {
        // -6 <= x < -4: y = 2
        y = 2.0f;
    }
    else if (x >= -4 && x < 2)
    {
        // -4 <= x < 0: прямая через точки (-4,2) и (0,-1)
        // y = -0.5*x
        if (x != 0)
        {
            y = -0.5f * x;
        }
        else
        {
            y = 0.0f;
        }
    }
    else if (x >= 2 && x <= 4)
    {
        // 2 <= x <= 4: прямая через точки (2,-1) и (4,1)
        // y = x - 3
        y = x - 3.0f;
    }
    else
    {
        // x вне допустимого диапазона
        y = NAN;
    }

    return {x, y};
}
int main()
{
    // Лучше сразу читать x_start, x_end как float, чтобы шаг мог быть дробным
    float x_start, x_end, step;
    cout << "Через пробел введите x начальное, x конечное и шаг x: ";
    cin >> x_start >> x_end >> step;

    cout << fixed << setprecision(2);
    cout << setw(8) << "x" << setw(10) << "y" << endl;
    cout << "-------------------------" << endl;
    for (float x = x_start; x <= x_end; x += step)
    {
        auto p = fx(x);
        cout << setw(8) << p.first << setw(10) << p.second << endl;
    }
    return 0;
}
