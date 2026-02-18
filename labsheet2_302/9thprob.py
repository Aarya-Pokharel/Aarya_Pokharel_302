import math
import random

def acceptance_probability(delta_e, temperature):
    if delta_e < 0:
        return 1.0
    return math.exp(-delta_e / temperature)

def temperature_demo():
    delta_e = 3   # Inferior move (higher cost)
    temperatures = [100, 50, 10, 1, 0.1]

    print("\nTemperature Effect Demonstration:")
    for T in temperatures:
        prob = acceptance_probability(delta_e, T)
        print(f"Temperature: {T:6} -> Probability: {prob:.4f}")

temperature_demo()