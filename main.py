import math
#how many seconds in a year
secs = 60 * 60 * 24 * 7
print(secs)

#volume of a sphere radius =10
vol = 4/3  * math.pi * 10 ** 3
print(vol)

#go board combinations
combos = 3 ** (19*19)
print (combos)

#find number in the hundreds
n = 12351113345 # any non negative integer
dig = (n % 1000) // 100
print(dig)

#find 4s bit
n = 1167
chunk = n % 8
if chunk >= 4:
    bit = 1
else:
    bit = 0
print(bit)