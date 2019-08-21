# Uses python3
# least common multiplier
import sys

def gcd(a, b):
	while a % b != 0:
		remainder = a % b
		if remainder == 0:
			return b
		a = b
		b = remainder
	return b

def lcm(a, b):
	if a == 0 or b == 0:
		return 0
	gcd_val = gcd(a, b)
	lcm_val = int(a / gcd_val) * int(b / gcd_val) * int(gcd_val)
	return lcm_val

if __name__ == "__main__":
    #input = sys.stdin.read()
    a, b = tuple(map(int, input().split()))
    print(lcm(max(a, b), min(a, b)))