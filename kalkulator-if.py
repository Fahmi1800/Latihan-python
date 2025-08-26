#kalkulator pake if elif
while True :
    print('==KALKULATOR SEDERHANA==')
    angka1 = int(input('masukkan angka pertama : '))
    angka2 = int(input('masukkan angka ke dua : '))
    operator = str(input('pilih operator [+ - * /] : '))

    if operator == "+" :
        hasil = angka1 + angka2
        print(f'hasil tambah adalah = {hasil}\n')

    elif operator == "-" :
        hasil = angka1 - angka2
        print(f'hasil kurang adalah = {hasil}\n')

    elif operator == "*" :
        hasil = angka1 * angka2
        print(f'hasil kali adalah = {hasil}\n')

    elif operator == "/" :
        if angka2 == 0 :
            print(f'hasilnya = tak terdefinisi\n')
        
        else :
            hasil = angka1 / angka2
            print(f'hasil bagi adalah = {hasil}\n')

    else :
        print('MASUKKAN OPERATOR YG BENAR!!\n')
