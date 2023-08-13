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
    tabel_cart = tabulate(Cart_Ambil,headers=['Nomor Index','Nama Barang','Jenis Barang','Jumlah Barang Diambil','Satuan'])
    print ('Daftar barang yang diambil')
    print(tabel_cart)

Cart_Tambah = []

def printing_cart_tambah():
    tabel_cart = tabulate(Cart_Tambah,headers=['Nomor Index', 'Nama Barang','Jenis Barang', 'Jumlah Barang Ditambah', 'Satuan'])
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
        Nama_Barang_Baru = input('Masukkan nama barang baru: ')
        Jenis_Barang_Baru = input('Masukkan jenis barang baru: ')
        Jumlah_Barang_Baru = int(input('Masukkan jumlah barang baru: '))
        Satuan = 'pcs'
        TabelUtama.append([Nama_Barang_Baru,Jenis_Barang_Baru,Jumlah_Barang_Baru,Satuan])
        printing_tabel()

    if pilihanmenu == '3':
        printing_tabel()
        Index_Hapus = int(input('Masukkan index barang yang akan dihapus: '))
        del TabelUtama[Index_Hapus]
        printing_tabel()

    if pilihanmenu == '4':
        printing_tabel()
        while True:
            Index_Ambil = int(input('index barang yang akan diambil:'))
            Quantity_Ambil = int(input('Masukkan jumlah barang yang akan diambil: '))
            Satuan = 'pcs'
            if Quantity_Ambil > TabelUtama[Index_Ambil][2]:
                print ('Jumlah stock kurang, silahkan masukkan angka yang benar.')
            else:
                Cart_Ambil.append([Index_Ambil,TabelUtama[Index_Ambil][0],TabelUtama[Index_Ambil][1],Quantity_Ambil,Satuan])
                printing_cart_ambil()
                TabelUtama[Index_Ambil][2] -= Quantity_Ambil
                Cart_Ambil.clear()
                printing_tabel()
                break

    if pilihanmenu == '5':
        printing_tabel()
        while True:
            Index_Tambah = int(input('index barang yang akan ditambah:'))
            Quantity = int(input('Masukkan jumlah barang yang akan ditambah: '))
            Satuan = 'pcs'
            Cart_Tambah.append([Index_Tambah,TabelUtama[Index_Tambah][0],TabelUtama[Index_Tambah][1],Quantity,Satuan])
            printing_cart_tambah()
            TabelUtama[Index_Tambah][2] += Quantity
            break
        Cart_Tambah.clear()
        printing_tabel()
    if pilihanmenu == '6':
        break

