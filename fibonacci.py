#!/usr/bin/python
a = 1
b = 2
c = 0
i = 10
print a, b,
while i != 0:
	c = b+a
	a = b
	b = c
	print b,
	i -= 1
raw_input()