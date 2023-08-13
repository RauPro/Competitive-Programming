#include <iostream>
#include <vector>
#include <cmath>

long long computeQuadraticValue(long long X, const std::vector<long long>& Y) {
    long long sum = 0;
    for (long long y : Y) {
        sum += (2*X + y) * (2*X + y);
    }
    return sum;
}

std::pair<double, double> solveQuadratic(double a, double b, double c) {
    double discriminant = b*b - 4*a*c;
    if (discriminant < 0) {
        return {NAN, NAN};  // No hay soluciones reales
    }
    double x1 = (-b + sqrt(discriminant)) / (2*a);
    double x2 = (-b - sqrt(discriminant)) / (2*a);
    return {x1, x2};
}

int main() {
    std::vector<double> Y = { 9181 ,4243, 7777, 1859, 2017, 4397, 14, 9390, 2245, 7225};

    long long M = 635472106413848880;

    // Coeficientes para la ecuación cuadrática
    double a = Y.size();
    double b = 0;
    for (long long y : Y) {
        b += 2*y;
    }
    double c = 0;
    for (long long y : Y) {
        c += (double)y*y;
    }
    c -= M;

    std::pair<double, double> solutions = solveQuadratic(a, b, c);

    std::cout << "X1: " << solutions.first << ", X2: " << solutions.second << std::endl;

    return 0;
}
