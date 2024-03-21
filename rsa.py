import random
import math
hex_word = []
so_nguyen_to = []
so_chu = {}
chu_so = {}
so_nguyen_to_2 = []
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(3, 200 * 200):
    if isPrime(i):
        so_nguyen_to_2.append(i)

for i in range(20, 200):
    if isPrime(i):
        so_nguyen_to.append(i)
for i in range(48, 58):
    hex_word.append(chr(i))
    
for i in range(97, 103):
    hex_word.append(chr(i))
    
for i in range(len(hex_word)):
    so_chu[so_nguyen_to[i]] = hex_word[i]

for i in so_chu:
    chu_so[so_chu[i]] = i
    
def choice_p():
    return random.choice(so_nguyen_to)
def choice_q():
    return random.choice(so_nguyen_to)
def choice_e(Pn):
    e = random.choice(so_nguyen_to_2)
    while e >=Pn:
        e = random.choice(so_nguyen_to_2)
    return e
def choice_d(Pn, e):
    r1 = Pn
    r2 = e
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)
     
    while r2 > 0:
         
        q = r1//r2
        r = r1-q * r2
        r1 = r2
        r2 = r
        s = s1-q * s2
        s1 = s2
        s2 = s
        t = t1-q * t2
        t1 = t2
        t2 = t
         
    if t1 < 0:
        t1 = t1 % Pn
         
    return t1
 
def en(n, d, ma_bam):
    chu_ky = ""
    for m in ma_bam:
        chu_ky += str((chu_so[m] ** d) % n) + " "
    return chu_ky
def de(n, e, chu_ky):
    ma_bam = ""
    list_chu_ky = list(map(int, chu_ky.split()))
    for c in list_chu_ky:
        if ((c ** e) % n) in so_chu:
            ma_bam += so_chu[((c ** e) % n)]
        else:
            return "Giải mã chữ ký không thành công!"
    return ma_bam