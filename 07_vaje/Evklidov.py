def Evklid(a, b):
    """
    Evklidov algoritem
    """
    r = max(a, b)
    q = min(a, b)

    if q == 0:
        return r
    else:
        return Evklid(q, r % q)

print(Evklid(42, 49))
print(Evklid(157128, 919182))

    