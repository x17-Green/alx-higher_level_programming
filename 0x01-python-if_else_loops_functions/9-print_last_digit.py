#!/usr/bin/python3
def print_last_digit(number):
	if number < 0:
		last_n = number % -(10)
		print(-(last_n), end='')
	else:
		last_n = number % 10
		print(last_n, end='')
		print(end='')
	return abs(last_n)

