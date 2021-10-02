a = 4.0 / 10.0 + 3.5 * 2
print(a)

b = 10 % 4 + 6 / 2
print(b)

c = abs(4 - 20//3)**3
print(c)

import math
def formular():
    a = int(input("pls, type in your a value "))
    b = int(input("pls, type in your b value "))
    r = int(input("pls, type in your r value "))
    cos_a = math.cos(a)**2
    sin_b = math.sin(b)**2
    r_cos_a = r * cos_a
    r_sin_b = r * sin_b
    sum_ab =  r_cos_a + r_sin_b
    ans = math.sqrt(sum_ab)

    print(ans)
    print(cos_a, sin_b)
    print(r_cos_a, r_sin_b)
formular()

   
