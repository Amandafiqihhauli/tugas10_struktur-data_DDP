# jawaban BAGIAN 1
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikat_lulus(data):
    lulus = [mahasiswa['nama']
         for mahasiswa in data
         if mahasiswa['nilai'] > 65]
    return lulus

hasil = predikat_lulus(hasil_akhir)
print('siswa yang lulus:', hasil)

#  jawaban BAGIAN 2 no.1
def fungsi(buah):
    list_terbalik = []
    
    for i in range (len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik

buahnya = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_list_buah_terbalik = fungsi(buahnya)
print(hasil_list_buah_terbalik)

# jawaban BAGIAN 2 no.2
def fungsi(nama_buah):
    hasil_duplikasi = []
    
    for buah in nama_buah:
        hasil_duplikasi.append(buah)
        hasil_duplikasi.append(buah)
    return hasil_duplikasi

buahnya = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
duplikasian = fungsi(buahnya)
print(duplikasian)

# jawaban BAGIAN 2 no.3
def fungsi(kata):
    huruf_konsonan = ''
    
    for huruf in kata:
        if huruf not in ('aiueo'):
            huruf_konsonan += huruf
    return huruf_konsonan

kalimatnya = 'Nurul Fikri'
hasil_konsonan = fungsi(kalimatnya)
print(hasil_konsonan)    
        



    
         
    