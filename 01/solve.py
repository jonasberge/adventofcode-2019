#!/usr/bin/env python3

from collections import deque
from sys import stdin

data = [int(l.strip()) for l in stdin.readlines()]

def calculate_fuel(mass):
  return int(mass / 3) - 2

result = sum(calculate_fuel(value) for value in data)
print(result)

