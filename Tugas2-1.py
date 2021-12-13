def fungsi(angka): 
    list = []
    for i in angka:   
        jumlah = angka.count(i)
        if jumlah == 1:
            list.append(i)   
    return list
            
a = input()
b = fungsi(a)
c = list(map(int,b))

print(c)