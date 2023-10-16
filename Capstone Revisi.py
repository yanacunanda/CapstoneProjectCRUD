from tabulate import tabulate
TabelUtama = [
    ['Chicken Nugget', 'Makanan Frozen', 200, 'pcs'],
    ['Sosis Ayam', 'Makanan Frozen', 210, 'pcs'],
    ['Kebab Mini', 'Makanan Frozen', 300, 'pcs'],
    ['Bakso Mini', 'Makanan Frozen', 150, 'pcs'],
    ['Wonton Mini','Makanan Frozen', 175, 'pcs']
]

def printing_tabel ():
    print('Daftar stock barang')
    indexed_data =[]
    for index,row in enumerate(TabelUtama):
        indexed_data.append([index]+row)
    tabel = tabulate(indexed_data,headers=['No.','Nama Barang','Jenis Barang','Jumlah Barang','Satuan'])
    print(tabel)

Cart_Ambil = []        

def printing_cart_ambil():
    tabel_cart = tabulate(Cart_Ambil,headers=['Nama Barang','Jenis Barang','Jumlah Barang Diambil','Satuan'])
    print ('Daftar barang yang diambil')
    print(tabel_cart)

Cart_Tambah = []

def printing_cart_tambah():
    tabel_cart = tabulate(Cart_Tambah,headers=['Nama Barang','Jenis Barang','Jumlah Barang Ditambah','Satuan'])
    print ('Daftar barang yang ditambah')
    print(tabel_cart)

while True:
    pilihanmenu=input('''
                      Selamat datang di gudang makanan frozen
                      
                      List menu:
                      1. Menampilkan daftar stock gudang
                      2. Menambahkan jenis barang
                      3. Menghapus jenis barang
                      4. Mengambil stock barang
                      5. Menambah stock barang
                      6. Exit
                      Masukkan menu yang diinginkan: ''')
    if pilihanmenu == '1':
        printing_tabel()

    if pilihanmenu == '2':
        while True:
            menu_2 = input('''
                           1. Menambah jenis barang
                           2. Keluar dari menu
                           Pilih menu yang diinginkan: ''')
            if menu_2 == '2':
                break
            else:
                Nama_Barang_Baru = input('Masukkan nama barang baru: ')
                Jenis_Barang_Baru = input('Masukkan jenis barang baru: ')
                Jumlah_Barang_Baru = int(input('Masukkan jumlah barang baru: '))
                Satuan = 'pcs'
                exist = False
                for i in TabelUtama:
                    if Nama_Barang_Baru.title() == i[0]:
                        exist = True
                        print('Barang sudah ada mohon masukkan nama barang lain.')
                        break
                if not exist:
                    TabelUtama.append([Nama_Barang_Baru.title(),Jenis_Barang_Baru.title(),Jumlah_Barang_Baru,Satuan])
                    printing_tabel()
                    
                
    if pilihanmenu == '3':
        while True:
            menu_3 = input('''
                           1. Menghapus jenis barang
                           2. Keluar dari menu
                           Pilih menu yang diinginkan: ''')
            if menu_3 == '2':
                break
            else:
                printing_tabel()
                Nama_Hapus = input('Masukkan nama barang yang akan dihapus: ')
                for i in TabelUtama:
                    if Nama_Hapus.title() == i[0]:
                        TabelUtama.remove(i)
                    printing_tabel()
        
    if pilihanmenu == '4':
        while True:
            menu_4 = input('''
                           1. Mengambil stock
                           2. Keluar dari menu
                           Pilih menu yang diinginkan: ''')
            if menu_4 == '2':
                break
            else:
                printing_tabel()
                Nama_Ambil = input('nama barang yang stocknya akan diambil: ')
                Quantity_Ambil = int(input('Masukkan jumlah barang yang akan diambil: '))
                Satuan = 'pcs'
                for i in TabelUtama:
                    if Nama_Ambil.title() == i[0]:
                        if Quantity_Ambil > i[2]:
                            print ('Jumlah stock kurang, silahkan masukkan angka yang benar.')
                            break
                        if Quantity_Ambil <= i[2]:
                            Cart_Ambil.append([i[0],i[1],Quantity_Ambil,Satuan])
                            i[2] -= Quantity_Ambil
                            printing_cart_ambil()
                            Cart_Ambil.clear()
                            printing_tabel()
                            break    

    if pilihanmenu == '5':
        
        while True:
            menu_5 = input('''
                           1. Menambah jumlah stock
                           2. Keluar dari menu
                           Pilih menu yang diinginkan: ''')
            if menu_5 == '2':
                break
            else:
                printing_tabel()
                Nama_Tambah = input('nama barang yang stocknya akan ditambah: ')
                Quantity = int(input('Masukkan jumlah barang yang akan ditambah: '))
                Satuan = 'pcs'
                for i in TabelUtama:
                    if Nama_Tambah.title() == i[0]:
                        Cart_Tambah.append([i[0],i[1],Quantity,Satuan])
                        i[2] += Quantity
                        printing_cart_tambah()
                        Cart_Tambah.clear()
                        printing_tabel()
                        break
            
    if pilihanmenu == '6':
        break

