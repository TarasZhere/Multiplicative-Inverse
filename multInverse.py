# Taras Zherebetskyy
# Multiplicative invers finder
# given a mod world m, and a integer x for 0 <= x < m the algorithm will find the multiplicative inves of x in mod m

def multInvers(m, x):           #function with a simple while loop
    a = [0, 1]
    q = [None, None]
    r = [m, x]
    i = 1
    
    while r[i] > 1:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(r[i - 2] // r[i - 1])
        a.append((a[i-2] - q[i] * a[i - 1]) % m)
    
    print("\ti\tr[i]\tq[i]\ta[i]")
    for k in range(i + 1):
        print(f"\t{k}\t {r[k]}\t {q[k]}\t {a[k]}")

    if r[i] == 1: return a[i]
    else: return None

def multInversRecursion(r, x, a0, a1):
    if x == 1: return a1
    elif x == 0: return None
    else:
        global m
        return multInversRecursion(x, r % x, a1, (a0 - r // x * a1) % m)

#    MAIN START HERE
#   ATTENTION: change m and x for different tries
m = 15
x = 9


print(f"""
\t\t LOOP FUNCTION
Multiplicative inverse of {x} in mod {m} world is: {multInvers(m, x)}

\t\t RECURSION FUNCTION
Multiplicative inverse of {x} in mod {m} world is: {multInversRecursion(x, m % x, 1, (0 -  m // x * 1) % m)}
""")
