list_data = [] #tampung data

while True :
    print('\n===TO DO LIST SEDERHANA===')
    print('1. Tampilkan tugas')
    print('2. Tambah tugas baru')
    print('3. Hapus tugas')
    print('4. Keluar')

    input_user = int(input('\nPilih opsi [1-4] : '))

    if input_user == 1 :
        print(f'\n=DAFTAR TUGAS=')
        if len(list_data) == 0 : #kondisi jika data list kosong (maka akan menampilkan pesan....)
            print('- tidak ada data -')
        
        else :
            for nomor,tugas in enumerate(list_data, start=1) :
                print(f'{nomor}. {tugas}') #menampilkan daftar tugas
        
        while True :
            opsi_keluar = str(input('kembali ke menu? [y] : ').lower())
            if opsi_keluar == "y" :
                break

            else :
                print('\nKETIK [y] UNTUK KEMBALI KE MENU!!')


    elif input_user == 2 :
        while True :
            input_tugas_baru = str(input('masukkan tugas baru : '))
            list_data.append(input_tugas_baru) #menambahkan ke dalam list
            print('\nTugas berhasil di tambahkan!!')

            while True :
                input_lagi = str(input('Tambahkan tugas lagi? [y/n] : ').lower())
                print('')
                
                if input_lagi == 'y' :
                    break
                elif input_lagi == 'n' :
                    break
                else :
                    print('MASUKKAN [y/n] !!!')

            if input_lagi == 'n' :
                break

    elif input_user == 3 :
        print('\n==HAPUS TUGAS==')
        for nomor,tugas in enumerate(list_data, start=1):
            print(f'{nomor}. {tugas}')

        while True :
            input_hapus = int(input('Pilih list yg mau di hapus :')) #membuat variabel yg akan di gunakan .pop (bernilai integer)
            hapus_data = list_data.pop(input_hapus-1)

            print(f'tugas "{hapus_data}" berhasil di hapus!')

            for nomor,tugas in enumerate(list_data, start=1):
                print(f'{nomor}. {tugas}')

            hapus_lagi = str(input('hapus list lagi? [y/n] : ').lower())

            if hapus_lagi == "y" :
                pass

            elif hapus_lagi == "n" :
                break

            else :
                print('MASUKKAN [y/n]!!!')
    
    elif input_user == 4 :
        print('terimakasih, semoga harimu menyenangkan :)'.capitalize())
        break


