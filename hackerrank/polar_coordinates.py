# question --> https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

from cmath import phase

cnum = complex(input())

print(abs(complex(cnum.real, cnum.imag)))
print(phase(complex(cnum.real, cnum.imag)))

