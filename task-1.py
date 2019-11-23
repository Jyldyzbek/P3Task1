a = input('Vedite svoyu skasku: ')

zaglavnye = 0
propesnye = 0
simvoly = 0

for i in a:
    if i.isupper():
        zaglavnye += 1

    elif i.islower():
        propesnye += 1

    else:
        simvoly += 1

kolich_bukv = zaglavnye + propesnye
proc_kajd_buk = 100 / kolich_bukv
proc_zagl = proc_kajd_buk * zaglavnye
proc_propesnyh = proc_kajd_buk * propesnye

print('Procent propesnyh bukv: ', round(proc_propesnyh, 2), '%')
print('Procent zaglavnyh bukv: ', round(proc_zagl, 2), '%')