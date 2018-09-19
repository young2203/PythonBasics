def gcd(m, n):
    # Get maximum factor
    while n != 0:
        m , n = n, m%n
    return abs(m)