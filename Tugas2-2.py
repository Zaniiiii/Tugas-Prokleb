def fungsi(angka):
    target = angka[-1]
    for i in angka:
        for j in angka:
            if int(i) + int(j) == int(target):
                return [angka.index(i),angka.index(j)]

n = input().split()
print (fungsi(n))