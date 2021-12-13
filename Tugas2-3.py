def fungsi(kata):
    dik = {}
    for i in kata:
        dik[i] = kata.count(i)
    for i,v in dik.items():
        a = i,':', v
        print(i + '=' + str(v))
    return a 

a = input().split()
fungsi(a)