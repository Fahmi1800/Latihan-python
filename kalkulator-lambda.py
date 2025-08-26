#latihan kalkulator pake lambda
tambah = lambda angka1,angka2 : angka1+angka2
kurang = lambda angka1,angka2 : angka1-angka2
kali = lambda angka1,angka2 : angka1*angka2
bagi = lambda angka1,angka2 : angka1/angka2

while True :
    print("==KALKULATOR SEDERHANA==")
    angka1 = int(input('masukkan angka pertama : '))
    angka2 = int(input('masukkan angka ke dua : '))
    operator = str(input('masukkan operator [+ - * /] : '))

    if operator == '+' :
        print(f'hasil tambah adalah = {tambah(angka1,angka2)}\n')

    elif operator == '-' :
        print(f'hasil kurang adalah = {kurang(angka1,angka2)}\n')

    elif operator == '*' :
        print(f'hasil kali adalah = {kali(angka1,angka2)}\n')

    elif operator == "/" :
        if angka2 == 0 :
            print("hasilnya = tak terdefinisi")
        
        else :
            print(f'hasil bagi adalah = {bagi(angka1,angka2)}\n')
    
    else :
        print('masukkan operator yg benar!!')