# Uses python3
import sys

def gcd(a, b):
	while a % b != 0:
		remainder = a % b
		a = b
		b = remainder
	return b

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(max(a, b), min(a, b)))
