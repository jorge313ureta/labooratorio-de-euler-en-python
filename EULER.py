# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 16:43:37 2025

@author: jorge-ureta
"""

import math

def euler(f, x0, y0, x_target, h):
    x = x0
    y = y0
    while x < x_target:
        h_step = h if x + h <= x_target else x_target - x
        y += h_step * f(x, y)
        x += h_step
    return y

# Ejercicio 1: dy/dx = 0.2*x*y, y(1) = 1, aproximar y(1.5)
def f1(x, y):
    return 0.2 * x * y

x0_1, y0_1 = 1.0, 1.0
x_target_1 = 1.5

# Aproximaciones con h=0.1 y h=0.05
approx1_h1 = euler(f1, x0_1, y0_1, x_target_1, 0.1)
approx1_h05 = euler(f1, x0_1, y0_1, x_target_1, 0.05)

# Solución exacta Ejercicio 1
def exact1(x):
    return math.exp(0.1 * x**2 - 0.1)

exact_val_1 = exact1(x_target_1)
error1_h1 = exact_val_1 - approx1_h1
error1_h05 = exact_val_1 - approx1_h05

print("Ejercicio 1:")
print(f"Aproximación con h=0.1: {approx1_h1:.6f}, Error: {error1_h1:.6f}")
print(f"Aproximación con h=0.05: {approx1_h05:.6f}, Error: {error1_h05:.6f}\n")

# Ejercicio 2: dI/dt = 15 - 3I, I(0) = 0, aproximar I(0.5)
def f2(t, I):
    return 15 - 3 * I

t0_2, I0_2 = 0.0, 0.0
t_target_2 = 0.5

# Aproximaciones con h=0.1 y h=0.05
approx2_h1 = euler(f2, t0_2, I0_2, t_target_2, 0.1)
approx2_h05 = euler(f2, t0_2, I0_2, t_target_2, 0.05)

# Solución exacta Ejercicio 2
def exact2(t):
    return 5 * (1 - math.exp(-3 * t))

exact_val_2 = exact2(t_target_2)
error2_h1 = exact_val_2 - approx2_h1
error2_h05 = exact_val_2 - approx2_h05

print("Ejercicio 2:")
print(f"Aproximación con h=0.1: {approx2_h1:.6f}, Error: {error2_h1:.6f}")
print(f"Aproximación con h=0.05: {approx2_h05:.6f}, Error: {error2_h05:.6f}")