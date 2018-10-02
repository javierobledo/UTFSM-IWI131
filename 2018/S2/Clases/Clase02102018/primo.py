def primo(n):
    i = 2
    es_primo = True
    while i < n:
        if n % i == 0:
            es_primo = False
        i += 1
    return es_primo