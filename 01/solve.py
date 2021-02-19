#!/usr/bin/env python3

from collections import deque
from sys import stdin

data = [int(l.strip()) for l in stdin.readlines()]

def calculate_fuel(mass):
  return int(mass / 3) - 2

def calculate_fuel_total(mass):
  last = calculate_fuel(mass)
  total = last
  while last > 0:
    last = max(0, calculate_fuel(last))
    total += last
  return total

print(sum(calculate_fuel(value) for value in data))
print(sum(calculate_fuel_total(value) for value in data))

