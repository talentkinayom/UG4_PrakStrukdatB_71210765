import json

karyawan = int(input('Masukkan jumlah karyawan baru : '))
for i in range(karyawan):
    nama = input('Masukkan nama : ')
    list_karyawan = list()
    dict_karyawan = dict()
    dictalamat = dict()
    dictkolega = dict()
    dictKaryawan = dict()
    alamat = input('Masukkan alamat : ')
    dictKaryawan['Alamat'] = alamat
    kolega = int(input('Masukkan jumlah kolega : '))
    listkolega = list()
    for j in range (kolega):
        jmlhKolega = input('Masukkan nama kolega ke-{} : '.format(str(j + 1)))
        listkolega.append(jmlhKolega)
    dictkolega['Kolega'] = listkolega
    dict_karyawan['Karyawan'] = dictKaryawan
    list_karyawan.append(dict_karyawan)
    with open('karyawan.json', 'r') as datafile:
        data = json.load(datafile)
        data[nama] = list_karyawan
    with open('karyawan.json', 'w') as datafile:
        json.dump(data, datafile)
    print('=== Data berhasil ditambahkan ===\n')