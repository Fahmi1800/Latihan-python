#kalkulator pake function

def tambah(angka1,angka2):
    hasil = angka1 + angka2
    return hasil

def kurang(angka1,angka2):
    hasil = angka1 - angka2
    return hasil

def kali(angka1,angka2):
    hasil = angka1 * angka2
    return hasil

def bagi(angka1,angka2):
    hasil = angka1 / angka2
    return hasil

while True :
    angka1 = int(input('masukkan angka pertama : '))
    angka2 = int(input('masukkan angka ke dua : '))
    operator = str(input('pilih operator [+ - * /] : '))

    if operator == "+" :
        print(f'hasil tambah adalah = {tambah(angka1,angka2)}\n')

    elif operator == "-":
        print(f'hasil pengurangan adalah = {kurang(angka1,angka2)}\n')

    elif operator == "*" :
        print(f'hasil kali adalah = {kali(angka1,angka2)}\n')

    elif operator == '/':
        if angka2 == 0 :
            print('tak terdefinisi')

        else :
            print(f'hasil bagi adalah = {bagi(angka1,angka2)}')

